from patlist import patList
from generallist import generalList
from patient import patient

class patListEdit(patList,generalList):
	def newRec(self,code,surname="",name="",otchestvo="",year_of_birth=""):self.appendList(patient(code,surname,name,otchestvo,year_of_birth))
	def getSurname(self,code):return self.findByCode(code).getSurname()
	def getName(self,code):return self.findByCode(code).getName()
	def getOtchestvo(self,code):return self.findByCode(code).getOtchestvo()
	def getYear_of_birth(self,code):return self.findByCode(code).getYear_of_birth()

	def setSurname(self,code,value):self.findByCode(code).setSurname(value)
	def setName(self,code,value):self.findByCode(code).setName(value)
	def setOtchestvo(self,code,value):self.findByCode(code).setOtchestvo(value)
	def setYear_of_birth(self,code,value):self.findByCode(code).setYear_of_birth(value)