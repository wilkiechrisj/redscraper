import praw
import pandas
from flask import Flask


APP = Flask(__name__)
reddit = praw.Reddit(client_id='2QxECe_51Rkj5TXyv0RCPA', client_secret='tVmK3MuwFarRCQGTFNiebzxO9uSTTg',
                     user_agent='RedScraper')


@APP.route('/', methods=['GET'])
def root():
    return 'Hello World!'


@APP.route('/all', methods=['GET'])
def r_all():

    sub = reddit.subreddit('tifu').hot(limit=10)
    posts = []

    for post in sub:
        posts.append([post.title, post.score, post.url, post.selftext])

    posts = pandas.DataFrame(posts, columns=['TITLE', 'SCORE', 'URL', 'BODY'])

    return posts.to_html()


if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=8080, debug=True)
