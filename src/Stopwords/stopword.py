#importing libraries
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
  
text = "Robofied is a comprehensive Artificial Intelligence platform based in Gurugram,Haryana working towards democratizing safe artificial intelligence towards a common goal of Singularity. At Robofied, we are doing research in speech, natural language, and machine learning. We develop open-source solutions for developers which empowers them so that they can make better products for the world. We educate people about Artificial Intelligence, its scope and impact via resources and tutorials."

#List of stop words  
stop_words = set(stopwords.words('english'))  

#Token of words
token = word_tokenize(text)  
  
filtered_sentence = [w for w in token if not w in stop_words]  
  
filtered_sentence = []  
  
for w in token:  
    if w not in stop_words:  
        filtered_sentence.append(w)  
  
print(" ".join(token)) 
print(" ".join(filtered_sentence)) 
