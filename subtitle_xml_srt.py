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

for div_tag in soup.findAll('div'):
	for p_tag in div_tag.findAll('p'):
		
		srt += str(int(p_tag.get('id')[1:])+1) + '\n'
		srt += "%s --> %s\n" % (parse_time(p_tag.get('begin')), parse_time(p_tag.get('end')))

		for span_tag in p_tag.findAll('span'):
			span_sentence = span_tag.text
			srt += "<i>" + span_sentence + "</i>"
			has_span = True

		pt = p_tag.text

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