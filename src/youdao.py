# *-- coding: utf-8
#! /usr/bin/python3
import xml.etree.ElementTree as et
from urllib.request import urlopen
import sys
url_query = 'http://fanyi.youdao.com/openapi.do?keyfrom=majunzhe&key=27448872&type=data&doctype=xml&version=1.1&q='

def get_xml(word):
	url = url_query + word
	data = urlopen(url).read().decode('utf-8')
	return data

# format string for outputing
fs = '\t英： {}, 美: {}\n\t基本释义:\n\t\t{}\n\t网络释义:\n\t\t{}'
def parse_xml(data):
	result = fs
	root = et.fromstring(data)
	phonetic = root.find('.//phonetic').text.replace('\n', '')
	us_phone = root.find('.//us-phonetic').text.replace('\n', '')
	basic = root.find('basic')
	basic_ex = ''
	for ex in basic.findall('.//ex'):
		basic_ex += ex.text.replace('\n', '') + '\n\t\t'
	basic_ex = basic_ex.rstrip('\n\t\t')
	web = root.find('web')
	web_ex = ''
	for explain in web.findall('explain'):
		web_ex += explain.find('key').text.replace('\n', '')
		for ex in explain.findall('./value/ex'):
			web_ex += ex.text.replace('\n', '') + ','
		web_ex += '\n\t\t'
	web_ex = web_ex.rstrip('\n\t\t')
	return fs.format(phonetic, us_phone, basic_ex, web_ex) + '\n'

def go_ahead(word):
	data = get_xml(word)
	result = parse_xml(data)
	print(result)

def main():
	if len(sys.argv) > 1:
		for word in sys.argv[1:]:
			go_ahead(word)
			print('-'*80)
	else:
		while True:
			word = input('>>>')
			if '@' == word:
				break
			go_ahead(word)
if __name__ == '__main__':
	main()
