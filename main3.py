#-*- coding:utf-8 -*-
from polyclinic import polyclinic
from datasql import datasql
from dataxml import dataxml
import os

#from datajson import datajson

pol1=polyclinic()
pol2=polyclinic()
dxml1=dataxml(pol1,'old.xml','new.xml')
dxml2=dataxml(pol2,'old.xml','new.xml')

dsql1=datasql(pol1,'new.sqlite','new.sqlite')
dxml1.read()
if os.path.isfile(dsql1.getOut()):os.remove(dsql1.getOut())
dsql1.write()  
dsql1.read()
dxml2.write()