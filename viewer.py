import streamlit as st
import requests

# Streamlitアプリのタイトル
st.title('HTTP GETリクエストのデモ')

# GETリクエストを送信する関数
def fetch_data(url):
    try:
        response = requests.get(url)
        # レスポンスが成功したかどうかを確認
        if response.status_code == 200:
            return response.text
        else:
            return f'Error: {response.status_code}'
    except Exception as e:
        return f'Error: {e}'

# ユーザーにURLを入力させる
url = 'http://localhost:8000'

# ボタンを設置し、クリックされたらGETリクエストを実行
if st.button('GETリクエストを送信'):
    result = fetch_data(url)
    st.text('レスポンス:')
    st.write(result)