#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import Webpage
import cgi, cgitb
import os

#Enable logs for error checking
cgitb.enable(display=0, logdir="/data/logs")

#Main form to be used
form = cgi.FieldStorage()

#Recipe Get html
"""
<form action = "/src/main.py" method = "post">

Recipe: <input type = "text" name = "recipe_name">  <br />
Hop1: <input type = "text" name = "hop_name_1">
Hop2: <input type = "text" name = "hop_name_2">
Hop3: <input type = "text" name = "hop_name_3">
Hop4: <input type = "text" name = "hop_name_4">
Hop5: <input type = "text" name = "hop_name_5">  <br />
Time1: <input type = "text" name = "hop_time_1">
Time1: <input type = "text" name = "hop_time_2">
Time1: <input type = "text" name = "hop_time_3">
Time1: <input type = "text" name = "hop_time_4">
Time1: <input type = "text" name = "hop_time_5"> <br />
Temperature: <input type = "text" name = "temperature"> <br />
<textarea name = "textdescription" cols = "40" rows = "4">
Type description here...
</textarea>
<input type = "submit" value = "Submit" />
</form>
"""
hop_names = []
hop_times = []
recipe_name = form.getvalue('recipe_name')
hop_names = hop_names.append(form.getvalue('hop_name_1'))
hop_names = hop_names.append(form.getvalue('hop_name_2'))
hop_names = hop_names.append(form.getvalue('hop_name_3'))
hop_names = hop_names.append(form.getvalue('hop_name_4'))
hop_names = hop_names.append(form.getvalue('hop_name_5'))
hop_times = hop_times.append(form.getvalue('hop_time_1'))
hop_times = hop_times.append(form.getvalue('hop_time_2'))
hop_times = hop_times.append(form.getvalue('hop_time_3'))
hop_times = hop_times.append(form.getvalue('hop_time_4'))
hop_times = hop_times.append(form.getvalue('hop_time_5'))
temperature = form.getvalue('temperature')


#Recipe choose HTML
"""
<form action = "/src/main.py" method = "post" target = "_blank">
<input type = "radio" name = "subject" value = "OG DOOM" /> OG DOOM
<input type = "radio" name = "subject" value = "The Van Diesel" /> The Van Diesel
<input type = "submit" value = "Select Beer" />
</form>
"""
if form.getvalue('subject'):
   subject = form.getvalue('subject')
else:
   subject = "Not set"

#Recipe Description HTML
"""
<form action = "/src/main.py" method = "post" target = "_blank">
<textarea name = "textdescription" cols = "40" rows = "4">
Type description here...
</textarea>
<input type = "submit" value = "Submit" />
</form>
"""

if form.getvalue('textdescription'):
   text_content = form.getvalue('textdescription')
else:
   text_content = "Not entered"


#File Upload HTML
"""
<html>
<body>
   <form enctype = "multipart/form-data"
                     action = "/src/main.py" method = "post">
   <p>File: <input type = "file" name = "filename" /></p>
   <p><input type = "submit" value = "Upload" /></p>
   </form>
</body>
</html>
"""
recipe_file = form['filename']
# Test if the file was uploaded
if recipe_file.filename:
   #Strip leading path for security
   fn = os.path.basename(recipe_file.filename.replace("\\", "/" ))
   open('/tmp/' + fn, 'wb').write(recipe_file.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'