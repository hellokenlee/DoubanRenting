## 豆瓣租房·改

- - -

- 名字 Neta From 《中二病也要谈恋爱 剧场版》
- 豆瓣的搜索重复率太高了，而且很多限女生的房源
- 用爬虫+过滤滤掉了无效结果
- 依赖：Python2.7 BeautifulSoup3 Urllib2 tonado

- - -

![](README/origin.png)

- 豆瓣上的搜索有重复主题和仅限女生

![](README/origin2.png)

- 一个人发了无数条刷屏

- - -

#### 豆瓣租房·改 
- 可以勾选是否过滤重复主题
- 可以勾选是否过滤仅限女生
- 可以根据新鲜度选择： 最近一天发布的消息； 最近三天发布的消息； 最近一周发布的消息等；


![](README/example.png)


### 使用

- 安装 Python2.7 和 pip
- `pip install beautifulsoup`
- `pip install tornado`
- 在安装目录下`python DoubanServer.py`
- 浏览器访问 `http://127.0.0.1:8081` 即可


也可以直接访问( 不稳定的 ) [服务器](http://133.130.112.26:8081)。 但速度会比较慢。
