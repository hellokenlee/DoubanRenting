# -*- coding:utf-8 -*-
__author__="KenLee"
__email__="ken_4000@qq.com"

import tornado.ioloop
import tornado.web
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

import os.path
import os
import urllib2

import DoubanSpider

# settings
settings={
	"static_path": os.path.join(os.path.dirname(__file__),"www/dist"),
	"debug":True,
}


port = 8081

# 
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#
		kw = "OvO"
		days_til_now = 3
		exclude_similar = True
		exclude_girl_only = True
		#
		if self.request.arguments.has_key("kw"):
			kw = self.get_argument('kw')
			print(kw)
			kw = urllib2.unquote(kw)
		if self.request.arguments.has_key("days"):
			days_til_now = int(self.get_argument('days'))
		if self.request.arguments.has_key("sim"):
			exclude_similar = bool(int(self.get_argument('sim')))
		if self.request.arguments.has_key("sex"):
			exclude_girl_only = bool(int(self.get_argument('sex')))
		#
		res = DoubanSpider.GrapResult(kw, days_til_now, exclude_similar, exclude_girl_only)
		#
		page = ""
		if(res[1] != -1):
			for tile in res[0]:
				page = page + "\n" + tile.prettify()
		#
		num = len(res[0])
		exclude_num = res[1]
		#
		print(days_til_now)
		self.render("./www/template.html", kw = kw, page = page, num = num, exclude_num = exclude_num, sex = exclude_girl_only, sim = exclude_similar, days = days_til_now)

# main func
def main():
	#
	application=tornado.web.Application([
		(r"/",MainHandler),
		],**settings)
	#
	application.listen(port)
	#
	tornado.ioloop.IOLoop.instance().start()
	#
	pass


if __name__ == '__main__':
	main()