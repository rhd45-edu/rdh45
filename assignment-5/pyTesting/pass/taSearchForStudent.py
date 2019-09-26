class TA: 
    def __init__(sec, number):
        sec.number = number

names = ['Albert','Stephanie','Raphael']

class courseSection:
    def __init__(section, number, studentNames):
        section.number = number
        section.studentnames = studentNames
        
teacherAssistant = TA(10)
section = courseSection(10,names)
enteredNameForSearch = "Raphael"

def test():
    if teacherAssistant.number == section.number:
	assert enteredNameForSearch in section.studentnames
    else:
        assert teacherAssistant.number == section.number

