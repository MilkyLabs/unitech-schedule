import logging
from bs4 import BeautifulSoup
from requests import Session
from dataclasses import dataclass


@dataclass
class Group:
    name: str
    link: str

    def __init__(self, name: str, link: str):
        self.name = name
        self.link = link

GROUPS_URL      = "https://ies.unitech-mo.ru/schedule_list_groups?f={form}"
GROUPS_FORMS    = [1]#[1, 3, 6]

def parse():
    groups = []

    for form in GROUPS_FORMS:
        with Session() as session:
            response = session.get(GROUPS_URL.format(form=form))

            if response.status_code != 200:
                logging.error(f"Status code {response.status_code} for url {GROUPS_URL.format(form=form)}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('tr')

            for row in rows[1:]:
                cols = row.find_all('td')
                groups.append(Group(cols[0].text, cols[1].find('a', href=True)['href']))
        
    return groups
