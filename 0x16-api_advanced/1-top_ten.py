#!/usr/bin/python3
"""Queries reddit API"""
import requests


def top_ten(subreddit):
    """
    Queries subreddit for the first 10 hot posts

    Arguments.
        subreddit: subreddit to query
    """
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'user-agent': 'windows:osgthbtnapp:task2'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('None')
    else:
        for idx, post in enumerate(response.json()['data']['children']):
            if idx < 10:
                print(post['data']['title'])
            else:
                break
