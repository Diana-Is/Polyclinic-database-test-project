from appeallist import appList
from generallist import generalList
from appeal import appeal

class appListEdit(appList,generalList):
	def newRec(self,code,doctor,patient,date_of_application,diagnosis,price):self.appendList(appeal(code,doctor,patient,date_of_application,diagnosis,price))

	def getDoctor(self,code):return self.findByCode(code).getDoctor()
	def getPatient(self,code):return self.findByCode(code).getPatient()
	def getDate_of_application(self,code):return self.findByCode(code).getDate_of_application()
	def getDiagnosis(self,code):return self.findByCode(code).getDiagnosis()
	def getPrice(self,code):return self.findByCode(code).getPrice()

	def setDoctor(self,code,value):self.findByCode(code).setDoctor(value)
	def setPatient(self,code,value):self.findByCode(code).setPatient(value)
	def setDate_of_application(self,code,value):self.findByCode(code).setDate_of_application(value)
	def setDiagnosis(self,code,value):self.findByCode(code).setDiagnosis(value)
	def setPrice(self,code,value):self.findByCode(code).setPrice(value)
	def removebyDoctor(code):self.removeList(self.__doctor.getCode())
	def removebyPatient(code):self.removeList(self.__patient.getCode())