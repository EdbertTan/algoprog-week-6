coursenumber = ("COP 2510","EGN 3000L","MAC 2281","MUH 3016","PHY 2048")
coursename = { coursenumber[0]:"Programming Concepts",
coursenumber[1]:"foundations of engineering lab",
coursenumber[2]:"Calculus I",
coursenumber[3]:"Survey of Jazz",
coursenumber[4]:"General Physics I"
}
instructors = { coursenumber[0]:"Z. Beasley",
coursenumber[1]:"J. Anderson",
coursenumber[2]:"A. Makaryus",
coursenumber[3]:"A. Wilkins",
coursenumber[4]:"G. Pradhan"
}
classtimes = { coursenumber[0]:"MW 12:30pm – 1:45pm",
coursenumber[1]:"TR 11:00am – 12:15pm",
coursenumber[2]:"MW 9:30am – 10:45am",
coursenumber[3]:"online asynchronous",
coursenumber[4]:"TR 5:00pm – 6:15pm"
}

coursenuminput = input("Enter a course number: ")
x = coursenuminput.upper()
z = 0
for name in coursenumber:
    if x == name:
        y = coursenumber.index(name)
        print(f"The course details are:\nCourse Name: {coursename[coursenumber[y]]}\nInstructor: {instructors[coursenumber[y]]}\nClass Times: {classtimes[coursenumber[y]]}")
        z = 0
        break
    else:
        z = 1
if z == 1:
    print(f"{x} is an invalid course number.")
