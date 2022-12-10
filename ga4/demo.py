import os  
from ga4 import GA4RealTimeReport

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'smartclick-main-5ede53252196.json'

property_id = '324194880'

#property_id = '323646045'

lst_dimension = ['country','deviceCategory']
lst_metrics = ['activeUsers']

ga4_realtime = GA4RealTimeReport(property_id)
response = ga4_realtime.query_report(lst_dimension,lst_metrics,10,True)

print(response)