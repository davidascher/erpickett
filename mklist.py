# mklist.py

for line in open('list').split():
  img = line.strip()
  print '"<li><a href="images/full/' + img + '"><img src="images/thumb/' + img + '" alt="' + img + '" /></a></li>'