#!/usr/bin/python

import json, urllib

# flast list of categories
flat = []

# pull the tree
url = "https://api.foursquare.com/v2/venues/categories?oauth_token=V31SXZ1SGEI1DHAFRYS1SXEINBN5S21CQBTJF5H3M04RH3Q4&v=20131016"
response = urllib.urlopen(url);
data = json.loads(response.read())

# interator for subcategories
def walk(data):
  for subcategory in data:
    flat.append({'category_id': subcategory['id'], 'title': subcategory['name']})
    if subcategory['categories']:
      walk(subcategory['categories'])

# start at the top level
for category in data['response']['categories']:
  flat.append({'category_id': category['id'], 'title': category['name']})
  if category['categories']:
    walk(category['categories'])

with open("index.js", "w") as f:
  f.write("'use strict';\n\nexports.categories = ");
  f.write(json.dumps(flat).replace("}, ", "},\n\t"));
  f.write(";")
