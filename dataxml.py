#-*- coding:utf-8 -*-
import os,xml.dom.minidom
from data import data
class dataxml(data):
 def read(self):
  dom=xml.dom.minidom.parse(self.getInp())
  dom.normalize()
  for node in dom.childNodes[0].childNodes:
   if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='doctor'):
    code,surname,name,otchestvo,specialization,category=0,"","","","",""
    for t in node.attributes.items():
     if t[0]=="code":code=int(t[1])
     if t[0]=="surname":surname=t[1]
     if t[0]=="name":name=t[1]
     if t[0]=="otchestvo":otchestvo=t[1]
     if t[0]=="specialization":specialization=t[1]
     if t[0]=="category":category=t[1]
    self.getLib().newDoc(code,surname,name,otchestvo,specialization,category)
   if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='patient'):
    code,surname,name,otchestvo,year_of_birth=0,"","","",""
    for t in node.attributes.items():
     if t[0]=="code":code=int(t[1])
     if t[0]=="surname":surname=t[1]
     if t[0]=="name":name=t[1]
     if t[0]=="otchestvo":otchestvo=t[1]
     if t[0]=="year_of_birth":year_of_birth=t[1]
    self.getLib().newPat(code,surname,name,otchestvo,year_of_birth)
   if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='appeal'):
    code,doctor,patient,date_of_application,diagnosis,price=0,"","","","",""
    for t in node.attributes.items():
     if t[0]=="code":code=int(t[1])
     if t[0]=="doctor":doctor=self.getLib().findDocByCode(int(t[1]))
     if t[0]=="patient":patient=self.getLib().findPatByCode(int(t[1]))
     if t[0]=="date_of_application":date_of_application=t[1]
     if t[0]=="diagnosis":diagnosis=t[1]
     if t[0]=="price":price=int(t[1])
    self.getLib().newApp(code,doctor,patient,date_of_application,diagnosis,price)
    
 
 def write(self):
  dom=xml.dom.minidom.Document()
  root=dom.createElement("polyclinic")
  dom.appendChild(root)
  for c in self.getLib().getDocCodes():
   doc=dom.createElement("doctor")
   doc.setAttribute('code',str(c))
   doc.setAttribute('surname',self.getLib().findDocByCode(c).getSurname())
   doc.setAttribute('name',self.getLib().getDocName(c))
   doc.setAttribute('otchestvo',self.getLib().getDocOtchestvo(c))
   doc.setAttribute('spezialization',self.getLib().getDocSpecialization(c))
   doc.setAttribute('category',self.getLib().getDocCategory(c))
   root.appendChild(doc)
  for c in self.getLib().getPatCodes():
   pat=dom.createElement("patient")
   pat.setAttribute('code',str(c))
   pat.setAttribute('surname',self.getLib().getPatSurname(c))
   pat.setAttribute('name',self.getLib().getPatName(c))
   pat.setAttribute('otchestvo',self.getLib().getPatOtchestvo(c))
   pat.setAttribute('year_of_birth',self.getLib().getPatYear_of_birth(c))
   root.appendChild(pat)
  for c in self.getLib().getAppCodes():
   app=dom.createElement("appeal")
   app.setAttribute('code',str(c))
   app.setAttribute('doctor',str(self.getLib().getAppDoctor(c).getCode()))
   app.setAttribute('patient',str(self.getLib().getAppPatient(c).getCode()))
   app.setAttribute('date_of_application',self.getLib().getAppDate_of_application(c))
   app.setAttribute('diagnosis',self.getLib().getAppDiagnosis(c))
   app.setAttribute('price',str(self.getLib().getAppPrice(c)))
   root.appendChild(app)
  f = open(self.getOut(),"w")
  f.write(dom.toprettyxml())
