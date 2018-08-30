#!/usr/bin/python3
""" Api limit to ten"""
import requests


def top_ten(subreddit):
    url = 'https://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'mikenike'}
    r = requests.get(url, headers=headers)

    try:
        for i in r.json()['data']['children']:
            print(i['data']['title'])
    except:
        return print('None')
