"""
Capitals

TODO: Write a function named getCapital that when given a county name, Ex: Montserrado, it prints out the capital of that county.

Example 1:

getCapital('Montserrado');
Bensonville


Example 2:

getCapital('Bong');
Gbarnga

Example 3:

getCapital('Miami');

"""

def main():

    county = input("").title()
    getCapital(county)

def getCapital(countyName):

    match countyName:

        case "Lofa":
            print("Voinjama")
        case "Grand Gedeh":
            print("Zwedrew")
        case "Grand Bassa":
            print("Buchana")
        case "Sinoe":
            print("Greenville")
        case "Nimba":
            print("Sanniquellie")
        case "Bong":
            print("Gbarnga")
        case "Grand Kru":
            print("Barcleyville")
        case "Montserrado":
            print("Bensonville")
        case "River cess":
            print("Cestos City")
        case "River Gee":
            print("Fishtown")
        case "Grand Cape Mount":
            print("Robert Sport")
        case "Gbapolu":
            print("Bopolu")
        case "Bomi":
            print("Tubmanburge")
        case "Margibi":
            print("Kakata")
        case "Maryland":
            print("Harper")
        case _:
            print("Not a county!")
main()