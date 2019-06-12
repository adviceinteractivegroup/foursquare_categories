#!/usr/bin/python

import json, urllib

# flast list of categories
flat = []

# pull the tree
url = "https://api.foursquare.com/v2/venues/categories?oauth_token=V31SXZ1SGEI1DHAFRYS1SXEINBN5S21CQBTJF5H3M04RH3Q4&v=20131016"
response = urllib.urlopen(url);
data = json.loads(response.read())
for category in data['response']['categories']:
  flat.append({'category_id': category['id'], 'title': category['name']})
  for subcategory in category['categories']:
    flat.append({'category_id': subcategory['id'], 'title': subcategory['name']})

with open("index.js", "w") as f:
  f.write("'use strict';\n\nexports.categories = ");
  f.write(json.dumps(flat).replace("}, ", "},\n\t"));
  f.write(";")
