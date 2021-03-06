from services.covidapi import CovidApi
import json

covidApi = CovidApi()
pais = "MEX"
fecha = "2022-07-17"
print("APIQuery", pais, fecha, sep="\t")
print("="*40)
apiData = covidApi.getReports(pais, fecha)
#print(json.dumps(apiData, indent=4))
arr_data = apiData["data"]
for data_item in arr_data:
    confirmed = data_item["confirmed"]
    active = data_item["active"]
    province = data_item["region"]["province"]
    print(confirmed, active, province, sep="\t")
