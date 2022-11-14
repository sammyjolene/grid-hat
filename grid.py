#s = ['.xxxx.', 'xxxxxx', 'xxx...', '.xxxx.', '...xxx', '....xx', 'xxxxxx', '.xxxx.']
#a = ['.xxxx.', 'xxxxxx', 'xx..xx', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx']
#m = ['x....x', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx', 'xx..xx', 'xx..xx']
alphabet = {'s': ['.xxxx.', 'xxxxxx', 'xxx...', '.xxxx.', '...xxx', '....xx', 'xxxxxx', '.xxxx.'], 'a': ['.xxxx.', 'xxxxxx', 'xx..xx', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx'], 'm': ['x....x', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx', 'xx..xx', 'xx..xx']}
#print(alphabet['s'][0])
#function takes in the word sam, breaks it down by letter and then prints the same grid. 
def input_word(word):
  word_letters = [x for x in word]
  #makes the word into a list of letters
  letter_dict = {}
  count = 1
  #splits the word that has been input into a dictionary where the letters of the word are the value of 
  # the keys that keep count, this essentially creates a way for me to call upon the letters without creating empty variables
  while len(word_letters) > 0:
    letter_dict[count] = word_letters[0]
    count += 1
    word_letters.pop(0)
  #print(letter_dict)
  #this is a way to reference the dictionary stored from the dictionary created and prints the letters one 
  # after another. so right now it prints s, then a, then m if i input sam
  dict_count = 1
  #while len(letter_dict)>0:
   # print(*(alphabet[letter_dict[dict_count]]), sep = "\n")
   # letter_dict.pop(dict_count)
   # dict_count +=1
  grid = []
  row = []
  idx = 0

#Need to insert loop that goes through each value list for the length so that there are multiple rows
  for temp in range(8):
    for items in letter_dict:
      row.append(alphabet[letter_dict[dict_count]][idx])
      dict_count += 1

    grid.append(str(row))
    dict_count = 1
    idx += 1
    row.clear()
  
  print(*grid, sep="\n")  


#Next step is how to unpack a nested list to print without brackets

input_word("sam")
#to print in new lines:   *s_row, sep = "\n"
