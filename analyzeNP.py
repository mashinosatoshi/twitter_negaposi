# -*- coding: utf-8 -*-
import os, re, MeCab, pandas
"""
ネガポジ判定
"""

class analyzeNP:
    """
    初期値の読み込み
    判定表の作成、形態素解析メソッド
    """
    def __init__(self):
        trans = {'n': -1, 'e': 0, 'p': 1}
        dic_file = os.path.dirname(os.path.abspath(__file__)) + '/pn.csv.m3.120408.trim'
        pd_dic = pandas.read_csv(dic_file, sep='\t', header=None)
        t_ward_set = {}

        for col in pd_dic.values:
            if col[1] in trans:
                t_ward_set[col[0]] = trans[col[1]]
            else:
                t_ward_set[col[0]] = 0
        self.ward_set = t_ward_set

        # 形態素解析実行メソッド
        self.m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        self.m.parseToNode('')

    """
    解析実行
    """
    def analyze(self, t):
        # 引用RTに入るURL等は解析対象から外す
        t = re.sub('https?:\/\/[\w\/:%#\$&\?\(\)~\.=\+\-]+','',t)
        ma = self.m.parseToNode(t)
        score = 0
        count = 0
        while ma:
            text = ma.feature.split(',')[6]
            for i in range(len(text), 0, -1):
                # 前方一致で見つかるまで判定表と付き合わせる
                if text[0:i] in self.ward_set:
                    score += self.ward_set[text[0:i]]
                    count += 1
                    break
            ma = ma.next
        if count == 0:
            return 0
        return score / count
