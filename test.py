import re

s = "unoDosTres"
print(re.sub(r"([A-Z][a-z])", r" \1", s).split())
