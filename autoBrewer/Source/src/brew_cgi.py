# -*- coding: utf-8 -*-
from Recipe import parseRecipe
from Webpage import startBrewing
import cgi, cgitb
"""
<form action = "/src/main.py" method = "post" target = "_blank">
<input type = "radio" name = "subject" value = "OG DOOM" /> OG DOOM
<input type = "radio" name = "subject" value = "The Van Diesel" /> The Van Diesel
<input type = "submit" value = "Select Beer" />
</form>
"""
#Enable logs for error checking
cgitb.enable(display=0, logdir="/data/logs")

#Main form to be used
form = cgi.FieldStorage()

if form.getvalue('Beer'):
  subject = form.getvalue('subject')
  try:
    file = subject.replace(' ', '_') + '.rec'
    recipe = parseRecipe(file)
    times = []
    for time in recipe.times:
      if time is not 0:
        times.append(time)
    startBrewing(times, recipe.temperature)

  except:
    raise ValueError('Recipe does not exist')

else:
   subject = "Not set"