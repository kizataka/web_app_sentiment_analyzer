## 概要
Twitterから特定の人物名のツイートを取得し、自然言語処理による感情分析を用いてツイート内容を解析することでその人物に関する肯定的なツイートのみを表示させるアプリです。  

（TwitterAPIの規約変更によりツイート取得ができなくなったため、kaggleのデータセットをツイート取得に見立てて擬似的に動かせるようにしました）

#### webアプリURL
https://emotional-analysis.streamlit.app/  

#### デモ動画
![web_app_movie](https://github.com/kizataka/web_app_sentiment_analyzer/assets/112063667/c514762d-908b-4e8a-b31a-8f00877578e2)  


## 機能一覧
* ファイルのアップロード
* データのサンプル表示
* サイドバーでの検索設定
    * データのカラム選択
    * キーワード検索
    * 取得するデータ数の指定
    * 感情フィルターの選択
* 文章の感情分析機能
* 分析結果の表示

## 使用技術一覧
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