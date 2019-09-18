import MeCab
"""
形態素解析
"""
def init():
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    m.parseToNode('')
    return m