import spacy
import pysrt
import nltk
import mix
import numpy as np

nlp = spacy.load('en_core_web_md')
subs = pysrt.open('subtitles/casablanca.srt', encoding='iso-8859-1')

len(subs)

#first_sub = subs[0]

#print first_sub.text;
#print str(first_sub.start.minutes) + " minutes and " + str(first_sub.start.seconds);
#print str(first_sub.end.minutes) + " minutes and " + str(first_sub.end.seconds);

#print subs.slice(starts_after={'minutes': 2, 'seconds': 30}, ends_before={'minutes': 2, 'seconds': 40}).text;

cues = []

class emotion:
    def __init__(self, wav, phrase, thresh):
        self.wav = wav
        self.phrase = phrase
        self.vec = nlp(phrase)
        self.thresh = thresh

    def score(self, query):
        return self.vec.similarity(nlp(query))

emotions = [#emotion("laugh.wav", u'happy', 0.72),
            emotion("awww.mp3", u'that\'s cute', 0.78),]
emo_scores = {}
def parse_cue(sub, emo):
    hours = sub.end.hours * 3600000
    minutes = sub.end.minutes * 60000
    seconds = sub.end.seconds * 1000
    cue = (hours + minutes + seconds, emo)
    print("\t{} event: {}:{}:{}".format(emo, sub.end.hours,sub.end.minutes,sub.end.seconds))
    return cue

for sub in subs:
    if not "kid" in sub.text and not "friendship" in sub.text:
        continue

    n = nlp(sub.text) 

    for emo in emotions:
        score = emo.score(sub.text)
        if emo.wav not in emo_scores:
            emo_scores[emo.wav] = []
        emo_scores[emo.wav].append(score)
        if score > emo.thresh:
            print(sub.text, score)
            cues.append(parse_cue(sub, emo.wav))

#print(cues)
#ts, wav = cues[0]
video = "casablanca.mkv"

mix.add_wavs(cues, video)
