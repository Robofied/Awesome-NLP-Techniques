#install textblob using "pip install textblob" and then import it
from textblob import TextBlob, Word

#Lemmatize the sentence
sentence = "Robofied is a comprehensive Artificial Intelligence platform based in Gurugram,Haryana working towards democratizing safe artificial intelligence towards a common goal of Singularity. At Robofied, we are doing research in speech, natural language, and machine learning. We develop open-source solutions for developers which empowers them so that they can make better products for the world. We educate people about Artificial Intelligence, its scope and impact via resources and tutorials."

sent = TextBlob(sentence)

" ". join([w.lemmatize() for w in sent.words])
