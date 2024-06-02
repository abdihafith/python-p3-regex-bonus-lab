import re

my_pattern = r"[A-Z][a-z]*'*[a-z]\s[a-z' ]*today'*[ a-z, ]*[?\.]+"
#my_pattern = r"(?:It's such a lovely day today\.|Some weather we're having today, huh?|Maybe today's just not my day\.)"
my_regex = re.compile(my_pattern)
