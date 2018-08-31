#!/usr/bin/python3
""" Api querie for all tiles"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'https://reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    headers = {'user-agent': 'mikenike'}
    r = requests.get(url, headers=headers)

    try:
        for i in r.json()['data']['children']:
            hot_list.append(i['data']['title'])
        after = r.json()['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return (hot_list)
    except:
        return None
