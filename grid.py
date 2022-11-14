s = ['.xxxx.', 'xxxxxx', 'xxx...', '.xxxx.', '...xxx', '....xx', 'xxxxxx', '.xxxx.']
a = ['.xxxx.', 'xxxxxx', 'xx..xx', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx']
m = ['x....x', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx', 'xx..xx', 'xx..xx']

def input_letters(letter1, letter2, letter3):
  letters = []
  row = len(letter1)-1
#this will give us the number or rows or items we need to hit. so for this example the 
# list has three elements so the length is 3, we subtract one to zero index 
  index = 0
#since we are starting at the back of the list we will need to be able to insert each 
# # following loop into the zero index position
  while row >= 0:
    letters.insert(index, str(letter1[row]) + "  " + str(letter2[row]) + '  ' + str(letter3[row]))
    row = row - 1
#This loop works until the condition is not met. We will hit the last item on the list first then 
# subtract one from the row value moving it up an index towards the beginning of the list followed 
# by the second to last and so forth until we hit the 0 index
  print(*letters, sep = "\n")

input_letters(s, m, s)