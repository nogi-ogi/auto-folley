import spacy
import pysrt
import nltk
import mix
import json
import numpy

nlp = spacy.load('en_core_web_md')
subs = pysrt.open('subtitles/haine.srt', encoding='iso-8859-1')

len(subs)

#first_sub = subs[0]

#print first_sub.text;
#print str(first_sub.start.minutes) + " minutes and " + str(first_sub.start.seconds);
#print str(first_sub.end.minutes) + " minutes and " + str(first_sub.end.seconds);

#print subs.slice(starts_after={'minutes': 2, 'seconds': 30}, ends_before={'minutes': 2, 'seconds': 40}).text;

cues = []
rawTings = []
rawScores = []

target = nlp(u'annoy')

def parse_cue(sub):
    hours = sub.end.hours * 3600000
    minutes = sub.end.minutes * 60000
    seconds = sub.end.seconds * 1000
    cue = (hours + minutes + seconds, "laugh.wav")
    print("event: {}:{}:{}".format(sub.end.hours,sub.end.minutes,sub.end.seconds))
    return cue

for sub in subs:
#    if "porno" in sub.text or "organezized" in sub.text:

    rawTings.append(sub.text)
    score = target.similarity(nlp(sub.text))
    #print(sub.text, score)
    rawScores.append(score)
    if score > 0.5: 
        print(sub.text, score)
    #    cues.append(parse_cue(sub))

#print(rawScores)
#print(cues)
#ts, wav = cues[0]
#video = "taxi_driver.mkv"

with open('raw_input_happy.txt', 'w') as outfile:
    json.dump(rawScores, outfile)

std_dev = numpy.std(rawScores)
mean = numpy.mean(rawScores)

top_five = []
_TOP_SCORES = 5

for score in rawScores:
    if score > std_dev + mean:
        if len(top_five) < _TOP_SCORES:
             top_five.append(cues)
        else:
            if score > top_five[0]:
                top_five[0] = score
        top_five.sort()

print top_five

#mix.add_wavs(cues, video)
