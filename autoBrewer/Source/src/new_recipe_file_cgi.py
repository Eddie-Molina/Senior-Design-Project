# -*- coding: utf-8 -*-
import Webpage
import cgi, cgitb
import os
from os.path import dirname
#Enable logs for error checking
cgitb.enable(display=0, logdir="/data/logs")

#Main form to be used
form = cgi.FieldStorage()


recipe_file = form['filename']
# Test if the file was uploaded
if recipe_file.filename:
  #Strip leading path for security
  fn = os.path.basename(recipe_file.filename.replace("\\", "/" ))
  d = dirname(dirname(abs(__file__)))
  d = str(d) + '/data/recipe/' + fn
  open(d, 'wb').write(recipe_file.file.read())

  message = 'The file "' + fn + '" was uploaded successfully'

else:
  message = 'No file was uploaded'

print(message)