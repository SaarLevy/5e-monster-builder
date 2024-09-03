from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame

def get_links(url):
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table_class = 'wiki-content-table'
    tables = soup.find_all('table', class_=table_class)

    links_matrix = []

    for table_index, table in enumerate(tables):
        links = table.find_all('a', href=True)
        column_links = [link['href'] for link in links] 
        links_matrix.append(column_links)
    return links_matrix


if __name__ == '__main__':
    url = 'https://dnd5e.wikidot.com/spells'
    DataFrame(get_links(url)).to_csv('spell_links.csv')
    pass