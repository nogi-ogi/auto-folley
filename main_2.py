import spacy
import pysrt
import nltk
import mix
import json
import numpy
'''
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
    return cue

for sub in subs:
#    if "porno" in sub.text or "organezized" in sub.text:

    rawTings.append(sub.text)
    score = target.similarity(nlp(sub.text))
    #print(sub.text, score)
    rawScores.append(score)
    #cues.append(parse_cue(sub))
    #if score > 0.5:
    #    print(sub.text, score)

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

rawScores_cues = zip(rawScores, rawTings)
sorted_top_pick = sorted(rawScores_cues)[-5:]


#print top_five

#mix.add_wavs(cues, video)
'''
def get_top_scores_and_timestamps (subtitle_path, target, n):
    nlp = spacy.load('en_core_web_md')
    subs = pysrt.open(subtitle_path, encoding='iso-8859-1')

    cues = []
    raw_scores = []

    target = nlp(u(target))

    for sub in subs:
        score = target.similarity(nlp(sub.text))
        raw_scores.append(score)
        cues.append(parse_cue(sub))

    std_dev = numpy.std(raw_scores)
    mean = numpy.mean(raw_scores)

    raw_scores_and_cues = zip(raw_scores, cues)
    return sorted(raw_scores_and_cues)[-5:] 
