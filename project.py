#Owen Andersons Homework 4

diameter = float(input("Enter a diameter: "))
wallthick = float(input("Enter a wall thickness: "))

radius = diameter/2

fullmassequation = ((4/3)*(3.14159265358)*(radius**3)-(4/3)*(3.14159265358)*((radius-wallthick)**3))*2700

print("the mass of the sphere in kg is: ",fullmassequation)

    




    