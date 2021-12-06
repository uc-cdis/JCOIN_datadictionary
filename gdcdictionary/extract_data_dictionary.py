import docx
from pathlib import Path
import  xmltodict
from jsonpath_ng import parse, JSONPathError
import zipfile
import yaml
import json
path = Path(r"C:\Users\kranz-michael\projects\phs-rcg\JCOIN_datadictionary\JCOIN Baseline Participant Measure Specifications 6-24-21 Final.docx")
doc = docx.Document(path)

#read in the document xml
xml = zipfile.ZipFile(path)
#xml.namelist() #use to read in the names of the xml files
doc_xml = xml.read('word/document.xml')

# convert xml to json
data_dict = xmltodict.parse(doc_xml)
#visualize structure of xml in a prettified json
with open('test.json','w') as f:
    json.dump(data_dict,f)


#"w:body" body of document
#"w:r" for row
#"w:t"

#""w:tblGrid"
#"w:c"
#"w:t"


body_xml = data_dict['w:document']['w:body']

#make a list of paragraph and table elements in order