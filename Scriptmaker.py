# A way to create an easy-to-read script from downloaded YouTube subtitles.
import re
start = open('caption_input.srt', 'r+')
lines = start.readlines()
end = open('videoscript.txt', 'w+')
lines2 = end.readlines()
for line in lines:
  ''' Code below removes lines with colons and line less than 4 characters long
      then removes newlines to create the end document. '''
  if not re.search(':\S', line) and len(line) > 4:
    end.write(line.replace('\n', ' '))
    
start.close()
end.close()
