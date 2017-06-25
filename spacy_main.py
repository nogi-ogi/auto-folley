from __future__ import unicode_literals
from spacy.en import English

parser = English()

multiSentence = "So, what do you want to hack for, Bickle." \
                "I can't sleep nights." \

parsedData = parser(multiSentence)

# Let's look at the sentences
sents = []
# the "sents" property returns spans
# spans have indices into the original string
# where each index value represents a token
for span in parsedData.sents:
    # go from the start to the end of each span, returning each token in the sentence
    # combine each token using join()
    sent = ''.join(parsedData[i].string for i in range(span.start, span.end)).strip()
    sents.append(sent)

for sentence in sents:
    print(sentence)

for span in parsedData.sents:
    sent = [parsedData[i] for i in range(span.start, span.end)]
    break

for token in sent:
    print(token.orth_, token.pos_)