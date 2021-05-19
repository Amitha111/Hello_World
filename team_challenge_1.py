import string

from string import Template

a = Template('$pronoun is the $noun given to $verb on for today ')
b = a.substitute(pronoun = 'This', noun = 'Team Challenge', verb = 'work')
print(b)