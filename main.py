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
