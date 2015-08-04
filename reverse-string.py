seq=raw_input("Enter a string:\n")
x=-1
reverse=''
for i in seq:
   reverse+=seq[x]
   x-=1
print "The reverse string of %s >>>>is>>>> %s" %(seq,reverse)
