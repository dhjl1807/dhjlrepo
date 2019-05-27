# -*- coding: utf-8 -*-
import json


def parse_city():
    citylists = []
    with open('city.json', 'r', encoding='utf-8') as f:
        cities = json.load(f)
        zpdata = cities['zpData']
        cityList = zpdata['hotCityList']
        for item in cityList:
            cityID = item['code']
            citylists.append(str(cityID))
        return citylists


if __name__ == '__main__':
    print(parse_city())
