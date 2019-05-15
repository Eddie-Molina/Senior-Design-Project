# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 00:14:09 2018

@author: Marco
"""
import Recipe
import sys
import Timer
import os
from os.path import dirname
from subprocess import call

class Webpage:

  def __init__(self,name):
    self.recipes = []
    self.time    = ''
    self.html    = '../src/brew.html'
    d = dirname(dirname(abs(__file__)))
    self.cgi_script = str(d) + '/src/'
    d = str(d) + '/src/BrewCrew.html'
    self.html    = d
    self.header  = '''<!DOCTYPE html>
                          <html>
                          <head>
                              <title>UTA Brew Crew</title>
                              <link rel="stylesheet" type="text/css" href="StyleBrew.css">
                          </head>
                          <body>
                          <h1 align="center">DOOM</h1>
                          <h6 align="center"> <i>(Drunk Object Oriented Machine)</i> </h1>
                          <center><img width ="500"src="beer_image.webp"></center>
                          <h3 align="center"><a href = "Beer_Recipes.html">Brew Crew Recipes</a></h3>
                          <table align="center" border ="1">
                                    <thead>
                                <tr>
                                    <th>Type</th>
                                    <th>Time</th>
                                    <th>Style</th>
                                </tr>
                            </thead>'''
    self.custom  = f'''<h3>Custom Recipes</h3>
                        <form action = "{self.cgi_script}new_recipe_cgi.py" method = "post">
                            <div>
                                <label for="Recipe Name">Recipe:</label>
                                <input name="Recipe" id="Recipe Name" type="text" placeholder="Enter recipe name here" required>
                            </div>
                            <div>
                                <label for="Type of Hops1">Hops 1:</label>
                                <input name="hop_name_1" id="Type of Hops1" type="text" placeholder="Enter Hops type here" required>
                                <label for="Type of Hops2">Hops 2:</label>
                                <input name="hop_name_2" id="Type of Hops2" type="text" placeholder="Enter 2nd Hops" required>
                                <label for="Type of Hops3">Hops 3:</label>
                                <input name="hop_name_3" id="Type of Hops3" type="text" placeholder="Enter 3rd Hops" required>
                                <label for="Type of Hops4">Hops 4:</label>
                                <input name="hop_name_4" id="Type of Hops4" type="text" placeholder="Enter 4th Hops" required>
                                <label for="Type of Hops5">Hops 5:</label>
                                <input name="hop_name_5" id="Type of Hops5" type="text" placeholder="Enter 5th Hops" required>
                                <label for="Type of Hops6">Hops 6:</label>
                                <input name="hop_name_6" id="Type of Hops6" type="text" placeholder="Enter 6th Hops" required>
                            </div>
                            <div>
                                <label for="Type of Time1">Time 1:</label>
                                <input name="hop_time_1" id="Type of Time1" type="text" placeholder="Enter Time in minutes" required>
                                <label for="Type of Time2">Time 2:</label>
                                <input name="hop_time_2" id="Type of Time2" type="text" placeholder="Enter 2nd Time" required>
                                <label for="Type of Time3">Time 3:</label>
                                <input name="hop_time_3" id="Type of Time3" type="text" placeholder="Enter 3rd Time" required>
                                <label for="Type of Time4">Time 4:</label>
                                <input name="hop_time_4" id="Type of Time4" type="text" placeholder="Enter 4th Time" required>
                                <label for="Type of Time5">Time 5:</label>
                                <input name="hop_time_5" id="Type of Time5" type="text" placeholder="Enter 5th Time" required>
                                <label for="Type of Time6">Time 6:</label>
                                <input name="hop_time_6" id="Type of Time6" type="text" placeholder="Enter 6th Time" required>
                            </div>
                            <div>
                                <p>Style Description:</p>
                                <textarea name="textdescription" rows="3" cols="30" placeholder="Enter general description like bitter,sour etc."></textarea>
                            </div>
                            <div>
                                <label for="Temperature">Temperature:</label>
                                <input name="temperature" id="Temperature" type="text" placeholder="Enter in celsius" required>
                            </div>
                            <div>
                                <input type = "submit" value = "Submit" />
                            </div>
                        </form>
                        </body>
                        </html>'''

    self.recipe_HTML = ''
    d = dirname(dirname(abs(__file__)))
    d = str(d) + '/src/Beer_Recipes.html'
    self.recipe_HTML = d

    self.recipe_HTML_Header = '''<!DOCTYPE html>
                                    <html>
                                    <head>
                                        <title>Recipes</title>
                                    </head>
                                    <body>
                                        <h1 align="center">Signature Recipes</h1>
                                    <table align="center" border ="1">
                                        <thead>
                                            <tr>
                                                <th>Beer</th>
                                                <th>Recipe</th>
                                            </tr>
                                        </thead>
                                        <tbody>'''
    self.recipe_HTML_Closing = '''</tbody>
                                    </table>
                                    </body>
                                    </html>'''

###END INIT


  def startBrewing(self, times, temperature):
      """
      times should be an array no larger than 5
      it contains the time in minutes which each set of hops will be brewed.
      the position in the array should dirrectly relate to the canister in which the hops
      for that time are held so
      times[0] = the time in minutes for the hops in canister 1
      time [1] = '                                           ' 2
      """
      if(len(times) > 6 or len(times) < 1):
          print("error, array of invalid size")
      command = "brew"
      counter = 1
      for item in times:
        command = command + "  -t " + str(counter) + "/" + str(item)
        counter = counter + 1

      os.system(command)
      return command

  def display_recipe(curRec):
    if curRec.active == False:
      pass
    else:
      return str(curRec.name)

#### HTML CREATION

  def create_recipe_list(self):
    if not(self.recipes):
      self.recipes = Recipe.parseRecipes()
    total_time = 0
    table = '<tbody>'
    for recipe in self.recipes:
      app = '<tr align="center">'
      app = app + '<td>' + recipe.name + '</td>'
      for time in recipe.times:
        total_time = total_time + time
      app = app + '<td>' + str(total_time) + ' minutes</td>'
      app = app + '<td>' + recipe.description + '</td></tr>'
      table = table + app
    table = table + '</tbody></table>'
    return table

  def create_recipe_buttons(self):
    if not(self.recipes):
      self.recipes = Recipe.parseRecipes()
    table = f'<form action = "{self.cgi_script}brew_cgi.py" method = "post" target = "_blank"><fieldset><legend>Choose your Beer style</legend>'
    for recipe in self.recipes:
      app = '<div>'
      app = app + '<input type="radio" id="' + recipe.name + '"name="Beer" value="' + recipe.name + '" checked />'
      app = app + '<label for="' + recipe.name + '">' + recipe.name + '</label></div>'
      table = table + app
    table = table + '<div><input type="button" class="btn" value = "Start Brewing"><input type="button" class="btn" value = "STOP"></div></fieldset></form>'
    return table

  def create_recipe_table(self):
    if not(self.recipes):
      self.recipes = Recipe.parseRecipes()
    table = ''
    hops = ''
    total_time = 0
    for recipe in self.recipes:
      for time in recipe.times:
        total_time = total_time + time
      for hop in recipe.hops:
        hops = hops + ' ' + hop
      table = table + '<tr><td>' + recipe.name + '</td><td><ul><li>Hops: ' + hops + '</li><li>Temperature: ' + recipe.temperature + ' C</li><li>Time: ' + str(total_time) + ' minutes</li><li>Description: ' + recipe.description + '</li></ul></td></tr>'
    return table

  def createHTML(self):
    if not(self.recipes):
      self.recipes = Recipe.parseRecipes()
    html_text = self.header + self.create_recipe_list() + self.create_recipe_buttons() + self.custom
    with open(self.html, 'w+') as fp:
      fp.write(html_text)
    return

  def recipeHTML(self):
    if not(self.recipes):
      self.recipes = Recipe.parseRecipes()
    html_text = self.recipe_HTML_Header + self.create_recipe_table() + self.recipe_HTML_Closing
    with open(self.recipe_HTML, 'w+') as fp:
      fp.write(html_text)
    return




###############################
def _main():
  fName = sys.argv [1]
  print('Testing Webpage class using '+fName)

if ( __name__ == '__main__' ) :
  _main()
