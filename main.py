import re
from bs4 import BeautifulSoup
import requests
import chardet
import urllib
from article import Article
from save_article import SaveArticle
import pymysql.cursors
import json
import datetime
from fabric.colors import green,red
now = datetime.datetime.now()

def saveAllLinkIdArticles():
	baseURL = "https://www.necoweb.com"
	partURL = "/neco/program/category.php?id="
	linkList = []
	saveIt = SaveArticle()
	for categoryId in range(2,10):
		categoryURL = baseURL + partURL + str(categoryId)
		resp = requests.get(categoryURL)
		resp.encoding = resp.apparent_encoding
		soup = BeautifulSoup(resp.text, "html.parser")
		aTags = soup.find_all("a")
		for tag in aTags:
			if tag.get("href") is not None and 'detail' in tag.get("href"):
				URL = tag.get("href")
				articleId = re.findall(r'detail\.php\?id=(\d*)&', URL)[0]
				neco = Article(articleId, categoryId)
				saveIt.saveArticle(neco)
				saveIt.save_all_keywords(neco)


# saveAllLinkIdArticles()
"""#デバグ用
neco = Article("4460", "3")
#neco.toString()
saveNeco = SaveArticle()
saveNeco.saveArticle(neco)
saveNeco.save_all_keywords(neco)
"""
