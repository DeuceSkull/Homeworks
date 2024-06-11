from countryinfo import CountryInfo
from pprint import pprint
import json

country_data = []
while True:
    country_name = input('Davlat nomini kiriting: ')
    if country_name == 'stop':
        print('Dastur toxtadi !')
        with open('country.info', mode='a', encoding='utf-8') as file:
            json.dump(country_data, file, indent=4, ensure_ascii=False)
        break
    try:
        get_country = CountryInfo(country_name)
        data = get_country.info()
        pprint(data)

        name = data['name']
        area = data['area']
        capital = data['capital']
        population = data['population']
        currencies = data['currencies']
        languages = data['languages']
        region = data['region']
        borders = data['borders']
        iso = data['ISO']
        alt_spellings = data['altSpellings']
        calling_code = data['callingCodes']
        capital_latlng = data['capital_latlng']
        demonym = data['demonym']
        flag = data['flag']
        geo_JSON = data['geoJSON']
        native_name = data['nativeName']
        provinces = data['provinces']
        subregion = data['subregion']
        timezones = data['timezones']
        tld = data['tld']
        translations = data['translations']
        wiki = data['wiki']


        pprint(f"""{name} davlat xaqida ma'lumotlar:
{name} davlat {region} qit'asida joylashgan bo'lib,
Uning xududi: {area} km/kv,
Poytaxti: {capital},
Axoli soni: {population},
Valyuta: {currencies},
Tillar: {languages},
Chegaradoshlari: {borders},
ISO: {iso},
Alt Imlolar: {alt_spellings},
Qo'ng'iroq kodi: {calling_code},
Kapital latlng: {capital_latlng},
Demonim: {demonym},
Bayrog'i: {flag},
GeoJSON: {geo_JSON},
Mahalliy nomi: {native_name},
Viloyatlar: {provinces},
Subregion: {subregion},
Vaqt zonalari: {timezones},
Tld: {tld},
Tarjimalar: {translations},
Wiki: {wiki}
""")

        country_data.append({
            'name': name,
            'area': area,
            'population': population,
            'capital': capital,
            'currencies': currencies,
            'languages': languages,
            'region': region,
            'borders': borders,
            'ISO': iso,
            'altSpellings': alt_spellings,
            'callingCodes': calling_code,
            'capital_latlng': capital_latlng,
            'demonym': demonym,
            'flag': flag,
            'geoJSON': geo_JSON,
            'nativeName': native_name,
            'provinces': provinces,
            'subregion': subregion,
            'timezones': timezones,
            'tld': tld,
            'translations': translations,
            'wiki': wiki
        })



    except Exception:
        print('Xato kiritingiz !!!')
