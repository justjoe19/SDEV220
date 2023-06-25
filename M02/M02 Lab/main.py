""" 
Joe Hollenbach
M02 Lab
This application will allow the user to enter the student's last name, first name and 
grade point average (GPA).  If the last name entered is 'ZZZ', the app will close.  If 
the GPA entered is 3.25 to 3.49, a message will print saying the student has made the 
Honor Roll.  If the GPA is 3.5 or greater, a message will print saying that the student 
has made the Dean's List.
""" 

def main():

    # Ask for and accept a student's last name.  Quit processing student records if the 
    # last name entered is 'ZZZ'.
    last_name = input("\nPlease enter the student's last name: ")
    if last_name == "ZZZ":
        return

    # Ask for and accept a student's first name.
    first_name = input("Please enter the student's first name: ")
    
    # Ask for and accept the student's GPA as a float.
    gpa = float(input("Please enter the student's grade point average (GPA): "))

    # Test if the student's GPA is 3.5 or greater and, if so, print a message saying that
    # the student has made the Dean's List.  If the student's GPA is 3.25 - 3.49,
    # print a message saying that the student has made the Honor Roll.  If the GPA is less
    # than 3.25, the program will close.
    if gpa >= 3.5:
        print("Congratulations, you made the Dean's List!\n")
    elif gpa >= 3.25:
        print("Congratulations, you made the Honor Roll!\n")
    else:
        print("\n")
        return

if __name__ == "__main__":
    main()
