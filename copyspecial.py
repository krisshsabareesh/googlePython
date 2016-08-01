#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def copytodir(tdir, dirs):
  (status, output) = commands.getstatusoutput('ls ' + tdir)
  if status :
    print 'Creating New Folder-------, Copying---'
    os.mkdir(tdir)
  else:
    print 'Folder exists, now copying-----'

  for dir in dirs:
    files = os.listdir(dir)
    for file in files:
      if (re.search(r'__\w+__',file)):
        shutil.copy(file, tdir)
        print "ok"
      else:
        print 'Not a special file ---- Skipping'
  
def makezip(zdir, dirs):
  copytodir(zdir[:-4],dirs)
  shutil.make_archive(zdir[:-4],'zip',zdir[:-4])
  shutil.rmtree(zdir[:-4])

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  if len(args) == 1:
    filenames = os.listdir(args[0])
    for file in filenames:
      print file

  # +++your code here+++
  # Call your functions

  for arg in args:
    if len(todir) > 0:
      copytodir(todir, args)
    if len(tozip) > 0:
      makezip(tozip, args)

      
  
if __name__ == "__main__":
  main()
