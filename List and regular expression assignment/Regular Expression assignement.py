#REGULAR EXPRESSIONS 

#Question 1
import re
ipaddr = "216.08.094.196"
res = re.sub('0', '', ipaddr)
print(res)

#Question 2
txt = 'I have a tab'
res=re.findall(".*a.*b",txt)
print(res)

#Question 3
string = 'They ate 6 apples and 10 bananas'
string = re.sub('6', 'six', string)
string = re.sub('10', 'ten', string)
print (string)