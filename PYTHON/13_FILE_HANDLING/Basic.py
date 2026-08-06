"""
File Handling
    When we want to create, update, read, delete any file we use file handling 
    - we have to use open() function to open any file
    -   'r' -> read (file must exist)
        'w' -> create or overwrite
        'a' -> append (Add to end of file)
        'x' -> create (create a new file)

"""
#  reading file-----------
# file = open("my-file", 'r') 
# print(file.read())

"""
with open("my-file", 'r') as f :
    content = f.read()  # read all the content

print(content)


 # instead of print all the text. let's print only 10 character
with open("my-file", 'r') as f :
    newContent = f.read(10) 
    print(f"only 10 chanracter: {newContent}")


#  readline(): read only the first line -------------
with open("my-file", 'r') as f :
    oneLine = f.readline()

    print(f"Read only first line: {oneLine}")
"""

# write file -------------------


with open("write-file", 'w') as f :
    f.write('This text will be written in a newly created file \n')

with open("write-file", 'a') as f :
    f.write("This text has to be appended at the end")


# deleting files ----------------------

import os
# os.remove("my-file")
if os.path.exists("my-file") :
    os.remove("my-file")
else :
    print("this file does not exist")



#  changing JSON into dictonary 
import json

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dict = json.loads(person_json)

print(type(person_dict))
print(person_dict)
print(person_dict["city"])


# changing dict into json

change_json = json.dumps(person_dict, indent=4)   # indent shows tabs 
print(type(change_json))
json_data = change_json
print(change_json)

# saving Json file 

with open("Json_output", "w") as f :
    f.write(change_json)



# ------ file with CSV (comma seperated value) Extention ----------

import csv
with open("csv_example.csv") as f : 
    csv_reader = csv.reader(f, delimiter=",")
    line = 0
    for rows in csv_reader :
        if line == 0 :
            print(f"Column names are {", ".join(rows)}")
            line += 1
        else :
            print(f"\t{rows[0]} is a teacher. He lives in {rows[1]}, {rows[2]}.")
            line += 1
print(f"Rows count: {line}")



# ------- File with xlsx Extension ----------

"""
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
"""


# ------- File with xml Extension-------------
import xml.etree.ElementTree as ET
tree = ET.parse("xml_example.xml")
root = tree.getroot()

print(f"Root Tag: ", root.tag)
print(f"Attribute: ", root.attrib)

for child in root :
    print(f"{child.tag} : {child.text}")
    skills = root.find("skills")
    
for skill in skills :
    print(f"{skill.text}")

