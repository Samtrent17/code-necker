#
'''def findAreaOfRectangle():
    length = 6
    width = 4
    area = length * width
    print("The area of the rectangle is:", area)

#calling a function
findAreaOfRectangle()

#Defining function(Return)
def findAreaOfRectangle2():
    length = 7
    width = 5
    area2 = length * width
    return area2
#calling function(Return)
print('Area (return) is',findAreaOfRectangle2()) 




#define function
def Names():
    Firstname = 'NANGOLI'
    Lastname = 'SAMUEL'
    Name = Firstname + ' ' + Lastname
    print('Full Names are:',Name)
Names()

#define using return function 
def Names2():
    Firstname = 'Wamala'
    Lastname = 'Jassim'
    Name = Firstname + ' ' + Lastname
    return Name

#calling function using return
print('Full Names (return) are:',Names2())

def findAreaOfRectangleParameter(length, width):
    area = length * width
    print('Area is',area)
findAreaOfRectangleParameter()


def findAreaOfRectangleParameterReturn(length, width):
    area = length * width
    return area
findAreaOfRectangleParameterReturn(4,6)



#define function
def convertToEuros():
    EUR = 'Euros'
    UGX = 'Ugandan shillings'
    exchange_rate = 4000 
    amount = 200000
    conversionAmount = amount / exchange_rate
    print('The Amount in Euros is',conversionAmount)

#calling function
convertToEuros()

#defining using return function
def figureEuros():
    EUR = 'Euros'
    UGX = 'Ugandan shillings'
    exchange_rate = 4000 
    amount = 200000
    convertAmount = amount / exchange_rate
    return convertAmount

#output
print('The Amount in Euros (return) is',figureEuros())
#callong function
figureEuros()'''


#define function
def distance_travelled():
    speed = 60
    time = 3
    distance_covered = speed * time
    print('The distance covered is',distance_covered)
    