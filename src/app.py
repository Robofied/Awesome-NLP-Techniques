import streamlit as st
import nltk
import pandas as pd
import re
import numpy as np
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from textblob import TextBlob, Word
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
nltk.download('stopwords')

set(stopwords.words('english'))


def main():

    display = ["Home", "Tokenization", "Stemming",
        "Stopwords", "Lemmatization", "BagOfWords"]

    st.sidebar.title("Natural Language Processing")
    selected_box = st.sidebar.selectbox("Select any box", display)

    if selected_box == "Home":
        home()

    if selected_box == "Tokenization":
        token()

    if selected_box == "Stemming":
        stem()

    if selected_box == "Stopwords":
        stop()
    if selected_box == "Lemmatization":
        lemmat()

    if selected_box == "BagOfWords":
        bag()

    


def home():
    st.image('/home/lenovo/NLP/Robofied.png')
    st.markdown('''
    # Awesome-NLP-Techniques &nbsp; ![](https://img.shields.io/github/forks/Robofied/Awesome-NLP-Techniques?style=social) ![](https://img.shields.io/github/stars/Robofied/Awesome-NLP-Techniques?style=social) ![](https://img.shields.io/github/watchers/Robofied/Awesome-NLP-Techniques?style=social)

![](https://img.shields.io/github/repo-size/Robofied/Awesome-NLP-Techniques) ![](https://img.shields.io/github/license/Robofied/Awesome-NLP-Techniques?color=red)    [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Robofied/Awesome-NLP-Techniques)
![](https://img.shields.io/github/issues/Robofied/Awesome-NLP-Techniques?color=green) ![](https://img.shields.io/github/issues-pr/Robofied/Awesome-NLP-Techniques?color=green) ![](https://img.shields.io/github/downloads/Robofied/Awesome-NLP-Techniques/total) ![](https://img.shields.io/github/last-commit/Robofied/Awesome-NLP-Techniques) ![](https://img.shields.io/github/contributors/Robofied/Awesome-NLP-Techniques)

Natural language processing (NLP) is a subfield of [linguistics](https://en.wikipedia.org/wiki/Linguistics), [computer science](https://en.wikipedia.org/wiki/Computer_science), and [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of [natural language](https://en.wikipedia.org/wiki/Natural_language) data. The result is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves.

Challenges in natural language processing frequently involve [speech recognition](https://en.wikipedia.org/wiki/Speech_recognition), [natural language understanding](https://en.wikipedia.org/wiki/Natural_language_understanding), and [natural-language generation](https://en.wikipedia.org/wiki/Natural-language_generation).
    ''')

    st.markdown('''
        # License

Licensed under the [MIT License](LICENSE)

# Contributing to Awesome NLP Technique
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

A detailed overview on how to contribute can be found in the contributing guide. There is also an overview on GitHub.

If you are simply looking to start working with the voicenet codebase, navigate to the GitHub "issues" tab and start looking through interesting issues. There are a number of issues listed under Docs and good first issue where you could start out.

You can also triage issues which may include reproducing bug reports, or asking for vital information such as version numbers or reproduction instructions.

Or maybe through using you have an idea of your own or are looking for something in the documentation and thinking ‘this can be improved’. You can do something about it!

Feel free to ask questions on the mailing list or on Slack.

# Contributor
[Mansi Maurya](https://github.com/mansi75)

    ''')


def token():

    st.markdown("""   #  Tokenization

# What is Tokenization?

Tokenization is breaking a sentence, paragraph, or an text document into smaller units, such as words or characters. Each of these smaller units are called tokens. The tokens could be words, numbers or punctuation marks.




# Need of Tokenization

Tokenization is the most basic step to proceed with NLP. After tokenization the meaning of the text can be interpreted by analyzing the words present in the text. If we are given a paragraph, we need to get all sentences. From all these sentences, we need words and then only we can understand the text completely.


# Types of Tokenization

There are two types of Tokenizations:

1. Word Tokenization

2. Sentence Tokenization

   """, True)

    st.write(" **Word Tokenization** ")

    val = st.text_input("Enter a Paragraph")

    out = word_tokenize(val)

    out1 = sent_tokenize(val)

    if st.button("Sentence Tokenization"):
        st.success(out1)
    if st.button("Word Tokenization"):
        st.success(out)


def stem():
    st.markdown(""" #  Stemming

# What is Stemming?

Stemming is removing the suffix from a word and reduce it to its root word. It is a technique used to extract the base form of the words by removing affixes from them. For example the stem of words writing, writes or written is write.

        """, True)

    word_stemmer = PorterStemmer()

    val = st.text_input("Enter a word")

    out = word_stemmer.stem(val)
    if st.button("Stemming"):
        st.success(out)


def stop():
    st.markdown(""" # Stopwords

# What is stopwords?

Stopwords are the most common words in any natural language. For the purpose of analyzing text data and building NLP models, these stopwords might not add much value to the meaning of the document.

# Need of Stopwords

Tasks like text classification, where the text is to be classified into different categories, stopwords are removed from the given text so that more focus can be given to those words which define the meaning of the text.By removing stopwords,dataset size decreases and the time to train the model also decreases. Removing stopwords can help improve the performance as there are fewer and only meaningful tokens left. It could increase classification accuracy.

    """, True)

    stop_words = set(stopwords.words('english'))

    val = st.text_input("Enter a sentence/paragraph")

    word_tokens = word_tokenize(val)
    new_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            new_sentence.append(w)

    out = " ".join(new_sentence)
    if st.button("Stopwords"):
        st.success(out)


def lemmat():
    st.markdown(""" #  Stemming

# What is lemmatization?

Lemmatization is similar to stemming but it brings context to the words. The output after lemmatization is called ‘lemma’, which is a root word rather than root stem, the output of stemming. After lemmatization, we will get a valid word that means the same thing. Lemmatization is preferred over Stemming because lemmatization does morphological analysis of the words. One major difference with stemming is that lemmatize takes a part of speech parameter, “pos” If not supplied, the default is “noun.”


        """, True)

    nltk.download('punkt')

    val = st.text_input("Enter a sentence/paragraph")

    s = TextBlob(val)
    out = " ".join([w.lemmatize() for w in s.words])
    if st.button("Lemmatization"):
        st.success(out)




def bag():

    st.markdown(""" # Bag Of Words

# What is Bag Of Words?

Bag of words is a Natural Language Processing technique of text modelling. In technical terms, we can say that it is a method of feature extraction with text data. It is used to preprocess the text by converting it into a bag of words, which keeps a count of the total occurrences of most frequently used words. It keep track of word counts and disregard the grammatical details and the word order.

# Why bag of words are used?

With bag-of-Words we can convert variable-length texts into a fixed-length vector. Machine learning models work with numerical data. By using the bag of words technique, we can convert a text into its equivalent vector of numbers.


        """, True)

    val = st.text_input("Enter a senntence/paragraph")



    

    dataset = nltk.sent_tokenize(val)

    for i in range(len(dataset)):

        dataset[i] = dataset[i].lower()
        

        dataset[i] = re.sub(r'\W', ' ', dataset[i])
        dataset[i] = re.sub(r'\s+', ' ', dataset[i])


        
    word2count = {} 
    for data in dataset: 
        words = nltk.word_tokenize(data) 
        for word in words: 
            if word not in word2count.keys(): 
                word2count[word] = 1
            else: 
                word2count[word] += 1
    out = word2count
     

    if st.button("BagOfWOrds"):
        st.success(out)



    


    

    
        
 

 


    

         





    

        
    

    
    







    
   
    
    


    
if __name__ == '__main__':
    main()


