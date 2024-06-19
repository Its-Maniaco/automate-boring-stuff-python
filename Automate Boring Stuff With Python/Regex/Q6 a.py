import re

# From the list keep only the lines that start with a number or a letter after > sign.


# Create regex for start
matchObject = re.compile(r'''
\>(\d+|\w+) #start with digit or alphabet after '>'


''', re.VERBOSE)

# find needed text
Text = matchObject.findall(''' 
>Slovenia
>Belgium
>Spain
>Kazakhstan
>[15]
>1964
>1968
>1972
>1992
>1996
>2000''')

print(Text)