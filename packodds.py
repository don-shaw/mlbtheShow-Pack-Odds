from bs4 import BeautifulSoup
import requests
import csv
import uuid
requests.packages.urllib3.disable_warnings()

# Make sure you change the range function below to match the number of pages, I always do pages + 5 just in case


def get_cards(csv_file):

    headers = {
        'YOU NEED TO PUT YOUR HEADER INFORMATION HERE. FORGET ABOUT THE PARAMS PART AND THE REQUEST... JUST THE HEADERS!'
        }
    try:
            with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
                packfile = csv.DictWriter(csv_file, fieldnames=['pack type','pack id', 'date', 'url', 'item', 'type', 'rarity'])
                packfile.writeheader()
                for x in range(1, 25):
                    params = (('page', str(x) + '^'), ('', ''), )
                    print(params)
                    r = requests.get("https://theshownation.com/mlb20/packs/open_pack_history", headers=headers, params=params,
                                                                                                         verify=False)
                    print(r.url)
                    pagetext = r.text
                    soup = BeautifulSoup(pagetext, 'html.parser')
                    details = {}

                    pack_meta = soup.find_all("div", class_="section-pack-history-secondary")
                    #print(pack_meta)
                    #pack_items = soup.find_all("tr")

                    for x in pack_meta:
                        pack_type = x.find('h3').text
                        date_opened = x.find('p').text[7:16]
                        pack_items = x.find_all('tr')
                        pack_id = uuid.uuid4()


                        for p in pack_items:
                            item_name = p.find('td')

                            a_tags = p.find('a', {'href': True})
                            if a_tags is not None:
                                if a_tags.has_attr('href'):
                                    ending = a_tags['href']
                                    url = 'https://theshownation.com' + ending
                                    details['url'] = url

                            if p.contents[3].text == 'Name':
                                pass
                            else:
                                name = p.contents[3].text.lstrip('\n\n').rstrip('\n\n')
                                details['item'] = name



                            if p.contents[5].text == 'Type':
                                pass
                            else:
                                i_type = p.contents[5].text


                            for img in p.find_all('img', class_='icons-rarity'):
                                image = img['src']
                                details['rarity'] = image
                                image = image.split('shield-')[1]
                                image = image.rsplit('.png')[0]
                                packfile.writerow({'pack type': pack_type, 'pack id': pack_id.hex, 'date': date_opened, 'url': url,
                                                     'item': name, 'type': i_type, 'rarity': image})

    except Exception as e:
                    print(e)


if __name__ == '__main__':
    get_cards('packHistory.csv')