#An example of how to use the wordnet lemmatizer on words and sentences.

import nltk
#Download nltk package
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer 

lemmatizer = WordNetLemmatizer()

#sentence to be lemmatized
sentence = "Robofied is a comprehensive Artificial Intelligence platform based in Gurugram,Haryana working towards democratizing safe artificial intelligence towards a common goal of Singularity. At Robofied, we are doing research in speech, natural language, and machine learning. We develop open-source solutions for developers which empowers them so that they can make better products for the world. We educate people about Artificial Intelligence, its scope and impact via resources and tutorials."

#Split the sentence into it's word components
word_list = nltk.word_tokenize(sentence)

print(word_list)

#Lemmatize list of words and join
lemmatized_output = ' '.join([lemmatizer.lemmatize(wrd) for wrd in word_list])

print(lemmatized_output)



