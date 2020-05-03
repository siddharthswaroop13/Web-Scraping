


import nltk
from newspaper import Article

#Get the article
url = 'https://www.washingtonpost.com/technology/2019/07/17/you-downloaded-faceapp-heres-what-youve-just-done-your-privacy/?noredirect=on&utm_term=.1938589d078f'
article = Article(url)

# Do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

#Get the authors
print(article.authors)


#Get the publish date
print(article.publish_date)

#Get the top image
print(article.top_image)


#Get the article text
print(article.text)


