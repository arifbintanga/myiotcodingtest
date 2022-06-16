import datetime
import pandas as pd
startdate = "01/01/1970"
enddate = pd.to_datetime(startdate) + pd.DateOffset(days=5)
print(enddate.date())

output = {
        "0":{
            "timestamp":1655323806,
            "humidity":95.753949879,
            "temperature":17.2513526316,
            "roomArea":"roomArea1"},
        "1":{
            "timestamp":1655323808,
            "humidity":96.6564762405,
            "temperature":18.6837295195,
            "roomArea":"roomArea1"},
        "2":{
            "timestamp":1655323810,
            "humidity":94.7925736759,
            "temperature":19.219402959,
            "roomArea":"roomArea1"}
        }   