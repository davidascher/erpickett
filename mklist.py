# mklist.py

for line in open('list').readlines():
  img = line.strip()
  print '<li><a href="images/full/' + img + '"><img src="images/thumb/' + img + '" alt="' + img + '" /></a></li>'
