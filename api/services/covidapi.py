import requests
import json


class CovidApi:
    def getReports(self, iso, date):
        url = "https://covid-19-statistics.p.rapidapi.com/reports"
        querystring = {"iso": iso, "date": date}
        headers = {
            "X-RapidAPI-Key": "1ead6b9fb3msh90d4404a2b71121p1b963bjsncf4dad082546",
            "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        return json.loads(response.text)
