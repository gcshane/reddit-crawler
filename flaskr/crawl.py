from flask import Blueprint
from dotenv import load_dotenv
from datetime import datetime
import praw, os, pymongo

load_dotenv()

bp = Blueprint('main', __name__)

@bp.route('/crawl/<subreddit_name>/<int:top>', methods=['GET'])
def crawl(subreddit_name, top):
        
    reddit = praw.Reddit(
        client_id = os.environ.get('client_id'),
        client_secret = os.environ.get('client_secret'),
        user_agent = os.environ.get('user_agent')
    )
    sub_reddit = reddit.subreddit(subreddit_name)
    top_posts = sub_reddit.top(time_filter='day', limit=top)

    result = [{
        "title": post.title,
        "score": post.score,
        "url": post.url,
        "permalink": post.permalink
    } for post in sorted(top_posts, key=lambda x: x.score, reverse=True)]

    document = {"crawl_time" : datetime.now() ,"items" : result}
    myclient = pymongo.MongoClient(os.environ.get('mongo_uri'))
    mydb = myclient["reddit_crawler"]
    mycol = mydb[subreddit_name]
    mycol.insert_one(document)

    return result