import praw
import pandas
from flask import Flask, request
from prawcore import NotFound


APP = Flask(__name__)
reddit = praw.Reddit()

NOT_FOUND = {'ERROR': 'SUBREDDIT DOES NOT EXIST!'}
VAR_ERROR = {'ERROR': 'YOUR VARIABLES ARE INCORRECT - PLEASE SEE README AT urlhere'}

TIMEFRAME = ['hour', 'day', 'week', 'month', 'year', 'all']


def subreddit(name, num):
    pass


def exists(name):

    try:
        reddit.subreddits.search_by_name(name, exact=True)
    except NotFound:
        return False
    return True


def validate_args(name, num, time):

    if name:
        if exists(name):
            pass
        else:
            name = False
    else:
        name = False

    if num:
        if num.isdigit():
            num = int(num)
        else:
            num = False
    else:
        num = 10

    if time:
        if time in TIMEFRAME:
            pass
        else:
            time = False
    else:
        pass

    return name, num, time


@APP.route('/', methods=['GET'])
def root():
    return 'Hello World!'


@APP.route('/sub', methods=['GET'])
def user_sub():

    name = request.args.get('subreddit')
    num = request.args.get('limit')
    time = request.args.get('time')

    validate_args(name, num, time)

    sub = reddit.subreddit(name).top


@APP.route('/all', methods=['GET'])
def r_all():

    sub = reddit.subreddit('all').hot(limit=10)
    posts = []

    for post in sub:
        posts.append([post.title, post.url, post.selftext])

    posts = pandas.DataFrame(posts, columns=['TITLE', 'URL', 'BODY'])

    return posts.to_html()


@APP.route('/test', methods=['GET'])
def test():
    var = request.args.get('var')
    print(type(var))
    return var


if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=8080, debug=True)
