import re, sys
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Need file name!")
    sys.exit(2)

f = open(sys.argv[1])
s = f.read()
f.close()

s = s.replace('<br />', '\n')
soup = BeautifulSoup(s)

parse_time = lambda time: time[:-3] + "," + time[-2:] + "0"
srt = ''
span_sentence = None
has_span = False
latter = None

for d in soup.findAll('div'):
	for pro in d.findAll('p'):
		
		srt += str(int(pro.get('id')[1:])+1) + '\n'
		srt += "%s --> %s\n" % (parse_time(pro.get('begin')), parse_time(pro.get('end')))

		for s in pro.findAll('span'):
			span_sentence = s.text
			srt += "<i>" + span_sentence + "</i>"
			has_span = True

		pt = pro.text

		if has_span is True:
			latter = pt.replace(span_sentence, '')
			srt += latter
			has_span = False
		else:
			latter = pt
			srt += latter

		srt += '\n\n'

f = open(sys.argv[1][:-4] + ".srt", 'w')
f.write(srt)
f.close()