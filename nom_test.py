# -*- coding: utf-8 -*-

import spacy
import pysrt
import mix
import json
import numpy
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics import accuracy_score 
from sklearn.base import TransformerMixin 
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

import string
punctuations = string.punctuation

from spacy.en import English
parser = English()

#Custom transformer using spaCy 
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]
    def fit(self, X, y=None, **fit_params):
        return self
    def get_params(self, deep=True):
        return {}

# Basic utility function to clean the text 
def clean_text(text):     
    return text.strip().lower()


nlp = spacy.load('en_core_web_md')
subs = pysrt.open('subtitles/haine.srt', encoding='iso-8859-1')
subs2 = pysrt.open('subtitles/taxi_driver.srt')

len(subs)
len(subs2)

train = []
test = []

for sub in subs2:
    train.append(sub.text)

for sub in subs:
#    if "porno" in sub.text or "organezized" in sub.text:

    test.append(sub.text)
    #score = target.similarity(nlp(sub.text))
    #print(sub.text, score)
    #rawScores.append(score)
    #if score > 0.689: 
       # print(sub.text, score)
    #    cues.append(parse_cue(sub))


#Create spacy tokenizer that parses a sentence and generates tokens
#these can also be replaced by word vectors 
def spacy_tokenizer(sentence):
    tokens = parser(sentence)
    tokens = [tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_ for tok in tokens]
    tokens = [tok for tok in tokens if (tok not in stopwords and tok not in punctuations)]
    return tokens

#create vectorizer object to generate feature vectors, we will use custom spacy’s tokenizer
vectorizer = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1)) 
classifier = LinearSVC()

pipe = Pipeline([("cleaner", predictors()),
                 ('vectorizer', vectorizer),
                 ('classifier', classifier)])



# Create model and measure accuracy
pipe.fit([x[0] for x in train], [x[1] for x in train]) 
pred_data = pipe.predict([x[0] for x in test]) 
for (sample, pred) in zip(test, pred_data):
    print (sample, pred) 
print ("Accuracy:", accuracy_score([x[1] for x in test], pred_data))

#first_sub = subs[0]

#print first_sub.text;
#print str(first_sub.start.minutes) + " minutes and " + str(first_sub.start.seconds);
#print str(first_sub.end.minutes) + " minutes and " + str(first_sub.end.seconds);

#print subs.slice(starts_after={'minutes': 2, 'seconds': 30}, ends_before={'minutes': 2, 'seconds': 40}).text;

#cues = []
#rawTings = []
#rawScores = []

#target = nlp(u'happy')

# def parse_cue(sub):
#     hours = sub.end.hours * 3600000
#     minutes = sub.end.minutes * 60000
#     seconds = sub.end.seconds * 1000
#     cue = (hours + minutes + seconds, "laugh.wav")
#     print("event: {}:{}:{}".format(sub.end.hours,sub.end.minutes,sub.end.seconds))
#     return cue


#print(rawScores)
#print(cues)
#ts, wav = cues[0]
#video = "taxi_driver.mkv"

# with open('raw_input_happy.txt', 'w') as outfile:
#     json.dump(rawScores, outfile)

# std_dev = numpy.std(rawScores)
# mean = numpy.mean(rawScores)

# top_five = []
# _TOP_SCORES = 5

# for score in rawScores:
#     if score > std_dev + mean:
#         if len(top_five) < _TOP_SCORES:
#              top_five.append(cues)
#         else:
#             if score > top_five[0]:
#                 top_five[0] = score
#         top_five.sort()

# print top_five

#mix.add_wavs(cues, video)
