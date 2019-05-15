# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:21:06 2018

@author: Marco
"""
import sys
import os
from os.path import dirname
import glob
class Recipe:
  """
  This class will be used as an instance for a specific recipe.

      Data
      name        = string
      hops        = list of strings
      times       = list of strings
      description = string
      temperature = string
      active      = boolean

      Functions
      parseRecipe()
      genRecipe()
      __init__()

  """

  def __init__(self, name = '', hops = [], times = [], description = '', temperature = ''):
    self.active      = False
    self.name        = name
    self.hops        = hops
    self.times       = times
    self.description = description
    self.temperature = temperature

    ###############################
    # Recipe Parsing will go here #
    ###############################

  def parseRecipe(self,File):
    """
        Name
            parseRecipe

        Input
            Recipe File

        Output
            Recipe Instance

        Function
            This function will take a .rec file as input. It will parse the file line by line while removing whitespace
            and terminating characters. It will match the correct values with its equivalent recipe class variables.
            Then return its equivalent recipe instance.
    """
    try:
      with open( File, 'r' ) as fp :
        lines = fp.read().replace('\r', '' ).split( '\n' )
        name  = lines[0].replace('_', ' ')
        hops  = lines[1].split(';')
        times = lines[2].split(' ')
        description = lines[3]
        temperature = lines[4]
    except:
      raise ValueError('Incorrect Recipe format')

    output = Recipe(name, hops, times, description, temperature)
    return output

    def parseRecipes(self):
    """
        Name
            parseRecipes

        Output
            List of Recipe Instances

        Function
            It will parse the file line by line while removing whitespace
            and terminating characters. It will match the correct values with its equivalent recipe class variables.
            Then return its equivalent recipe instance.
    """
    try:
      File = dirname(dirname(abs(__file__)))
      File = str(File) + '/data/recipe/*.rec'
      files = glob.glob(File)
      recipes = []
      for item in files:
        with open( item, 'r' ) as fp :
          lines = fp.read().replace('\r', '' ).split( '\n' )
          name  = lines[0].replace('_', ' ')
          hops  = lines[1].split(';')
          times = lines[2].split(' ')
          description = lines[3]
          temperature = lines[4]
        recipes.append(Recipe(name, hops, times, description, temperature))
    except:
      raise ValueError('Incorrect Recipe format')

    return recipes


  def genRecipe(self, recipe_name, hop_names, hop_times, description, temperature):
    """
        Name
            genRecipe

        Input
            Recipe Instance referenced by Name

        Output
            Recipe File to the ../recipe/ file directory

        Function
            This function will create a .rec file as its output.
            It will take the recipe class and turn each value into a line of text.
            List values will be seperated by a space while different variables are seperated by newline characters.
    """
    try:
      File = dirname(dirname(abs(__file__)))
      File = str(File) + '/data/recipe/'
      recipe_name = recipe_name.replace(' ', '_')
      File = File + str(recipe_name) +'.rec'
      File = open(File,'w')
      File.write(recipe_name + '\n')
      for item in hop_names:
        File.write(str(item)+';')
      File.write('\n')
      for item in hop_times:
        File.write(str(item)+' ')
      File.write('\n')
      File.write(description)
      File.write('\n')
      File.write(temperature)
      File.write('\n')
    except:
        print("error in creating .rec file")

    return

#################################
def _main():
  help(Recipe)
  fName = sys.argv [1]
  print('Testing Recipe class using'+fName)


if ( __name__ == '__main__' ) :
  _main()