#s = ['.xxxx.', 'xxxxxx', 'xxx...', '.xxxx.', '...xxx', '....xx', 'xxxxxx', '.xxxx.']
#a = ['.xxxx.', 'xxxxxx', 'xx..xx', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx']
#m = ['x....x', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx', 'xx..xx', 'xx..xx']
alphabet = {'s': ['.xxxx.', 'xxxxxx', 'xxx...', '.xxxx.', '...xxx', '....xx', 'xxxxxx', '.xxxx.'], 'a': ['.xxxx.', 'xxxxxx', 'xx..xx', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx'], 'm': ['x....x', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx', 'xx..xx', 'xx..xx']}

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
  while len(letter_dict)>0:
    print(len(letter_dict))
    print(*(alphabet[letter_dict[dict_count]]), sep = "\n")
    letter_dict.pop(dict_count)
    dict_count +=1
  

#THIS is where I stopped. I'm at the same place at the beginning print of SAM except that now comes from input. 
# next step is to figure out how to make them print left to right. Each is currently printing the reference 
# string from the dictionary alphabet. I might be able to reference the string by index for each key on a loop. 

input_word("sam")
#to print in new lines:   *s_row, sep = "\n"

#How do I turn the dictionary value of 's' into my variable of s which stores the rows for creating that letter. - my solution was to use two dictionaries where one's value references the others key and that value is the string I want to print
