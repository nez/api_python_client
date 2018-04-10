	#!/usr/bin/python3

import client as api


# objeto de pruebas
query = {}
api.makeCall('sinaica', query)

# pageSize
query = {
    "pageSize": "10"
}
api.makeCall('sinaica', query)

# Igualdad
query = {
    "pageSize": "10",
    "parametro": "PM2.5",
    "estacionesid": 300
}
api.makeCall('sinaica', query)

# rangos
query = {
    "date-insert>=": "2017-06-29T19:00:00",
    "date-insert<=": "2017-07-29T19:00:00"
}
api.makeCall('sinaica', query)

# sort
query = {
    "sort": "date-insert",
    "pageSize": 10
}
api.makeCall('sinaica', query)
