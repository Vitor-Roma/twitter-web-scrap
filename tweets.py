import datetime
import statistics
from math import ceil
from pprint import pprint
import snscrape.modules.twitter as st

query = 'Python'
profiles = []
for users in st.TwitterSearchScraper(query).get_items():
    if len(profiles) >= 50:
        break

    perfil = {
        'username': users.user.username,
        'displayed_name': users.user.displayname,
        'followers': users.user.followersCount,
        'following': users.user.friendsCount,
        'join_date': users.user.created,
        'website': users.user.linkUrl,
        'posts': [],
    }
    if perfil['followers'] > 1000:
        for i, tweets in enumerate(st.TwitterUserScraper(perfil['username']).get_items()):
            if i >= 10:
                break

            tweet = {
                'content': tweets.content,
                'date': tweets.date.date(),
                'url': tweets.url,
                'favorites': tweets.likeCount,
                'retweets': tweets.retweetCount,
                'replies': tweets.replyCount,
            }
            perfil['posts'].append(tweet)
        profiles.append(perfil)

post_dates = [post['date'] for profile in profiles for post in profile['posts']]
min_date = min(post_dates)
max_date = max(post_dates)
dates_with_posts = [{'date': min_date + datetime.timedelta(days=x), 'posts': 0} for x in
                    range((max_date - min_date).days + 1)]
for i, date_with_post in enumerate(dates_with_posts):
    qt_posts = [post_date for post_date in post_dates if post_date == date_with_post['date']]
    if len(qt_posts) > 0:
        dates_with_posts[i]['posts'] += len(qt_posts)

total_days = len(dates_with_posts)
total_weeks = ceil(total_days % 365 / 7)
total_months = ceil(total_days / 30)
total_posts = len(post_dates)

tweets_per_day = total_posts / total_days
tweets_per_week = total_posts / total_weeks
tweets_per_month = total_posts / total_months
mean_tweets_per_day = total_posts / total_days
mean_tweets_per_week = total_posts / total_weeks
mean_tweets_per_month = total_posts / total_months
median_tweets_per_day = statistics.median([date['posts'] for date in dates_with_posts])
median_tweets_per_week = ceil(median_tweets_per_day % 365 * 7)
median_tweets_per_month = ceil(median_tweets_per_day * 30)

results = {
    'tweets_per_day': tweets_per_day,
    'tweets_per_week': tweets_per_week,
    'tweets_per_month': tweets_per_month,
    'mean_tweets_per_day': mean_tweets_per_day,
    'mean_tweets_per_week': mean_tweets_per_week,
    'mean_tweets_per_month': mean_tweets_per_month,
    'median_tweets_per_day': median_tweets_per_day,
    'median_tweets_per_week': median_tweets_per_week,
    'median_tweets_per_month': median_tweets_per_month,
}

pprint(results)