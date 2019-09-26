class Assignment: 
    def __init__(assignment,name,filetype):
        assignment.name = name
        assignment.filetype = filetype

a1 = Assignment("pyTest",".py")

fileName = "studentAssignment"
attemptedFileType = ".txt"

def testing():
    if a1.filetype != attemptedFileType:
        assert a1.filetype == attemptedFileType
    else:    
        assert a1.filetype == attemptedFileType
