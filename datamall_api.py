import json
import requests

URL = 'http://datamall2.mytransport.sg/'
PATH = 'ltaodataservice/BusArrivalv2?'

HEADERS = {
'AccountKey': '/8ejWnEdS46+g+b5JC7+1w==',
'accept': 'application/json'
}

def getData(busStopCode):
	final_url = URL+PATH
	parameters = {
		'BusStopCode':busStopCode
	}
	
	r = requests.get(final_url,headers=HEADERS,params=parameters)
		
	#Converting into a python dict
	file = json.loads(r.content)
		
	return file

if __name__ == '__main__':
	getData(83139)

