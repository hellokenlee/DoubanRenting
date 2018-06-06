# -*- coding:utf-8 -*-
__author__ = "KenLee"
__email__ = "hellokenlee@163.com"

import urllib2
import difflib
import time
from BeautifulSoup import BeautifulSoup

sexKeywords = ["女舍友", "限女", "女生"]

def GrapResult(searchKeyword, daysTilNow, useSimilarity, useSex):
	#
	print("[Spider]: keyword = " + searchKeyword + "; daysTilNow = " + str(daysTilNow) + "; antiSim = " + str(useSimilarity) + "; antiSex = " + str(useSex))
	#
	limitTime = time.localtime(time.time() - (daysTilNow * 60 * 60 * 24))
	res = []
	totalNum = 0
	index = 0
	flag = True
	#
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	#
	while flag and index < 1000:
		#
		url = "https://www.douban.com/group/search?start=" + str(index) + "&cat=1013&sort=time&q=" + searchKeyword
		print("[Spider] URL = " + url)
		try:
			print(headers)
			req = urllib2.Request(url = url, headers = headers)  
			page = urllib2.urlopen(req).read()
		except Exception as e:
			print(e)
			return (["Error"], 0)
		soup = BeautifulSoup(page)
		trs = soup.findAll("tr", attrs = {'class':['pl']})
		# 
		totalNum += len(trs)
		#
		hashTable = {}
		repetition = 0
		prevTitle = ""
		for tr in trs:
			# 判断时间
			releaseTime = tr.findAll("td", attrs = {'class':['td-time']})[0].get('title')
			releaseTime = time.strptime(releaseTime, '%Y-%m-%d %H:%M:%S')
			if releaseTime < limitTime:
				# print(releaseTime, limitTime, releaseTime < limitTime)
				flag = False
				break
			# 提取题目
			title = tr.td.a.string
			title = title.replace(" ", "")
			# 去除完全一样的
			if not hashTable.has_key(title):
				# 相邻相似度筛查
				if useSimilarity:
					ratio = difflib.SequenceMatcher(None, prevTitle, title).ratio()
					prevTitle = title
					if(ratio > 0.5):
						repetition += 1
						continue
				# 反性别歧视
				trueTitle = tr.td.a["title"]
				if useSex:
					fits = False
					for kw in sexKeywords:
						if kw in trueTitle:
							fits = True
							break
					if fits:
						#print(trueTitle)
						repetition += 1
						continue
				# 发现新的条目
				hashTable[title] = True
				res.append(tr)
			else:
				#
				if not useSimilarity:
					res.append(tr)
				else:
					repetition += 1
		#
		index += 50

	#
	
	return (res, repetition)
	pass

def main():
	res = GrapResult("广州", 3, True, True)
	for topic in res[0]:
		print(topic)
	
	print(len(res[0]), res[1])
	pass

if __name__ == '__main__':
	main()