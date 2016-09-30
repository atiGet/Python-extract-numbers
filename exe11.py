#write a python program that extracts all the numbers from a file and prints the list of numbers and their sum 
import re
fName=raw_input("Please enter file name:")
hand=open(fName)
count=0
sum=0
for line in hand:
	line=line.rstrip()
	y=re.findall('[0-9]+',line)
	if len(y)==0:continue
	print y
	count=count+len(y)
	for x in y:
		sum=sum+int(x)
print "There are ",count,"values with the sum=",sum