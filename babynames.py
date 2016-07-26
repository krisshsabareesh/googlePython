#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""




def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  matchlist = {}
  count_dict = {} 
  x = 1
  f = open(filename, "r")
  for line in f:
    """match = re.search(r'(</td><td>)(\w+)(</td>)', line)"""
    #### matchlist.append(re.findall(r'(</td><td>)(\w+)(</td>)', line))  
    if re.findall(r'(</td><td>)(\w+)(</td>)', line):
      matchlist[x] = (re.findall(r'(</td><td>)(\w+)', line))
      x += 1
      #print re.findall(r'(</td><td>)(\w+)+', line)
  count_dict = count(matchlist)
  return count_dict

def count(matchlist):
  dict = {}
  x = 1
  for  tuple in matchlist.values():
    dict[tuple[0][1]] = x
    if len(tuple[0]) > 2:
         dict[tuple[0][3]] = x
    x +=1
  return dict


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for i in range(len(args)):
    if summary == True:
      sfile = open(args[i]+'.summary',"w")
      sorted_dict = extract_names(args[i])
      for item in sorted_dict.items():
        sfile.write(item[0] +' '+ str(item[1]) + '\n')

    else:
      sorted_dict = extract_names(args[i])
      for item in sorted_dict.items():
        print item[0], ' ', item[1]

if __name__ == '__main__':
  main()
