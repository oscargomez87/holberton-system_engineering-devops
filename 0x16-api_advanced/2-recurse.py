#!/usr/bin/python3
"""Queries reddit API"""
import requests
headers = {'user-agent': 'windows:osgthbtnapp:task3'}


def recurse(subreddit, after=None, hot_list=[]):
    """
        Queries all hot posts in a given subreddit

        Args:
            subreddit: subreddit to query posts from
            after: page to start from
            hot_lost: list to save posts in

        returns:
            list: list of hot posts

    """
    url = 'https://www.reddit.com/r/{}.json?after={}&limit=100'.format(
        subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        response.raise_for_status()
    except:
        return None
    for post in response.json()['data']['children']:
        hot_list.append(post['data']['title'])
    after = response.json()['data']['after']
    if after is not None:
        recurse(subreddit, after, hot_list)
    if hot_list:
        return hot_list
    else:
        return None
