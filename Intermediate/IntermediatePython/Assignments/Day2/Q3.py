
Celsius = [39.2, 36.5, 37.3, 37.8]

def CtoF(x):
    return ((float(9)/5)*x + 32)

def FtoC(x):
    return (float(5)/9)*(x-32)


Fahrenheit = list(map(CtoF,Celsius))

print(Fahrenheit)

NewCelcius = map(FtoC,Fahrenheit)

print(list(NewCelcius))
