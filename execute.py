# -*- coding: utf-8 -*-

import json
import getTimelineTweet

req = getTimelineTweet.get_tweet('matsugae_tmyk')
if req.status_code == 200:
    res = json.loads(req.text)
    print(len(res))
    for line in res:
        print(line['id'])
        print(line['text'])
        print('*******************************************')
else:
    print("Failed: %d" % req.status_code)