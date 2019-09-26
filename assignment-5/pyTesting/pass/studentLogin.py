class studentLogin: 
    def __init__(student,username,password):
        student.username = username
        student.password = password
        
s1 = studentLogin("Raphael","testingPython")

usernameEntered = "Raphael"
passwordEntered = "testingPython"


def test():
    if usernameEntered == s1.username:
        assert s1.password == passwordEntered
    else :
        assert s1.username == usernameEntered
