from flask import Blueprint, send_file
from dotenv import load_dotenv
from datetime import datetime
from fpdf import FPDF
import praw, os, pymongo, telepot

load_dotenv()

bp = Blueprint('main', __name__)

@bp.route('/crawl/<subreddit_name>/<int:top>/<telegram_username>', methods=['GET'])
def crawl(subreddit_name, top, telegram_username):

    crawl_time = datetime.now()
        
    reddit = praw.Reddit(
        client_id = os.environ.get('client_id'),
        client_secret = os.environ.get('client_secret'),
        user_agent = os.environ.get('user_agent')
    )
    sub_reddit = reddit.subreddit(subreddit_name)
    top_posts = sub_reddit.top(time_filter='day', limit=top)

    result = []
    counter = 1

    pdf = FPDF()
    pdf.add_page()
    font_path = os.path.join(os.path.dirname(__file__), "fonts", "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=8)
    pdf.cell(0, 10, f'Top {top} posts from r/{subreddit_name} at {crawl_time}:', ln=1)
        
    for post in sorted(top_posts, key=lambda x: x.score, reverse=True):
        result.append({
            "title": post.title,
            "score": post.score,
            "url": post.url,
            "permalink": post.permalink
        })
        pdf.cell(0, 10, f'{counter}. Title: {post.title} | Score: {post.score} | URL: {post.url}' , ln=1)
        counter += 1

    pdf.output("report.pdf")

    document = {"crawl_time" : crawl_time,"items" : result}
    myclient = pymongo.MongoClient(os.environ.get('mongo_uri'))
    mydb = myclient["reddit_crawler"]
    mycol = mydb[subreddit_name]
    mycol.insert_one(document)

    bot = telepot.Bot(token=os.environ.get('telegram_token'))
    response = bot.getUpdates()
    for r in response:
        if r['message']['from']['username'] == telegram_username:
            bot.sendDocument(r['message']['from']['id'], open('report.pdf', 'rb'))
            break

    return result