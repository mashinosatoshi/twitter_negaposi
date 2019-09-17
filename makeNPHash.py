# -*- coding: utf-8 -*-
import pandas as pd
import os
"""
極性対応表の読み込み
"""


def getData():
    dic_file = os.path.dirname(os.path.abspath(__file__)) + '/pn_ja.dic'
    pd_dic = pd.read_csv(dic_file, sep=':', encoding='cp932', header=None)
    kanji = {}
    yomi = {}

    for col in pd_dic.to_dict(orient="index").items():
        col = col[1]
        kanji[col[0]] = [col[2], col[3]]
        yomi[col[1]] = [col[2], col[3]]

    return [kanji, yomi]
