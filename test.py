from utils import busData

if __name__ =='__main__':
	bd = busData(83139)
	buses = bd.extractBuses()
	n1,n2,n3 = bd.extractBusTimings(buses)

	for n in n1:
		print(n)
