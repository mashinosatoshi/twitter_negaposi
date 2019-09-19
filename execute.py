# -*- coding: utf-8 -*-
import json, collections
import analyzeNP
from twitter_api import getTimelineTweet
from twitter_api import searchTweet

anp = analyzeNP.analyzeNP()


req = getTimelineTweet.get_tweet('matsugae_tmyk', 200)

"""
if req.status_code == 200:
    res = json.loads(req.text)
    print(len(res))
    sum_n = 0
    sum_c = collections.Counter()
    for line in res:
        num, counter = anp.analyze(line['text'])
        sum_c.update(counter)
        sum_n += num
    print(sum_n)
    print(sum_c)
else:
    print("Failed: %d" % req.status_code)
"""
ward = 'パズドラ'
req = searchTweet.get_tweet(ward, 100)

if req.status_code == 200:
    res = json.loads(req.text)['statuses']
    print(len(res))
    sum_n = 0
    sum_c = collections.Counter()
    for line in res:
        num, counter = anp.analyze(line['text'])
        sum_c.update(counter)
        sum_n += num
    print(sum_n)
    print(sum_c)
else:
    print("Failed: %d" % req.status_code)
#"""