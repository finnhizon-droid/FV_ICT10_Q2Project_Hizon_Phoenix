from pyscript import document, display




#SEATWORK1
#List of the already accepted basketball varsity members

varsity_members = ["Phoenix Hizon", "Erin Urbano", "Joaquin Castor", "Jarvis Joven", "Enzo Ruiz", "Rocky Saludez", "Miguel Santos"]

#Clicking the button triggers this event to verify if the inputted name is in the given list

def verify(event):

# 2 & 3. Get input values and combine into one full name using f-strings

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = f"{first_name} {last_name}"

#Using if/else statements to verify the inputted name and to set the message

    if candidate_name in varsity_members:
        message = f"Congratulations {candidate_name}! You are now part of the ICT club."
        styling = "member-found"

    else:
        message = f"Sorry {candidate_name}, your name is not on the list."
        styling = "member-not-found"

#Display the text and apply CSS to it

    result_div = document.getElementById("result")
    result_div.innerText = message
    result_div.className = styling
    result_div.style.opacity = "1"





#SKILLS TEST
# Dictionary containing elements
nonmetals = {
    "H": ("Hydrogen", 1, 1.008), 
    "He": ("Helium", 2, 4.002), 
    "F": ("Fluorine", 9, 19.00), 
    "Ne": ("Neon", 10, 20.18), 
    "P": ("Phosphorus", 15, 30.97), 
    "C": ("Carbon", 6, 12.01), 
    "N": ("Nitrogen", 7, 14.007), 
    "O": ("Oxygen", 8, 15.999), 
    "S": ("Sulfur", 16, 32.06), 
    "Cl": ("Chlorine", 17, 35.45), 
    "Se": ("Selenium", 34, 78.96), 
    "Br": ("Bromine", 35, 79.90), 
    "I": ("Iodine", 53, 126.90), 
    "Ar": ("Argon", 18, 39.95), 
    "Kr": ("Krypton", 36, 83.80), 
    "Xe": ("Xenon", 54, 131.29), 
    "Rn": ("Radon", 86, 222)
}

def search_nonmetal(e):
    # Get the input FROM HTML
    Nonmetal1 = document.getElementById("nonmetal1").value.strip()
    
    # Retrieve information from dictionary
    result = nonmetals.get(Nonmetal1, ("DATA_NOT_FOUND", "---", "---"))
    
    # Display the result in HTML
    document.getElementById("code").innerText = Nonmetal1 if Nonmetal1 in nonmetals else "ERR"
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]







#DRILL2
# #List of the already accepted basketball varsity members

# varsity_members = ["Phoenix Hizon", "Erin Urbano", "Joaquin Castor", "Jarvis Joven", "Enzo Ruiz", "Rocky Saludez", "Miguel Santos"]

# #Clicking the button triggers this event to verify if the inputted name is in the given list

# def verify(event):

# # 2 & 3. Get input values and combine into one full name using f-strings

#     first_name = document.getElementById("first_name").value.strip()
#     last_name = document.getElementById("last_name").value.strip()
#     candidate_name = f"{first_name} {last_name}"

# #Using if/else statements to verify the inputted name and to set the message

#     if candidate_name in varsity_members:
#         message = f"Congratulations {candidate_name}! You are now part of the ICT club."
#         styling = "member-found"

#     else:
#         message = f"Sorry {candidate_name}, your name is not on the list."
#         styling = "member-not-found"

# #Display the text and apply CSS to it

#     result_div = document.getElementById("result")
#     result_div.innerText = message
#     result_div.className = styling
#     result_div.style.opacity = "1"

grade7 = {'Miguel Santos', 'Enzo Ruiz', 'Spencer Santillan'}
grade8 = {'Jeremiah Schumacher', 'Joaquin Castor', 'Gerthy Bausa'}
grade9 = {'Erin Urbano', 'Jarvis Joven', 'Rocky Saludez'}
grade10 = {'Phoenix Hizon', 'Eran Diaz', 'Carlos Borromeo'}

total_members = grade7 | grade8 | grade9 | grade10

number_members = (len(total_members))
display(number_members, target = 'total')

members_list = '<br>' + '<br>'.join(sorted(total_members))

display(members_list, target = 'normal')

def adding(event):

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = first_name + " " + last_name

    display(candidate_name, target = 'normal')

    updated = number_members + 1

    display(updated, target = 'total')









    