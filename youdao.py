import sys
from urllib.request import urlopen
from html.parser import HTMLParser

def get_result(word):
        url = 'http://fanyi.youdao.com/openapi.do?keyfrom=majunzhe&key=27448872&type=data&doctype=xml&version=1.1&q='
        query_url = url + word
        result = urlopen(query_url).read().decode('utf-8')
        return result

class WordResultParser(HTMLParser):
        bHandled = False
        bExplain = False
        data_meaning = ''
        output = ''
        tags = ('phonetic', 'ex', 'key')
        def parse_data(self, data):
                beg_pos = data.rfind('[') + 1
                end_pos = data.find(']', beg_pos, len(data))
                if end_pos == -1:
                        end_pos = len(data)
                #print(beg_pos)
                #print(end_pos)
                #print(data)
                self.data_meaning = data[beg_pos:end_pos]

        def handle_starttag(self, tag, attrs):
                if 'basic' == tag:
                        self.output += '基本释义：\n\t'
                elif 'web' == tag:
                        self.output += '\r网络释义：\n\t'
                elif 'explain' == tag:
                        self.bExplain = True
                if tag in self.tags:
                                                                                                                                    1,1          顶端
