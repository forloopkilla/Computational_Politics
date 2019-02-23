import jieba
import string
import nltk

import jieba
import string
import nltk
def get_chinese_characters(raw):
    """Return list of Chinese characters in sentence.
    :param raw: raw chinese text
    """
    return list(sentence)

def get_chinese_words(raw):
    """Return list of Chinese words in sentence without stopwords. 
    :param raw: raw chinese text
    """
    stop_words = open("C:/Users/ASUS/Desktop/Thesis/stop_words/stop_words.txt")
    stop_words = stop_words.read()
    tokens = jieba.lcut(raw)
    result = [i for i in tokens if not i in stop_words]
    return result
    
def get_chinese_character_positions(raw):
    """Return a list of characters with their positions in the words. 
    :param raw: raw chinese text
    """
    return [u'{}{}'.format(char, i)
            for word in get_chinese_words(raw)
            for i, char in enumerate(word)]

def get_topic_distribution(lda_model, raw_input,sentences):
    """Return a vecor of topical distribution of each document or text. 
    :param raw: raw chinese text
    """
    dictionary = Dictionary(sentences)
    other_corpus = [dictionary.doc2bow(text) for text in raw_input] # raw input should be tokenized
    unseen_doc = other_corpus[0]
    vector = lda_model[unseen_doc]
    return vector[0]
    
def get_NdaysAgo_Data_from(today,date_col,df, days):
    """Retrieves data N-days ago. 
    :param today: format = 'YYYY-MM-DD'
    :param date_col:
    :param days: n days ago 
    :return: df with desired time frame
    """
    today = pd.to_datetime(today)
    begin = today - pd.offsets.Day(days)
    return(df[(date_col < today) & (date_col > begin)])

def get_NdaysAhead_Data_from(today,date_col,df, days):
    """Retrieves data N-days ahead in the future, in relations to "today". 
    :param today: format = 'YYYY-MM-DD'
    :param date_col: your 'date' column (datetime64) format
    :param days: n days in the future 
    return: df with desired time frame
    """
    today = pd.to_datetime(today)
    begin = today + pd.offsets.Day(days)
    return(df[(date_col >= today) & (date_col <= begin)])
