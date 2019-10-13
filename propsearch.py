import Pyro4

propID=raw_input("Enter the ID: ").strip()

push_property=Pyro4.Proxy("PYRONAME:property.id")

a = push_property.scanProplist(propID) 

if a == -1:
	propOwn=raw_input("Who owns this property? ").strip()
	propLong=raw_input("What is the longitude? ").strip()
	propLat=raw_input("What is the latitude? ").strip()
	b= [propLong,propLat]
	print push_property.addNew(propID, propOwn,b) 
else:
	print "The longitude and latitude of your location is: ",
	print a[0],
	print ",",
	print a[1]


# this is used because me as a client wants to either look up this id or add info for this id... so i have to give an ID... the server will tell me if it already exists by running the function scanProplist() on the RMI server... if it does exist, it will give me the location, if it does not, it will make me to give the own and location



# client asks for the ID ... server searches to see if the ID is there... if yes, then it gives the long and lat... if not, it asks for the owner and the long and the lat, and then stores that information in the data structure
