import pandas as pd

countries = pd.read_json('https://coronadatascraper.com/timeseries-byLocation.json')

def get_cases_curve(dias) : 
    casos_anterior = 0
    curva = []
    for casos in dias:
        curva.append(casos - casos_anterior)
        casos_anterior = casos

    return curva

def get_deaths_curve(mortes_por_dia) : 
    morte_anterior = 0
    curva = []
    for morte in mortes_por_dia:
        curva.append(morte - morte_anterior)
        morte_anterior = morte

    return curva


def get_dias(country): 
    if country not in countries:
        return [], [], [], []

    dias = []
    mortes = []   
    recovereds = []
    actives = []
    for date in countries[country]['dates']:
        if 'cases' in countries[country]['dates'][date]:
            cases = countries[country]['dates'][date]['cases']
        else :
            cases = 0

        if 'deaths' in countries[country]['dates'][date]:
            morte = countries[country]['dates'][date]['deaths']
        else:
            morte = 0
        
        if 'recovered' in countries[country]['dates'][date]:
            recovered = countries[country]['dates'][date]['recovered']
        else:
            recovered = 0

        if 'active' in countries[country]['dates'][date]:
            active = countries[country]['dates'][date]['active']
        else:
            active = 0

        if cases > 0:
            dias.append(cases)
            mortes.append(morte)
            recovereds.append(recovered)
            actives.append(active)

    return dias, mortes, recovereds, actives


def get_countries():
    return list(countries.keys())




