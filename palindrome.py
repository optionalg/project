seq=raw_input("Enter a word please")
if seq==seq[::-1]:
   print "yes, %s is a palindrome word" %(seq)
else:
   print "sorry, '%s' 'isn\'t a palindrome word" %(seq)
