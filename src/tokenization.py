import nltk

#Download punkt package
nltk.download('punkt') 

txt = "Robofied is a comprehensive Artificial Intelligence platform based in Gurugram,Haryana working towards democratizing safe artificial intelligence towards a common goal of Singularity. At Robofied, we are doing research in speech, natural language, and machine learning. We develop open-source solutions for developers which empowers them so that they can make better products for the world. We educate people about Artificial Intelligence, its scope and impact via resources and tutorials."

#Sentence tokenization is spliting of paragraph in it's component sentences
sentence = nltk.sent_tokenize(txt)
for sents in sentence:
    print(sents)
    print()

#Word Tokenization is splitting of paragraph in it's word components
for sents in sentence:
    words = nltk.word_tokenize(sents)
    print(words)
    print()
