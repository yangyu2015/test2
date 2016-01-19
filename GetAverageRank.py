
fileName = "/Users/Yang/Desktop/TestFactory.jmj"
# str = ""

# def analyseLineData(data):
# 	substr = ""
# 	testA = data.find(";")
# 	testB = data.find(";;")
# 	# print data
# 	print("testA : {0}".format(testA))
# 	print("testB : {0}".format(testB))
# 	startPos = data.find("self.")+5
# 	endPos = data.find("=")-1
# 	name = data[startPos:endPos]
# 	if name:
# 		if testB != -1:
# 			substr += "print(\"{0} : \")\n".format(name)
# 			substr += "for k,v in pairs(data.{0}) do\n".format(name)
# 			substr += "\tprint(k .. \" : \")\n"
# 			substr += "\tfor n,m in pairs(v) do\n"
# 			substr += "\t\tprint(\"====\" .. n .. \" : \" .. tostring(m))\n"
# 			substr += "\tend\n"
# 			substr += "end\n"
# 		else:
# 			if testA != -1:
# 				substr += "print(\"{0} : \")\n".format(name)
# 				substr += "for k,v in pairs(data.{0}) do\n".format(name)
# 				substr += "\tprint(k .. \" : \" .. tostring(v))\n"
# 				substr += "end\n"
# 			else:
# 				substr += "print(\"{0} : \" .. tostring(data.{0}))\n".format(name)

# 		return substr
# 	else:
# 		return ""
 

# fileRead = open(fileName,"r")
# for data in fileRead:
# 	str += analyseLineData(data)
# fileRead.close()

# fileWrite = open(fileName,"w")
# fileWrite.write(str)
# fileWrite.close()


dataDic = {1, 1, 1, 1, 1, 1, 7, 7, 1, 1, 11, 11, 5, 5, 7, 17}
for k

