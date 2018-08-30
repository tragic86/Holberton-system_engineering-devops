#!/usr/bin/python3
""" Api stuff"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'mikenike'}
    r = requests.get(url, headers=headers)

    try:
        return r.json()['data']['subscribers']

    except:
        return (0)
