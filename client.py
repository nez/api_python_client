#!/usr/bin/python3

import os
import sys
import urllib.request
import json
import xml.etree.ElementTree as etree
import re


def makeCall(collection, query):
    api_home = "https://api.datos.gob.mx/v2/{collection}?".format(collection=collection)

    url = api_home
    for key in query:
        operation = "="
        value = query[key]
        operator = key

        regexResult = re.search('(\<|\>)=?', operator)
        if regexResult is not None:
            operation = regexResult.group(0)
            operator = operator[ : (len(operation)*-1) ]

        url += "{key}{operation}{value}&".format(key=operator, value=value, operation=operation)
    url = url[:-1]

    print("CALL: " + url)
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


# objeto de pruebas
collection = "sinaica"
query = {}

result = makeCall(collection, query)
print(result["results"])
print("--------------------------------------------")


# pageSize
query = {
    "pageSize": "10"
}

result = makeCall(collection, query)
print(result)
print("--------------------------------------------")



# Igualdad
query = {
    "pageSize": "10",
    "parametro": "PM2.5",
    "estacionesid": 300
}

result = makeCall(collection, query)
print(result)
print("--------------------------------------------")


# rangos
query = {
    "date-insert>=": "2017-06-29T19:00:00",
    "date-insert<=": "2017-07-29T19:00:00"
}
result = makeCall(collection, query)
print(result)
print("--------------------------------------------")

# sort
query = {
    "sort": "date-insert",
    "pageSize": 10
}
result = makeCall(collection, query)
print(result)
print("--------------------------------------------")


print("----- Done")
