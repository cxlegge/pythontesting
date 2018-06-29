# A way to create an easy-to-read script from downloaded YouTube subtitles.
thing = open('caption_input.srt', 'r+')
lines = thing.readlines()
thing2 = open('videoscript.txt', 'w+')
lines2 = thing2.readlines()
for line in lines:
  # Code below removes lines with colons and line less than 4 characters long, then removes newlines to create the end document.
  if not ':' in line and len(line) > 4:
    thing2.write(line.replace('\n', ' '))
    
thing.close()
thing2.close()
