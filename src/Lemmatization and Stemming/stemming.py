# importing required modules 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
   
p = PorterStemmer() 

#The sentence to be stemmed
sentence = "Robofied is a comprehensive Artificial Intelligence platform based in Gurugram,Haryana working towards democratizing safe artificial intelligence towards a common goal of Singularity. At Robofied, we are doing research in speech, natural language, and machine learning. We develop open-source solutions for developers which empowers them so that they can make better products for the world. We educate people about Artificial Intelligence, its scope and impact via resources and tutorials."

#Tokenizing the sentence
words = word_tokenize(sentence) 
   
for w in words: 
    print(w, " : ", p.stem(w)) 
