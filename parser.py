# import requests
# import re
# from bs4 import BeautifulSoup as BS
# import csv
# from tabulate import tabulate
# import pandas as pd

# url = 'https://www.newportrentals.com/apartments-jersey-city-for-rent/roosevelt-house/residence-420/'
# result = requests.get(url)
# doc = BS(result.text, 'html.parser')

# def get_info(doc, url):
#     info = {}
#     address_html = doc.select('div.body-big-subtext.unit-text.text-light')[1]
#     address = ''.join(word for word in address_html.stripped_strings)
#     info['Address'] = address
#     bedroom = doc.find(string=lambda text: text and re.search(r"Bedroom$", text))
#     info['Bedroom'] = bedroom
#     bathroom = doc.find(string=lambda text: text and re.search(r"Bathroom$", text))
#     info['Bathroom'] = bathroom
#     square = doc.find(string=lambda text: text and re.search(r"Ft$", text))
#     info['Square'] = square
#     price = doc.find(string=lambda text: text and re.search(r"^\$", text))
#     info['Price'] = price
#     info['URL'] = url
#     return info
    

# def save_m(doc, url):
#     info = get_info(doc, url)
#     with open('info.csv', 'w') as file:
#         W = csv.DictWriter(file, fieldnames=info.keys(), delimiter='\t')
#         W.writeheader()
#         W.writerow(info)
#     return info


# def see_data(info):
#     tb = pd.DataFrame([info])
#     tb['URL'] = tb['URL'].apply(lambda x: x if len(x) < 50 else x[:47] + '...')
#     print(tabulate(tb, headers='keys', tablefmt='fancy_grid', showindex=False))


# info = save_m(doc, url)
# see_data(info)