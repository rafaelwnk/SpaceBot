import requests
from bs4 import BeautifulSoup
from chat.models import Satellite

url = 'https://www.heavens-above.com/Satellites.aspx'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" ,
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

def get_satellite_data(page):
    payload = {
        '__EVENTTARGET': 'ctl00$cph1$GridView1' ,
        '__EVENTARGUMENT': f'Page${page}' ,
        'ctl00$cph1$chkEO': '' ,
        'ctl00_cph1_btnNameSearch': 'Confirmar alterações'
    }

    session = requests.Session()

    response = session.post(url, data=payload, headers=headers)

    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find(
        name = 'table',
        attrs= {'class': 'standardTable'}
    )

    sat_data =[]

    for i, row in enumerate(table.find_all('tr')):
        if i == 0 or i == 21 or i == 22:
            continue
        cols = row.find_all('td')
        if cols:
            sat_name = cols[4].text.strip()
            orbital_state = cols[2].text.strip()
            designation= cols[3].text.strip()
            orbit = cols[5].text.strip()

            if not orbit:
                orbit = "Fora de órbita"

            sat_data.append((sat_name, orbital_state, designation, orbit))

    
    return sat_data

def save_satellites():
    for page in range(1, 51):
        sat_data = get_satellite_data(page)
        for data in sat_data:
            sat_name, orbital_state, designation, orbit = data
            Satellite.objects.update_or_create(
                name=sat_name,
                defaults={
                    'orbital_state': orbital_state,
                    'designation': designation,
                    'orbit': orbit
                }
            )