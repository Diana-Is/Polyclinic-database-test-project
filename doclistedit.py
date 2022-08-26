from doclist import docList
from generallist import generalList
from doctor import doctor


class docListEdit(docList,generalList):
	def newRec(self,code=0,surname="",name="",otchestvo="",specialization="",category=""):self.appendList(doctor(code,surname,name,otchestvo,specialization,category))
	def getSurname(self,code):return self.findByCode(code).getSurname()
	def getName(self,code):return self.findByCode(code).getName()
	def getOtchestvo(self,code):return self.findByCode(code).getOtchestvo()
	def getSpecialization(self,code):return self.findByCode(code).getSpecialization()
	def getCategory(self,code):return self.findByCode(code).getCategory()	
	
	def setSurname(self,code,value):self.findByCode(code).setSurname(value)
	def setName(self,code,value):self.findByCode(code).setName(value)
	def setOtchestvo(self,code,value):self.findByCode(code).setOtchestvo(value)
	def setSpecialization(self,code,value):self.findByCode(code).setSpecialization(value)
	def setCategory(self,code,value):self.findByCode(code).setCategory(value)