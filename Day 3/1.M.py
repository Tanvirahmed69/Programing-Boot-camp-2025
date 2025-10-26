##Grade system: A(>=90), B(>=80), C(>=70), D(>=60), F

grade=float(input('what is your result?'))
                  
if grade >=101:
    print('no')                 
elif grade >=90 and grade <=100:
    print('A')
elif grade >=80:
    print('B')
elif grade >=70:
    print('C')
elif grade >=60:
    print('D')
elif grade >=101:
    print('no')
else:
    print('F')