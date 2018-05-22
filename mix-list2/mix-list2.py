#!/usr/bin/env python3
#Lab 9 more list business

proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
#print(proto)
#proto.append('dns') # this line will add 'dns' to the end of our list
#protoa.append('dns') # this line will add 'dns' to the end of our list
#print(proto)
proto2 = [ '22', '80', '443', '53' ] # a list of common ports
#proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
#print (proto)
#protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
#print (protoa)

#this will sort proto, protoa, and port2 alphebitcally

#adds proto2 into protoa which adds it into proto
proto.extend(proto2)
proto.extend(protoa)

#this sorts the extended lists(had to ensure inputs were like types)
proto.sort()
print (proto)