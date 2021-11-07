import praw
import pandas
from flask import Flask, request, Response
from prawcore import NotFound


APP = Flask(__name__)
reddit = praw.Reddit(client_id='VGrBHwVwAalrdBJ9Wqm3vw', client_secret='d6TPJWt1vNfQ9Z9ldX-NtqY7wWLXOg',
                     user_agent='RedScrape')

NOT_FOUND = {'ERROR': 'SUBREDDIT DOES NOT EXIST!'}
VAR_ERROR = {'ERROR': 'YOUR VARIABLES ARE INCORRECT - PLEASE SEE README AT https://wilkiechrisj.github.io/redscraper/'}

TIMEFRAME = ['hour', 'day', 'week', 'month', 'year', 'all']
IMG_TAGS = ['.jpg', '.jpeg', '.png', '.gif']


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
            name = NOT_FOUND
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
        time = 'all'

    return name, num, time


def format_table(posts):

    for index in range(0, len(posts)):
        if posts[index][2][-4:] in IMG_TAGS:
            posts[index][2] = '<img src="' + posts[index][2] + '" width=300>'
        if posts[index][3]:
            posts[index][2] = posts[index][3]
        del posts[index][3]
    return posts


@APP.route('/redscraper/', methods=['GET'])
def root():
    with open("README.txt", "r") as file:
        content = file.read()
    return Response(content, mimetype='text/plain')


@APP.route('/redscraper/sub', methods=['GET'])
def sub():

    name = request.args.get('subreddit')
    num = request.args.get('limit')
    time = request.args.get('time')

    name, num, time = validate_args(name, num, time)

    if name is NOT_FOUND:
        return NOT_FOUND
    if not name or not num or not time:
        return VAR_ERROR

    subreddit = reddit.subreddit(name).top(time, limit=num)
    posts = []

    for post in subreddit:
        posts.append([post.title, post.url, post.url, post.selftext])

    posts = format_table(posts)
    posts = pandas.DataFrame(posts, columns=['TITLE', 'URL', 'CONTENT'])

    return posts.to_html(escape=False, index=False, render_links=True, justify='center', table_id='reddit_data')


if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=8080, debug=True)
