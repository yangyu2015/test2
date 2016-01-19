import os,shutil,re,xlrd,sys,time
reload(sys)
sys.setdefaultencoding("utf8")

dirName = "excel_lua"
readPath = "/Users/Yang/Documents/Job/Workspace/YYFramework/excel"
writePath = "/Users/Yang/Documents/Job/Workspace/YYFramework/coc/src/app/" + dirName

key = "id"      

if os.path.isdir(writePath):
	shutil.rmtree(writePath)
os.mkdir(writePath)
os.chdir(writePath)

def checkChangeInt(value):
	try:
		intValue = int(value)
		return str(intValue)
	except ValueError:
		return "\"" + value + "\""

def write(writeFileName,str):
	fileWrite = open(writeFileName + ".lua","w")
	try:
		fileWrite.write(str)
	finally:
		print "Finish write : " + writePath + "/" + writeFileName + ".lua!!!"
		fileWrite.close()

def createTable(sign,string):
	tString = "{"
	if sign == "|":
		tempList = string.split('|')
		for v in tempList:
			tString += createTable(':',v)
	elif sign == ":":
		tempList = string.split(':')
		for v in tempList:
			tString += createTable('#',v)
	else:
		tempList = string.split('#')
		for v in tempList:
			tString += checkChangeInt(v) + ","
	tString += "},"
	return tString

fileListString = "module (..., package.seeall)\nexcel_lua_id = {\n"
unfileListString = "excel_lua_unid = {\n"
filelist=os.listdir(readPath)  
regular_name = re.compile(r"(.+).xls")
for name in filelist:
	readFileName = os.path.join(readPath,name)
	if os.path.isfile(readFileName):
		excel = xlrd.open_workbook(readFileName)
		readFileName = re.findall(regular_name,name)[0]
		for i in range(excel.nsheets-1):
			index = i + 1
			writeFileName = readFileName + "_" + excel.sheet_names()[index]
			# print writeFileName
			sheet = excel.sheet_by_index(index)

			info = []
			keyCol = -1   
			string = "local {0} = {1}\n".format(writeFileName,"{")
			for i in range(sheet.ncols):
				item = [sheet.cell_value(rowx=0, colx=i),sheet.cell_value(rowx=1, colx=i),sheet.cell_value(rowx=3, colx=i)]
				if sheet.cell_value(rowx=0, colx=i) == key:
					keyCol = i
				info.append(item)

			createFlag = False
			headFileFlag = False
			for rnum in range(sheet.nrows-5):
				keyValue = sheet.cell_value(rowx=rnum+5, colx=keyCol)
				# print type(keyValue),keyValue
				if keyCol == -1 or keyValue == '' or info[keyCol][2] == "server":
					string += "\t{"
				else:
					if headFileFlag == False:
						headFileFlag = True
					string += "\t[{0}] = {1}".format(int(sheet.cell_value(rowx=rnum+5, colx=keyCol)),"{")
				for cnum in range(sheet.ncols):
					if info[cnum][2]  == "client":
						createFlag = True
						value = sheet.cell_value(rowx=rnum+5, colx=cnum)
						if info[cnum][1] == "int" or info[cnum][1] == "long":
							if value == "":
								value = 0
							if isinstance(value,float):
								string += "{0} = {1}, ".format(info[cnum][0],int(value))
							else:
								string += "{0} = {1}, ".format(info[cnum][0],value)
						elif info[cnum][1] == "table":
							if isinstance(value,float):
								value = int(value)
							value = str(value)
							if value == '':
								string += "{0} = \"\", ".format(info[cnum][0])
							else:
								tempString = createTable('|',value)
								string += "{0} = {1} ".format(info[cnum][0],tempString)
						else:
							if isinstance(value,unicode):
								if "\\" in value:
									value = value.replace("\\","\\\\")
								if "\'" in value:
									value = value.replace("\'","\\\'")
								if "\"" in value:
									value = value.replace("\"","\\\"")
							string += "{0} = \"{1}\", ".format(info[cnum][0],value)
				string += "},\n"
			string += "{1}\nreturn {0}".format(writeFileName,"}")

			if createFlag:
				if headFileFlag:
					fileListString += "\t\"src.app.excel_lua.{0}\",\n".format(writeFileName)
					headFileFlag = False
				else:
					unfileListString += "\t{0} = \"src.app.excel_lua.{0}\",\n".format(writeFileName)
				write(writeFileName,string)
fileListString += "}\n\n"+unfileListString + "}"
write("excel_lua",fileListString)