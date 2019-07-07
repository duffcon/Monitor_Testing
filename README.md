# regex

```py
import re
```
```
match   found at beginning of string
search  scan for location
findall     find all substrings, return list
finditer    find all substrings, return iterator
```

find instance of pattern
```py
import re

mystring = '''
1 fish
red fish
2 fish
blue fish
'''

match = re.search("\d fish", mystring)
print(match.group())
```

```
python file.py
```

->
```
1 fish
```

split pattern into groups, extract specific data
```py
import re

mystring = '''
1 fish
2 fish
red fish
blue fish
'''

match = re.search("(\d) fish", mystring)
print(match.group(1))
```

->
```
1
```


2 group example
```py
import re

mystring = '''
1 fish red fish
'''

match = re.search("(\d) fish (\w+) fish", mystring)
print(match.group(1), match.group(2))
```

->
```
1 red
```

last instance example
```py
import re

mystring = '''
1 fish
red fish
blue fish
2 fish
'''

match = re.search("(?s:.*)(\d) fish", mystring)
print(match.group(1))
```

->
```
2
```