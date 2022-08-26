from patient import patient
from generallist import generalList

class patList(generalList):
	def newItem(self,code,surname="",name="",otchestvo="",year_of_birth=""):generalList.appendItem(self,patient(code,surname,name,otchestvo,year_of_birth))
	def createItem(self, code,surname,name,otchestvo,year_of_birth):
		if code in self.getCodes():print("Пациент с кодом %s уже существует")
		else:generalList.appendItem(self,patList(self, code,surname,name,otchestvo,year_of_birth))