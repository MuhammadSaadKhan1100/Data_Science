# Automated News Summarizer 📝:
![image](https://user-images.githubusercontent.com/112848881/193465433-3ee507b2-cd54-42b9-8ccc-c57f45e7af8c.png)

* Machine learning algorithm is doing the summarization for us with no manual effort ofgoing the News.
* It is the text summarization of the news

# Contents 📈:
* Introduction to news summarizer
* Packages
* implementation in proteus using Jupyter Notebook
* Extract required text
* Finally build an Automated News Summarizer

# Text summarization 📃:
* Extracting meaningful text from a large chunk of data using algorithms powered by Natural Language Processing(NLP)
* A field of machine learning and national language processing
* Implemented in a variety of websites and mobile applications
* Helps engineers and data scientists create software  that can quickly find extract keywords from summarized text

# Types of Text Summarization 2️⃣:
* Extraction
* Abstraction

# Extraction:
* It extracts objects from the entire object collection without modifying the objects themselves
# Abstraction:
* Paraphrases the text and modifies the objects.

# Installation:
![image](https://user-images.githubusercontent.com/112848881/193464349-254bc741-f85f-4662-85c6-9c91a8d49fea.png)

# Random summarized output:
![image](https://user-images.githubusercontent.com/112848881/193465381-ae2d8cda-e9d9-4c9f-b7fd-49df42d54264.png)

 # Random summarizer.py
 ```python

# # News Extraction

# ### Import Packages

# In[1]:


from bs4 import BeautifulSoup
from requests import get


# ### CLI

# In[48]:


import sys #for argument parsing

# Exception Handling

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the  URL")


# ### Creating a Function to Extract only Text from `<p>` Tags

# In[17]:


def get_only_text(url):
 """ 
  return the title and the text of the article
  at the specified url
 """
 page = get(url)
 soup = BeautifulSoup(page.content, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 #text = soup.text
 title = ' '.join(soup.title.stripped_strings)
 return title , text    


# ### Calling the function with the desired News URL

# In[18]:


#url = "https://en.wikinews.org/wiki/Global_markets_plunge"


# In[19]:


text = get_only_text(url)


# In[26]:


#len(text[1])


# In[27]:


#text[1]


# ### Number of Words - Original Text

# In[28]:


#text[0]


# In[30]:


#len(str.split(text[1]))


# # Summarization

# In[36]:


from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


# ### Printing the Summarized Text
# 
# ### Method #1 - Word Count

# In[35]:


#text[1]


# In[37]:


print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), word_count=100))


# In[52]:


print("\n\nLength of the summarized text: " + str(len(str.split((summarize(repr(text[1]), word_count=100))))))


# ### Number of Words - Summarized Text

# In[42]:


#print ("Title : " + text[0])
#print ("Summary : ")
#print (summarize(repr(text[1]), ratio=0.1))


# In[43]:


summarized_text = summarize(repr(text[1]), ratio=0.1)


# ### Number of Words - Summarized Text

# In[44]:


#len(str.split(summarized_text))


# ### Keywords

# In[47]:


#print ('\nKeywords:')
#print (keywords(text[1], ratio=0.1, lemmatize=True))


# In[16]:
 ```
* 🔚
