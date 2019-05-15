# -*- coding: utf-8 -*-
from Recipe import genRecipe
from Webpage import createHTML
import cgi, cgitb

#Enable logs for error checking
cgitb.enable(display=0, logdir="/data/logs")

#Main form to be used
form = cgi.FieldStorage()

hop_names = []
hop_times = []
recipe_name = form.getvalue('recipe_name')
temperature = form.getvalue('temperature')
description = ''

### Hop values

if form.getvalue('hop_name_1'):
  hop_names = hop_names.append(form.getvalue('hop_name_1'))
else:
  hop_names = hop_names.append("Not entered")

if form.getvalue('hop_name_2'):
  hop_names = hop_names.append(form.getvalue('hop_name_2'))
else:
  hop_names = hop_names.append("Not entered")

if form.getvalue('hop_name_3'):
  hop_names = hop_names.append(form.getvalue('hop_name_3'))
else:
  hop_names = hop_names.append("Not entered")

if form.getvalue('hop_name_4'):
  hop_names = hop_names.append(form.getvalue('hop_name_4'))
else:
  hop_names = hop_names.append("Not entered")

if form.getvalue('hop_name_5'):
  hop_names = hop_names.append(form.getvalue('hop_name_5'))
else:
  hop_names = hop_names.append("Not entered")

if form.getvalue('hop_name_5'):
  hop_names = hop_names.append(form.getvalue('hop_name_5'))
else:
  hop_names = hop_names.append("Not entered")

### Hop Times

if form.getvalue('hop_time_1') and int(form.getvalue('hop_time_1')):
  hop_times = hop_times.append(form.getvalue('hop_time_1'))
else:
  hop_times = hop_times.append('0')

if form.getvalue('hop_time_2') and int(form.getvalue('hop_time_2')):
  hop_times = hop_times.append(form.getvalue('hop_time_2'))
else:
  hop_times = hop_times.append('0')

if form.getvalue('hop_time_3') and int(form.getvalue('hop_time_3')):
  hop_times = hop_times.append(form.getvalue('hop_time_3'))
else:
  hop_times = hop_times.append('0')

if form.getvalue('hop_time_4') and int(form.getvalue('hop_time_4')):
  hop_times = hop_times.append(form.getvalue('hop_time_4'))
else:
  hop_times = hop_times.append('0')

if form.getvalue('hop_time_5') and int(form.getvalue('hop_time_5')):
  hop_times = hop_times.append(form.getvalue('hop_time_5'))
else:
  hop_times = hop_times.append('0')

if form.getvalue('textdescription'):
  description = form.getvalue('textdescription')
else:
  description = "Not entered"

###Generate Recipe file

genRecipe(recipe_name, hop_names, hop_times, description, temperature)

###Refresh page

print(createHTML())

