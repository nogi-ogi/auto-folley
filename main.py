import spacy
import pysrt
import nltk
import mix
import numpy as np

_SUBTITLE_PATH = 'subtitles/taxi_driver.srt'


def get_top_scores_and_timestamps (subtitle_path, e, n):
    nlp = spacy.load('en_core_web_md')
    subs = pysrt.open(subtitle_path, encoding='iso-8859-1')

    cues = []
    raw_scores = []

    target = nlp(u(e.phrase))

    for sub in subs:
        score = e.score(sub.text)
        raw_scores.append(score)
        cues.append(parse_cue(sub, e.wav))

    std_dev = np.std(raw_scores)
    mean = np.mean(raw_scores)

    raw_scores_and_cues = zip(raw_scores, cues)
    return map(lambda x: x[1], sorted(raw_scores_and_cues)[-5:])

cues = ()

class emotion:
    def __init__(self, wav, phrase):
        self.wav = wav
        self.phrase = phrase

    def score(self, query):
        return self.vec.similarity(nlp(query))

emotions = [#emotion("laugh.wav", u'happy', 0.72),
            emotion("awww.mp3", u'that\'s cute')]
emo_scores = {}
def parse_cue(sub, emo):
    hours = sub.end.hours * 3600000
    minutes = sub.end.minutes * 60000
    seconds = sub.end.seconds * 1000
    cue = (hours + minutes + seconds, emo)
    print("\t{} event: {}:{}:{}".format(emo, sub.end.hours,sub.end.minutes,sub.end.seconds))
    return cue

for emo in emotions:

    '''
    score = emo.score(sub.text)
    if emo.wav not in emo_scores:
        emo_scores[emo.wav] = []
    emo_scores[emo.wav].append(score)
    if score > emo.thresh:
        print(sub.text, score)
        cues.append(parse_cue(sub, emo.wav))
    '''
    top_picks = get_top_scores_and_timestamps(_SUBTITLE_PATH, emo, 5)
    for top_pick in top_picks:
        cues.append(top_pick, emo.wav)


#print(cues)
#ts, wav = cues[0]
video = "casablanca.mkv"

mix.add_wavs(cues, video)
