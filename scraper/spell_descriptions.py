from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame, read_csv
from itertools import chain
from os.path import join
from math import isnan


def download_spell_descriptions(link_extensions):
    base_url = 'https://dnd5e.wikidot.com'
    extensions_flat = list(chain(*link_extensions.values))
    extensions_clean = filter(lambda val: isinstance(val, str), extensions_flat)
    links = [f'{base_url}{ext}' for ext in extensions_clean]
    return links


if __name__ == '__main__':
    csv_path = join('data', 'spell_links.csv')
    link_extensions = read_csv(csv_path)
    l = download_spell_descriptions(link_extensions)
    pass