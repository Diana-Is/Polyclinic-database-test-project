#-*- coding:utf-8 -*-
from doclistedit import docListEdit
from patlistedit import patListEdit
from appeallistedit import appListEdit

class polyclinic():
	def __init__(self):
		self.__doctors=docListEdit()
		self.__patients=patListEdit()
		self.__appeals=appListEdit()
	def removeDoctor(self,code):
		docappcodes = []
		for c in self.__appeals.getCodes():
			docappcodes.append(self.__appeals.findByCode(c).getDoctor().getCode())
		if code in docappcodes:
			print('Cant_delete_doctor.He/she_still_has_an_appeal')
		else:
			self.__doctors.removeList(code)
	def removePatient(self,code):
		patappcodes = []
		for c in self.__appeals.getCodes():
			patappcodes.append(self.__appeals.findByCode(c).getPatient().getCode())
		if code in patappcodes:
			print('Cant_delete_patient.He/she_still_has_an_appeal')
		else:
			self.__patients.removeList(code)

	def removeAppeal(self,code):self.__appeals.removeList(code)
	def clear(self):
		self.__doctors.clear()
		self.__patients.clear()
		self.__appeals.clear()
	def newDoc(self,code=0,surname="",name="",otchestvo="",specialization="",category=""):self.__doctors.newRec(code,surname,name,otchestvo,specialization,category)
	def findDocByCode(self,code):return self.__doctors.findByCode(code)
	def getDocNewCode(self):return self.__doctors.getNewCode()
	def getDocCodes(self):return self.__doctors.getCodes()
	def getDocName(self,code):return self.__doctors.getName(code)
	def getDocSurname(self,code):return self.__doctors.getSurname(code)
	def getDocOtchestvo(self,code):return self.__doctors.getOtchestvo(code)
	def getDocSpecialization(self,code):return self.__doctors.getSpecialization(code)
	def getDocCategory(self,code):return self.__doctors.getCategory(code)

	def setDocName(self,code,value):return self.__doctors.setName(code,value)
	def setDocSurname(self,code,value):return self.__doctors.setSurname(code,value)
	def setDocOtchestvo(self,code,value):return self.__doctors.setOtchestvo(code,value)
	def setDocSpecialization(self,code,value):return self.__doctors.setSpecialization(code,value)
	def setDocCategory(self,code,value):return self.__doctors.setCategory(code,value)


	def newPat(self,code=0,surname="",name="",otchestvo="",year_of_birth=1971):self.__patients.newRec(code,surname,name,otchestvo,year_of_birth)
	def findPatByCode(self,code):return self.__patients.findByCode(code)
	def getPatNewCode(self):return self.__patients.getNewCode()
	def getPatCodes(self):return self.__patients.getCodes()
	def getPatName(self,code):return self.__patients.getName(code)
	def getPatSurname(self,code):return self.__patients.getSurname(code)
	def getPatOtchestvo(self,code):return self.__patients.getOtchestvo(code)
	def getPatYear_of_birth(self,code):return self.__patients.getYear_of_birth(code)

	def setPatName(self,code,value):return self.__patients.setName(code,value)
	def setPatSurname(self,code,value):return self.__patients.setSurname(code,value)
	def setPatOtchestvo(self,code,value):return self.__patients.setOtchestvo(code,value)
	def setPatYear_of_birth(self,code,value):return self.__patients.setYear_of_birth(code,value)


	def newApp(self,code=0,doctor=None,patient=None,date_of_application="",diagnosis="",price=0):self.__appeals.newRec(code,doctor,patient,date_of_application,diagnosis,price)
	def findAppByCode(self,code):return self.__appeals.findByCode(code)
	def getAppCodes(self):return self.__appeals.getCodes()
	def getAppDoctor(self,code):return self.__appeals.getDoctor(code)
	def getAppPatient(self,code):return self.__appeals.getPatient(code)
	def getAppPrice(self,code):return self.__appeals.getPrice(code)
	def getAppDiagnosis(self,code):return self.__appeals.getDiagnosis(code)
	def getAppDate_of_application(self,code):return self.__appeals.getDate_of_application(code)

	def setAppDoctor(self,code,value):return self.__appeals.setDoctor(code,value)
	def setAppPatient(self,code,value):return self.__appeals.setPatient(code,value)
	def setAppPrice(self,code,value):return self.__appeals.setPrice(code,value)
	def setAppDiagnosis(self,code,value):return self.__appeals.setDiagnosis(code,value)
	def setAppDate_of_application(self,code,value):return self.__appeals.setDate_of_application(code,value)


