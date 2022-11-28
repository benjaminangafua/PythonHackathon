"""
Counties

TODO: Write a function named getCounty that when given a name of a capital, Ex: Bensonville, it prints out the county of the capital given.

Example 1:

getCounty('Bensonville');
Montserrado


Example 2:

getCounty('Gbarnga');
Bong

Example 3:

getCounty('Chicago');
Not a county!
"""


def main():

    capital = input("").title()
    getCounty(capital)

def getCounty(countyName):

    match countyName:

        case "Voinjama":
            print("Lofa")
        case "Zwedrew":
            print("Grand Gedeh")
        case "Buchana":
            print("Grand Bassa")
        case "Greenville":
            print("Sinoe")
        case "Sanniquellie":
            print("Nimba")
        case "Gbarnga":
            print("Bong")
        case "Barcleyville":
            print("Grand Kru")
        case "Bensonville" :
            print("Montserrado")
        case "Cestos City":
            print("River cess")
        case "Fishtown":
            print("River Gee")
        case "Robert Sport":
            print("Grand Cape Mount")
        case "Bopolu":
            print("Gbapolu")
        case "Tubmanburge":
            print("Bomi")
        case "Kakata":
            print("Margibi")
        case "Harper":
            print("Maryland")
        case _:
            print("Not a county")
main()