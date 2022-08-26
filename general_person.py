#-*- coding:utf-8 -*-
class general_person:
	def __init__(self,code=0,surname="",name="",otchestvo=""):
		self.setCode(code)
		self.setName(name)
		self.setSurname(surname)
		self.setOtchestvo(otchestvo)
	def setCode(self,value):self.__code=int(value)
	def setName(self,value):self.__name=value
	def setSurname(self,value):self.__surname=value
	def setOtchestvo(self,value):self.__otchestvo=value
	def getCode(self):return self.__code
	def getName(self):return self.__name
	def getSurname(self):return self.__surname
	def getOtchestvo(self):return self.__otchestvo