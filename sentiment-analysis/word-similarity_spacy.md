

```python
# Download spacy & model
#conda install spacy
#python -m spacy download en
```


```python
import spacy
import numpy as np

nlp = spacy.load('en')
```

The default English model installs vectors for one million vocabulary entries, using the 300-dimensional vectors trained on the Common Crawl corpus using the GloVe algorithm. The GloVe common crawl vectors have become a de facto standard for practical NLP.


```python
emotion = nlp(u'happy')
word = nlp(u'smile')

word.similarity(emotion)
```




    0.59745814413524079




```python
emotions = ['happy', 'sad']
emotions = [nlp(e) for e in emotions]

doc = "sunshine sun shine murder murders"
doc = nlp(doc)

# Which emotion
for word in doc:
    scores = [e.similarity(word) for e in emotions]
    idx = np.argmax(scores)
    
    res_score = scores[idx]
    res_emotion = emotions[idx]
    if res_score==0:
        print("Unknown -", word)
    else:
        print(res_emotion, "-", res_score, word)
```

    Unknown - sunshine
    happy - 0.325382734323 sun
    happy - 0.299066882966 shine
    sad - 0.329860494824 murder
    sad - 0.247688632473 murders

