import streamlit as st
import pandas as pd
import chardet
import requests
from sql_app.preprocessing import preprocess_text  # 前処理関数のインポート

st.title('ツイート感情分析アプリ')
st.write('')
st.write(
    """
    このアプリはTwitterから検索ワードに関するツイートを取得してその内容を感情分析し、
    ポジティブまたはネガティブなツイートのみを表示させるアプリです。
    """
)
st.write('')

uploaded_file = st.file_uploader('csvファイルをアップロードしてください', type='csv')

if uploaded_file is not None:

    # エンコーディングの設定
    rawdata = uploaded_file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

    uploaded_file.seek(0)
    data = pd.read_csv(uploaded_file, encoding=encoding)

    st.write('')
    st.write('データの先頭5件を表示しています')
    st.write(data.head())
    st.write('')

    # サイドバーの設定
    st.sidebar.header('検索設定')
    column_to_process = st.sidebar.selectbox('ツイートが含まれるカラムの選択:', data.columns)
    st.sidebar.write('')
    keyword = st.sidebar.text_input('検索ワード:', value='キーワードを入力してください')
    st.sidebar.write('')
    num_comments = st.sidebar.slider('取得するツイート数:', min_value=1, max_value=len(data), value=10, step=10)
    st.sidebar.write('')
    st.sidebar.write('取得するツイートの期間指定:')
    date_from = st.sidebar.date_input('何日から')
    date_to = st.sidebar.date_input('何日まで')
    st.sidebar.write('')
    sentiment_filter = st.sidebar.radio('感情選択:', options=['Positive', 'Negative'])

    st.write('検索設定が完了したら下の分析開始ボタンを押してください')
    st.write('')

    if st.button('分析開始'):

        # データの前処理
        filtered_data = data[data[column_to_process].str.contains(keyword, case=False, na=False)]
        filtered_data = filtered_data.head(num_comments)

        filtered_data['sentiment'] = ''
        filtered_data['sentiment_score'] = 0.0

        filtered_data = filtered_data[[column_to_process, 'sentiment', 'sentiment_score']]

        # 感情分析の実行
        for index, row in filtered_data.iterrows():
            url = 'https://sentiment-analyzer-xrp3.onrender.com/analyze_sentiment/'
            response = requests.post(url, json={'text': row[column_to_process]})

            if response.status_code == 200:
                sentiment_data = response.json()
                filtered_data.at[index, 'sentiment'] = sentiment_data['sentiment']
                filtered_data.at[index, 'sentiment_score'] = sentiment_data['sentiment_score']
                
            else:
                st.error(f'感情分析エラー:{response.text}')  # APIエラーの表示

        if sentiment_filter == 'Positive':
            filtered_data = filtered_data[filtered_data['sentiment'] == 'POSITIVE']
        elif sentiment_filter == 'Negative':
            filtered_data = filtered_data[filtered_data['sentiment'] == 'NEGATIVE']

        st.success('分析が完了しました')
        st.markdown('## ツイート一覧')
        st.write(f'{sentiment_filter}なツイートのみ表示しています')
        st.write(f'表示件数:{num_comments}')

        # sentiment_scoreの大きい順に並び替え
        filtered_data = filtered_data.sort_values(by='sentiment_score', ascending=False)

        # テキストの表示
        for index, row in filtered_data.iterrows():
            st.markdown(f'#### Tweet {index + 1}')
            st.write(row[column_to_process])
            st.write(f'{row["sentiment"]}: {row["sentiment_score"]}')
            st.write('---')
