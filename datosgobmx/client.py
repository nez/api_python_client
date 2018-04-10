#!/usr/bin/python3

import os
import sys
import urllib.request
import json
import xml.etree.ElementTree as etree
import re

def makeCall(endpoint, query={}):
    """
    Make a request from api.datos.gob.mx
    endpoint: one of the endpoints available from https://api.datos.gob.mx
    query: dict with the query parameters, where no operator means =
    Example: makeCall('resources',{'pageSize': 1})"""
    url = "https://api.datos.gob.mx/v2/{endpoint}?".format(endpoint=endpoint)
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
        result = json.loads(response.read().decode("utf-8"))
        print(result)
        return result

def api(endpoint='api-catalog', query={}):
    makeCall(endpoint, query)['results']
