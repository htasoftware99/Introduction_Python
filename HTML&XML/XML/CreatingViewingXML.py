import xml.etree.ElementTree as xml
students = [{
    'name': 'Hasan',
    'age': 23,
    'marks': 55
},
{
    'name': 'Mehmet',
    'age': 19,
    'marks': 90
}]

root = xml.Element('students')
for student in students:
    child = xml.Element('student')
    root.append(child)
    name = xml.SubElement(child, 'name')
    name.text = student.get('name')
    age = xml.SubElement(child, 'age')
    age.text = str(student.get('age'))
    marks = xml.SubElement(child, 'marks')
    marks.text = str(student.get('marks'))
tree = xml.ElementTree(root)
with open('myfile.xml', 'wb') as aux_file:
    tree.write(aux_file)