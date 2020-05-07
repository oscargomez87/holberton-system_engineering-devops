#!/usr/bin/python3
"""Queries Reditt's API"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries number of subscribers for a given subreddit

    Arguments.
        subreddit: subreddit to query subscribers count
    Return.
        number: subscribers count
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'hbtn/project'}
    res = requests.get(url, headers=headers)
    if (res.status_code == 200):
        return res.json()['data']['subscribers']
    else:
        return 0
