import re 

#Return a list containing every evety occurrence of "ai":

txt =  "The rain in Spain"
x = re.findall("ai", txt)
print(x)

