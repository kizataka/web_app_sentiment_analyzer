# 概要
Twitterから特定の人物名に関するツイートを取得し、自然言語処理による感情分析を用いてツイート内容を解析することでその人物に関する肯定的なツイートのみを表示し、誹謗中傷のような批判的なツイートが目に入らないようにするアプリです。  

（TwitterAPIの規約変更によりツイート取得ができなくなったため、Kaggleのデータセットをツイート取得に見立てて擬似的に動かせるようにしました。）

### webアプリURL
https://emotional-analysis.streamlit.app/  

### データセットについて
Kaggleの[Women's E-Commerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews?resource=download)を例として利用しました。  
ECサイトでの婦人服の売上データとなっており、商品分類名や商品に関するレビュー文が格納されています。  
レビュー文をツイートに置き換えて考え、ファイルをアップロードすることでツイートを取得できたと仮定しています。

### デモ動画
本来であれば人物名で検索するところを商品分類名の一つであるshirtを入力し、shirtに関するレビューを集めてポジティブなレビューのみを表示するようにしています。  
デモ動画ではKaggleのデータを縮小したCSVファイル[test.csv](https://drive.google.com/file/d/1cAJ2OdLswGHbR9fdrt8YFQYxP2c1SnKL/view?usp=drive_link)を使用しています。  

![web_app_movie](https://github.com/kizataka/web_app_sentiment_analyzer/assets/112063667/c514762d-908b-4e8a-b31a-8f00877578e2)  

# 機能一覧
* ファイルのアップロード
* データのサンプル表示
* サイドバーでの検索設定
    * データのカラム選択
    * キーワード検索
    * 取得するデータ数の指定
    * 感情フィルターの選択
* 文章の感情分析
* 分析結果の表示

# 使用技術一覧
* フロントエンドフレームワーク
    * streamlit 1.27.1
* フロントエンド言語
    * Python 3.9.13
* バックエンドフレームワーク
    * FastAPI 0.103.2
* バックエンド言語
    * Python 3.9.13
* データベース
    * SQLAlchemy 2.0.21
* 感情分析モデル
    * transformers(HuggingFaceのライブラリ) 4.33.3
* 環境構築
    * Poetry 1.6.1