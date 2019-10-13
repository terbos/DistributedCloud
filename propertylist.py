# RMI Server 
# Craig Gonzales - c1353987

import Pyro4
import os

# Don't forget to run this code: $ python -m Pyro4.naming

propertylist = [[0,0,[0,0]]]

# I used an array instead of a dictionary... it still works but I recognise it would have problems if this was a seriously big application.

# step 1 -- receive the propID from the client
# step 2 -- scan the propertyList[n][0] since ID is in the first spot ... need to learn about arrays within arrays
# step 3 -- if stuff-if there, return pL[2 & 3] which is lon/lat...
# step 4 -- if not in array, then get the owner, long, lat
# step 5 -- add the id, owner, long, lat to the array propertyList

class propertySearch(object):
	def scanProplist(self, propID): 
		n = 0
		cheatingVariable = 0
		while n < len(propertylist): 
			if propertylist[n][0] == propID:
				cheatingVariable = cheatingVariable + 1
				print "I am returning this to you: ", propertylist[n][2]
				return propertylist[n][2]
			else:
				n = n + 1
		if cheatingVariable > 0:
			print "Hope you find your way!"
		else:
			return -1

	def addNew(self, propID, propOwn, propll):
		propertylist.append([propID, propOwn, propll])
		print "Added the following data to our property list: ",
		print propID, propOwn, propll
		return "Added to list! Try again to prove it right!"


push_property=propertySearch()

daemon=Pyro4.Daemon()
ns=Pyro4.locateNS()
uri=daemon.register(push_property)
ns.register("property.id", uri)

print "Ready to search"
daemon.requestLoop()
