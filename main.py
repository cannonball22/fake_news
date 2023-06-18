"""
import streamlit as st
from helper import fake_news_det


query_params = st.experimental_get_query_params()
#print(query_params)

#st.write(query_params)
#st.title('Fake news dashboard')
#print(query_params["input"][0])

#fake_news_det(query_params["input"][0])
try:
    response = fake_news_det(query_params["input"][0])
    #st.write(response)
    st.json({'response': response})
except:
    st.write("error")
"""
from datetime import date

from flask import Flask,request, jsonify

from helper import fake_news_det

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {
        "greeting": ["hello", "world"],
        "date": date.today()
    }


@app.route('/input', methods=['GET'])
def search():
    args = request.args
    input = args.get('text')
    result = fake_news_det(input)
    return result


if __name__ == "__main__":
    hello_world()
