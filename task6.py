def find(word, letter, index): 
  while index < len(word): 
    if word[index] == letter: 
      return index 
    index = index + 1 
  return -1


def counter(word, letter, index, count):
    newIndex = 0
    while (index!=-1):
        index = find (word, letter, newIndex)
        newIndex=index+1 # index is index at which letter is found, newIndex is index+1, so that next search loop starts from next index after found character
        count = count+1
    return count-1 #decrement by 1, because extra count addition happens once even if the letter is not found

word = "banana"
letter = "a"
print("total number of letter " +letter +" in " + word + " is " + str(counter("banana","a", 0, 0)))