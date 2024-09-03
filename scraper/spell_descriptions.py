from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame, read_csv
from itertools import chain
from os.path import join
from math import isnan
import re
from pprint import pprint


def download_spell_descriptions(link_extensions):
    base_url = 'https://dnd5e.wikidot.com'
    extensions_flat = list(chain(*link_extensions.values))
    extensions_clean = filter(lambda val: isinstance(val, str), extensions_flat)
    links = [f'{base_url}{ext}' for ext in extensions_clean]
    spells = []
    for link in links:
        response = get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('div', id='page-content')
        paragraphs = content.find_all('p')
        description = [p.get_text() for p in paragraphs]
        spells.append(str2spell(description))

    return

def str2spell(description):
    source = description[0].split('Source:')[1].strip()
    level_text = description[1].split('-level')[0]
    level = 0 if 'cantrip' in level_text.lower() else int(level_text[0])
    bullet_points = ''.join(description[2].split(':')[1:]).split('\n')
    casting_time = bullet_points[0]
    range = int(bullet_points[1].split('Range')[1].split(' ')[1])
    components = bullet_points[2].split('Components')[1].split(',')
    ##TODO: split M components to 2 parts
    classes = description[-1].split('Spell Lists.')[1].split(',')
    general_description = '\n'.join(description[3:-1])

    spell = {
        "source": source,
        "level": level,
        "casting-time": casting_time,
        "range": range,
        "components": components,
        "classes": classes,
        "description": general_description
    }

    return spell

if __name__ == '__main__':
    csv_path = join('data', 'spell_links.csv')
    link_extensions = read_csv(csv_path)
    l = download_spell_descriptions(link_extensions)
    pass