from appeal import appeal
from generallist import generalList

class appList(generalList):
	def newItem(self,code,doctor,patient,date_of_application,diagnosis,price):generalList.appendItem(self,appeal(code,doctor,patient,date_of_application,diagnosis,price))
	def createItem(self, code,surname,name,otchestvo,year_of_birth):
		if code in self.getCodes():print("Запись с кодом %s уже существует")
		else:generalList.appendItem(self,appList(self,code,surname,name,otchestvo,year_of_birth))