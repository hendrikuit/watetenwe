import requests
from bs4 import BeautifulSoup

def scrape_recipe(url):
  # Haal de HTML van de opgegeven url op
  response = requests.get(url)

  # Maak een BeautifulSoup object van de HTML
  soup = BeautifulSoup(response.text, 'html.parser')

  # Zoek het recept op op basis van de structuur volgens schema.org
  recipe = soup.find('div', {'itemtype': 'http://schema.org/Recipe'})

  # Maak een lege dictionary waar we het recept in kunnen opslaan
  recipe_data = {}

  # Zoek de naam van het recept op en sla deze op in de dictionary
  recipe_data['name'] = recipe.find('h1', {'itemprop': 'name'}).text

  # Zoek de lijst met ingredienten op en sla deze op in de dictionary
  recipe_data['ingredients'] = [
    ingredient.text
    for ingredient in recipe.find_all('span', {'itemprop': 'ingredient_name'})
  ]

  # Zoek de lijst met instructies op en sla deze op in de dictionary
  recipe_data['instructions'] = [
    instruction.text
    for instruction in recipe.find_all('p', {'itemprop': 'recipeInstructions'})
  ]

  # Geef de dictionary met receptgegevens terug
  return recipe_data
