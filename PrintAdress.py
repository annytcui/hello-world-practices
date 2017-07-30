def printAddress(List):
    print name
    print number,
    print street
    print city + ",",
    print state,
    print postalcode
    print country

name = str(raw_input("Please enter your full name: "))
number = str(raw_input("Please enter your street number: "))
street = str(raw_input("Please enter your street name: "))
city = str(raw_input("Please enter the city you live in: "))
state = str(raw_input("Please enter the state you live in: "))
postalcode = str(raw_input("Please enter the postal code of your state: "))
country = str(raw_input("Please enter the country you live in: "))
List = [name, number, street, city, state, postalcode, country]

printAddress(List)
