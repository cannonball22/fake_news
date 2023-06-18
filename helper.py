import os

import joblib

# NLP libraries to clean the text data
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re


model = joblib.load(os.path.join(os.getcwd(), "static\\model.pkl"))
vectorization = joblib.load(os.path.join(os.getcwd(), "static\\tfidfvect.pkl"))

ps = PorterStemmer()
def wordopt(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [ps.stem(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)
    return text


def fake_news_det(news):
    input_data = {"text": [news]}
    new_def_test = pd.DataFrame(input_data)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]
    # print(new_x_test)
    vectorized_input_data = vectorization.transform(new_x_test)
    prediction = model.predict(vectorized_input_data)

    if prediction == 1:
        return ("Real News")
    else:
        return ("Fake News")






fake_news_det('U.S. Secretary of State John F. Kerry said Monday that he will stop in Paris later this week, amid criticism that no top American officials attended Sundayâ€™s unity march against terrorism.')