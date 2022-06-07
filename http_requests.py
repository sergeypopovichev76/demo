# -*- coding: utf-8 -*-
import requests

list_of_hero = ('Hulk', 'Thanos', 'Captain America')
id_list_of_hero = []
for hero in list_of_hero:
    url_search_id_hero = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
    resp_id = requests.get(url_search_id_hero)
    id_list_of_hero.append(resp_id.json()['results'][0]['id'])
id_list_of_hero = tuple(id_list_of_hero)

intelligence_list = []
for id in id_list_of_hero:
    url_hero_powerstats = f'https://superheroapi.com/api/2619421814940190/{id}/powerstats'
    resp_powerstats = requests.get(url_hero_powerstats)
    intelligence_list.append(resp_powerstats.json()['intelligence'])

hero_intelligence = {list_of_hero[i]: int(intelligence_list[i]) for i in range(len(list_of_hero))}

list_hero_intelligence = sorted(tuple(hero_intelligence.items()), key=lambda x: x[1], reverse=True)

print(f'Самый умный супергерой из представленного списка {list_hero_intelligence[0][0]}.')
