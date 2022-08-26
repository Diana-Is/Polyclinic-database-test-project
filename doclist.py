from doctor import doctor
from generallist import generalList

class docList(generalList,doctor):
	def newItem(self,code="0",surname="",name="",otchestvo="",specialization="",category=""):generalList.appendItem(self,doctor(code,surname,name,otchestvo,specialization,category))
	def createItem(self,code="0",surname="",name="",otchestvo="",specialization="",category=""):
		if code in self.getCodes():print("Специалист с кодом %s уже существует")
		else:generalList.appendItem(self,doctor(code,surname,name,otchestvo,specialization,category))