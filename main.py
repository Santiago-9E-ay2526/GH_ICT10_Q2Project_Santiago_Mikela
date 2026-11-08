# Project
from pyscript import display, document
# DRILL 2
# Members from G7-10
G7Club = {"Ryan Foster", "Olivia Hayes", "Sarah Morgan", "Megan Cooper"}
G8Club = {"Daniel Brooks", "Hannah Mitchell", "Ethan Parker", "Chloe Bennett"}
G9Club = {"Mateo Gozun", "Qualaen Mate", "Zadie Zagala", "Emily Carter"}
G10Club = {"Jaena Ambata", "Guia Dahap", "Chelsea Nortiga"}

AllMembers = G7Club | G8Club | G9Club | G10Club   # joins members from g7-10

# Adds users to the club list
def submit_name(e):
     document.getElementById('result').innerHTML = ' '

     # Name input
     firstname_input = " ".join(document.getElementById('firstname').value.strip().split())    # removes extra spaces
     lastname_input = " ".join(document.getElementById('lastname').value.strip().split())
     fullname = ((firstname_input + " " + lastname_input).title())

     AllMembers.add(fullname)      # adds typed name to set
     SortedMembers = "\n".join(sorted(AllMembers))     # sorts members alphabetically and puts each name on separate lines

     display(f"{SortedMembers}\n\nTotal Members: {len(AllMembers)}", target='result')     # displays all members and total number of members



# SKILLS TEST
def submit_details(e):
     document.getElementById('result').innerHTML = ' '
     enteredSym = document.getElementById('elSym').value.title()      # 1st letter of symbol will automatically be capitalized
     nonMetalName = {
          'H':'Hydrogen',
          'He':'Helium',
          'C': 'Carbon',
          'N':'Nitrogen',
          'O':'Oxygen',
          'F':'Fluorine',
          'Ne':'Neon',
          'P':'Phosphorus',
          'S':'Sulfur',
          'Cl':'Chlorine',
          'Ar':'Argon',
          'Se':'Selenium',
          'Br':'Bromine',
          'Kr':'Krypton',
          'I':'Iodine',
          'Xe':'Xenon',
          'Rn':'Radon',
     }

     nonMetalNum = {
          'H':'1',
          'He':'2',
          'C': '6',
          'N':'7',
          'O':'8',
          'F':'9',
          'Ne':'10',
          'P':'15',
          'S':'16',
          'Cl':'17',
          'Ar':'18',
          'Se':'34',
          'Br':'35',
          'Kr':'36',
          'I':'53',
          'Xe':'54',
          'Rn':'86',
     }

     nonMetalMass = {
          'H':'1.0078',
          'He':'4.0026',
          'C': '12.011',
          'N':'14.007',
          'O':'15.999',
          'F':'18.998',
          'Ne':'20.180',
          'P':'30.974',
          'S':'32.065',
          'Cl':'35.453',
          'Ar':'39.948',
          'Se':'78.960',
          'Br':'79.904',
          'Kr':'83.798',
          'I':'126.90',
          'Xe':'131.29',
          'Rn':'222',
     }

     display(f"Symbol: {enteredSym} \n Element: {nonMetalName.get(enteredSym, 'Not found')} \n Atomic Number: {nonMetalNum.get(enteredSym)} \n Atomic Mass: {nonMetalMass.get(enteredSym)}", target='result')     # Displays output in separate lines



# SW1
# checks if user is part of club
def check_user(e):
     document.getElementById('result').innerHTML = ' '
     firstname_input = " ".join(document.getElementById('firstname').value.strip().split())         #removes extra spaces
     lastname_input = " ".join(document.getElementById('lastname').value.strip().split())
     fullname = ((firstname_input + " " + lastname_input).title())         #removes extra spaces
     clubmembers = ["Mikela Santiago", "Jaena Ambata", "Guia Dahap", "Chelsea Nortiga", "Mateo Gozun", "Qualaen Mate", "Zadie Zagala"]
     studentchecker = fullname in clubmembers          #checks if the typed name is in the member list
     displaymessage = (f'Sorry, {fullname}, your name is not on the list.', f'Congratulations, {fullname}! You are part of the Book Club!')         #texts for not in club and in club

     display(displaymessage[studentchecker], target='result')