class studentCourses: 
    def __init__(course,courseOne):
        course.courseOne = courseOne

c1 = studentCourses("CS 4320")

classAttemptingToAccess = "CS 4320"

classAttemptingToAccess = "Bio 1010"

def test_example():
    if c1.courseOne != classAttemptingToAccess:
        assert c1.courseOne == classAttemptingToAccess
    else:    
        assert c1.courseOne == classAttemptingToAccess
