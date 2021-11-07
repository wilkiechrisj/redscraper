- RedScraper -
- Christopher Wilkie -
- VS 1.0 11/7/2021 -

This service provides the top posts of a specified subreddit.
Send an HTTPS request to https://wilkiechrisj.github.io/redscraper/sub add the following HTTP variables as necessary.

*REQUIRED*
subreddit - The name of the subreddit (ex. 'all' or 'funny')

*OPTIONAL*
limit - The amount of posts you want. The more posts, the longer it will take to load. DEFAULT=10
time - The time period where the posts should come from. Select from hour, day, week, month, year, or all. DEFAULT=all

-------

EXAMPLE: https://wilkiechrisj.github.io/redscraper/sub?subreddit=all&limit=11&time=month

This will generate a table containing the top 11 posts of the month from the subreddit r/all

-------

The page will be a table with three columns; title, url, and content. Title will be the title of the post and the URL
will contain either a link to the post itself or a link to the content of the post. The content column contains one of
the following; loaded image, content link, text body.

The table in the page has an html id of "reddit_data" for easier manipulation.

Future possible updates - comments, loading videos and image albums, article summaries?
