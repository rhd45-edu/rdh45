class Instructor: 
    def __init__(instruct,name,courseID):
        instruct.name = name;
        instruct.courseID = courseID
        
i1 = Instructor("Wergeles", 12345)

attemptsToEditCourse = 12345

def test():
    if i1.courseID == attemptsToEditCourse:
        assert i1 == attemptsToEditCourse
    else :
        assert s1.username == usernameEntered
