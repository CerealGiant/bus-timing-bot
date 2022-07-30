#Util file that contains all the functions that extract the data from the API
from datamall_api import getData as loadData

class busData:
	def __init__(self,stopCode):
		self.stopCode = stopCode
		self.file = loadData(self.stopCode)

	def extractBuses(self):
		#Based on the python dict generated
		buses = []
		for service in self.file['Services']:
			buses.append(service['ServiceNo'])
		return buses

	def extractBusTimings(self,buses):		
		#Taking values of next three buses
		next_bus = []
		next_bus2 = []
		next_bus3 = []
		for id,service in enumerate(self.file['Services']):
			#print("{} -> {}".format(buses[id],service['NextBus']['EstimatedArrival']))
			next_bus.append(service['NextBus']['EstimatedArrival'])

		for id,service in enumerate(self.file['Services']):
			#print("{} -> {}".format(buses[id],service['NextBus2']['EstimatedArrival']))
			next_bus2.append(service['NextBus2']['EstimatedArrival'])


		for id,service in enumerate(self.file['Services']):
			#print("{} -> {}".format(buses[id],service['NextBus3']['EstimatedArrival']))
			next_bus3.append(service['NextBus3']['EstimatedArrival'])

		return next_bus,next_bus2,next_bus3

	

		
