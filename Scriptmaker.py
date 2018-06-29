thing = open('caption_input.srt', 'r+')
lines = thing.readlines()
thing2 = open('videoscript.txt', 'w+')
lines2 = thing2.readlines()
for line in lines:
  
  if not ':' in line and len(line) > 4:
    thing2.write(line.replace('\n', ' '))
    
thing.close()
thing2.close()