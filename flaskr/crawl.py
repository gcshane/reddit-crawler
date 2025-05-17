from flask import Blueprint
import praw, os
from dotenv import load_dotenv

load_dotenv()

bp = Blueprint('main', __name__)

@bp.route('/crawl/<subreddit>/<int:top>', methods=['GET'])
def crawl(subreddit, top):
    reddit = praw.Reddit(
        client_id = os.environ.get('client_id'),
        client_secret = os.environ.get('client_secret'),
        user_agent = os.environ.get('user_agent')
    )
    subreddit = reddit.subreddit(subreddit)
    top_posts = subreddit.top(time_filter='day', limit=top)
    return [{
        "title": post.title,
        "score": post.score,
        "url": post.url,
        "permalink": post.permalink
    } for post in sorted(top_posts, key=lambda x: x.score, reverse=True)]