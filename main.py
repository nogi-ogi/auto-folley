import pysrt

subs = pysrt.open('subtitles/taxi_driver.srt')

len(subs)

first_sub = subs[0]

print "hello"
print first_sub.text;
print str(first_sub.start.minutes) + " minutes and " + str(first_sub.start.seconds);
print str(first_sub.end.minutes) + " minutes and " + str(first_sub.end.seconds);

print subs.slice(starts_after={'minutes': 2, 'seconds': 30}, ends_before={'minutes': 2, 'seconds': 40}).text;

