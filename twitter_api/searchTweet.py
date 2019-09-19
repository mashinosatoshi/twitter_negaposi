# -*- coding: utf-8 -*-
from config import config
from requests_oauthlib import OAuth1Session
"""
ツイートを取得する
ツイッターAPIへ接続するため、./config.pyへトークンなどを設定しなければならない
"""


def get_tweet(q, count=None, max_id=None):
    # OAuth認証部分
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)

    # Enedpointへ渡すパラメーター
    params = {
        'q': q,
        'include_rts': 0,   # リツイートしたものは含めない
        'exclude_replies': 1,   # リプライは含めない
    }
    # 取得数があれば設定する
    if count is not None:
        params['count'] = count
    # 過去を遡る際に使用する
    if max_id is not None:
        params['max_id'] = max_id

    return twitter.get('https://api.twitter.com/1.1/search/tweets.json', params=params)
