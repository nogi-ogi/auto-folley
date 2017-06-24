import pysrt

subs = pysrt.open('subtitles/taxi_driver.srt')

len(subs)

first_sub = subs[0]

print "hello"
print first_sub.text;
print first_sub.start.seconds;
print first_sub.end.seconds;