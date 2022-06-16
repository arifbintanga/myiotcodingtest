from datetime import datetime
import json
from itertools import groupby
import operator
import math
import datetime
import pandas as pd

with open("e:\CAD-IT\JSON Files\sensor_data.json") as file:
    # returns JSON object as a dictionary
    sensor_data = json.load(file)

  
# sort sensor_data by 'roomArea' key, and 'timestamp' key
updatedSensorData = sorted(sensor_data["array"], key = operator.itemgetter("roomArea", "timestamp"))


#return the numberof days since the epoch
def getDay(epoch):
    return math.floor(float((epoch/ (24 * 60 * 60 * 1000))))

#modify the timestamp for each sensor data
for data in updatedSensorData:
    startdate = "01/01/1970"
    timestampDate = pd.to_datetime(startdate) + pd.DateOffset(days=getDay(data["timestamp"]))
    day_timestamp = {'timestamp':timestampDate}
    data.update(day_timestamp)

df = pd.DataFrame(updatedSensorData)

aggSensorData = df.groupby(['roomArea', 'timestamp']).agg({'humidity': ['mean', 'min', 'max','median'],'temperature':['mean', 'min', 'max','median']})
aggSensorData.columns = ['humidity_mean', 'humidity_min', 'humidity_max', 'humidity_median','temperature_mean', 'temperature_min', 'temperature_max', 'temperature_median']
aggSensorData = aggSensorData.reset_index()

print(aggSensorData)

'''function .to_json have option date_format that can be set to 'iso' and not the default option 'epoch' '''
nomor_2 = aggSensorData.to_json('./nomor_2.json', orient='index')
