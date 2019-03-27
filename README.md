# scraping-template
template for basic scraping

## 環境
python 3.60
pip 19.0.2
beautifulsoup4==4.7.1     # via bs4
bs4==0.0.1
certifi==2019.3.9         # via requests
chardet==3.0.4
idna==2.8                 # via requests
pymysql==0.9.3
requests==2.21.0
soupsieve==1.8            # via beautifulsoup4
urllib3==1.24.1           # via requests

## ファイル説明

### 1. config.py
- databaseのアカウント情報を記入する場所
- 全体で使うグローバル定数を定義する場所

### 2. makeTable.sql
- databaseにインポートしてテーブルを作成するためのコード

### 3. requirements.in
- 必要なライブラリーをここに記入

### 4. article.py
- 記事を保管するためのクラス

### 5. save_article.py
- articleを渡してdatabaseに保存するためのクラス

### 6. main.py
- スクレイピングのコードをここに書く

## 使い方
