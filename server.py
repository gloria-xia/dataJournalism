from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():

    f = open("data/csvjson.json", "r")
    data = json.load(f)
    f.close()

    years=[2019, 2020, 2021, 2022]

    year = request.args.get('year')
    print(year)


    return render_template('about.html', years=years)

@app.route('/macro')
def macro():

    f = open("data/csvjson.json", "r")
    data = json.load(f)
    f.close()
    count2019 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    count2020 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    count2021 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    count2022 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    count2023 = {1: 0, 2: 0, 3: 0}

    for point in data:
        tempYear = point['Year']
        month = point['Month']
        if tempYear == 2019:
            count2019[month] += 1
        elif tempYear == 2020:
            count2020[month] += 1
        elif tempYear == 2021:
            count2021[month] += 1
        elif tempYear == 2022:
            count2022[month] += 1
        else:
            count2023[month] += 1
    macroData = {}
    macroData[2019] = count2019
    macroData[2020] = count2020
    macroData[2021] = count2021
    macroData[2022] = count2022
    macroData[2023] = count2023

    years = sorted(list(macroData.keys()))

    endpoints =[]

    for year in macroData:
        year = macroData[year]
        month = sorted(list(year.keys()))
        for i in range (len(year)-1):
            tempMonth = month[i]
            start_x = year[tempMonth]
            endMonth = month[i+1]
            end_x = year[endMonth]
            endpoints.append([start_x, end_x])
    print(endpoints)

    return render_template('macro.html', endpoints = endpoints, years = years)

@app.route('/micro')
def micro():

    f = open("data/csvjson.json", "r")
    data = json.load(f)
    f.close()

    years = [2019, 2020, 2021, 2022, 2023]

    year = request.args.get('year')
    print(year)

    yearData = []
    boroCount = {'RICHMOND': 0, 'KINGS': 0, 'NEW YORK': 0, 'QUEENS': 0, 'BRONX': 0}

    if year == '2019':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2019:
                boroCount[county] += 1
    elif year == '2020':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2020:
                boroCount[county] += 1
    elif year == '2021':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2021:
                boroCount[county] += 1
    elif year == '2022':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2022:
                boroCount[county] += 1
    else:
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2023:
                boroCount[county] += 1

    print(boroCount)

    
    return render_template('micro.html',years=years, year=year,queensCount=boroCount['QUEENS'],bronxCount=boroCount['BRONX'],nyCount=boroCount['NEW YORK'],
                            brooklynCount=boroCount['KINGS'],siCount=boroCount['RICHMOND'])


@app.route('/catetory')
def category():

    f = open("data/csvjson.json", "r")
    data = json.load(f)
    f.close()

    years = [2019, 2020, 2021, 2022, 2023]

    year = request.args.get('year')
    print(year)

    yearData = []
    typeCount = {'Race': 0, 'Religion': 0, 'Sexual Orientation': 0, 'Ethnicity': 0, 'Gender': 0, 'Age': 0, 'Disability': 0}

    if year == '2019':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2019:
                typeCount[category] += 1
    elif year == '2020':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2020:
                typeCount[category] += 1
    elif year == '2021':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2021:
                typeCount[category] += 1
    elif year == '2022':
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2022:
                typeCount[category] += 1
    else:
        for point in data:
            county = point['County']
            category = point['Category']
            if point['Year'] == 2023:
                typeCount[category] += 1

    print(typeCount)

    return render_template('category.html', categories=typeCount.keys(),years=years, year=year, typeCount=typeCount, raceCount=typeCount['Race'],
                            religionCount=typeCount['Religion'],sexualityCount=typeCount['Sexual Orientation'],ethnicityCount=typeCount['Ethnicity'],
                            genderCount=typeCount['Gender'],ageCount=typeCount['Age'],disabilityCount=typeCount['Disability'])



app.run(debug=True)
