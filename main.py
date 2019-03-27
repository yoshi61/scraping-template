import re
import requests
import chardet
import urllib
from bs4 import BeautifulSoup
from article import Article
from save_article import SaveArticle

""" sample """
# def saveAllLinkIdArticles():
# 	homeURL = "https://www.necoweb.com"
# 	saveIt = SaveArticle()
# 	resp = requests.get(homeURL)
# 	resp.encoding = resp.apparent_encoding
# 	soup = BeautifulSoup(resp.text, "html.parser")
# 	aTags = soup.find_all("a")
# 	for tag in aTags:
# 		if tag.get("href") is not None and 'detail' in tag.get("href"):
# 			URL = tag.get("href")
# 			articleId = re.findall(r'detail\.php\?id=(\d*)&', URL)[0]
# 			neco = Article(articleId, URL)
# 			saveIt.saveArticle(neco)
# 			saveIt.save_all_keywords(neco)
#
#
# saveAllLinkIdArticles()
