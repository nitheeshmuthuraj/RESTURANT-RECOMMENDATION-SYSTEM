
from predict import main as mn
import operator
import logging
import gensim
import pickle
import time
import nltk
from gensim import corpora
from gensim.corpora import BleiCorpus
from gensim.models import LdaModel
from pymongo import MongoClient
from settings import Settings
import pyLDAvis.gensim
import gensim.matutils
#from keras.models import load_model
#from keras.preprocessing.sequence import pad_sequences


import os
import time
import json
# import string as str

from pymongo import MongoClient

from settings import Settings



USER_D = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_STOP]
BUSINESS_D = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_STOP]



USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE]
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_PROFILE]

user_profile_cursor=USER_D.find()
business_profile_cursor=BUSINESS_D.find()

for i in user_profile_cursor:    
    USER_PROFILE.insert_one({
            "USER_ID":i["USER_ID"],
            "ENCRYPTED":str(mn(str(i["TEXT"])))
        })   

print("User profiles with their respective encoded values created which has their prefrences hidden in it",USER_PROFILE.find().count())



for i in business_profile_cursor:
    BUSINESS_PROFILE.insert_one({
            "USER_ID":i["BUSINESS_ID"],
            "ENCRYPTED":str(mn(str(i["TEXT"])))
        })   

print("business profiles with their respective encoded values created which has their features hidden in it",BUSINESS_PROFILE.find().count())

