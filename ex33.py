print("second degree equation's format is a*(x^2)+b*x+c=o")

def first_degree_equation():
    a = int(input("please enter a: "))
    b = int(input("please enter b: "))
    c = int(input("please enter c: "))
    x1 = (-1*b+((b**2)-4*a*c)**(1/2))/(2*a)
    x2 = (-1*b-((b**2)-4*a*c)**(1/2))/(2*a)
    if x2 != x1 :
        print (" the first answer is = " , x1 )
        print (" the second answer is = " , x2 )
    else :
         print (" the only answer is = " , x1 )
    return x1,x2
first_degree_equation()   

