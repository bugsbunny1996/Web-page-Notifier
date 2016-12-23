import urllib2
import re

html_content = urllib2.urlopen('https://www.facebook.com/siddarth.1996').read()

matches = re.findall('hey', html_content);

if len(matches) == 0: 
   print 'I did not find anything'
else:
   print 'Yep'
