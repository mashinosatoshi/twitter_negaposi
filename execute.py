# -*- coding: utf-8 -*-
import json
import getTimelineTweet
import analyzeNP

anp = analyzeNP.analyzeNP()

req = getTimelineTweet.get_tweet('matsugae_tmyk', 200)

if req.status_code == 200:
    res = json.loads(req.text)
    print(len(res))
    sum_t = [anp.analyze(line['text']) for line in res]
    print(sum_t)
    print(sum(sum_t))
else:
    print("Failed: %d" % req.status_code)