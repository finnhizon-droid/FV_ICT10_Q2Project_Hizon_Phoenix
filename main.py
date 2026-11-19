from pyscript import document, display




# - SEATWORK 1 - CLUB MEMBER CHECKER - 


varsity_members = [
    "Phoenix Hizon",
    "Erin Urbano",
    "Joaquin Castor",
    "Jarvis Joven",
    "Enzo Ruiz",
    "Rocky Saludez",
    "Miguel Santos",
]

def verify(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = f"{first_name} {last_name}".strip()

    status = {
        True: (f"Congratulations {candidate_name}! You are now part of the ICT club.",
            "member-found",),
        False: (f"Sorry {candidate_name}, your name is not on the list.",
            "member-not-found",),
    }

    is_member = candidate_name in varsity_members
    message, styling = status[is_member]

    result_div = document.getElementById("result")
    result_div.innerText = message
    result_div.className = styling
    result_div.style.opacity = "1"




# - SKILLS TEST - ELEMENT CHECKER -

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
    Nonmetal1 = document.getElementById("nonmetal1").value.strip().capitalize()
    
    # Retrieve information from dictionary
    result = nonmetals.get(Nonmetal1, ("DATA_NOT_FOUND", "---", "---"))
    
    # Display the result in HTML
    document.getElementById("code").innerText = Nonmetal1 if Nonmetal1 in nonmetals else "ERR"
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]







# - DRILL 2 - SCHOOL CLUB MEMBERS -
grade7 = {'Miguel Santos', 'Enzo Ruiz', 'Spencer Santillan'}
grade8 = {'Jeremiah Schumacher', 'Joaquin Castor', 'Gerthy Bausa'}
grade9 = {'Erin Urbano', 'Jarvis Joven', 'Rocky Saludez'}
grade10 = {'Phoenix Hizon', 'Eran Diaz', 'Carlos Borromeo'}

total_members = grade7 | grade8 | grade9 | grade10

def fixed_members():
    document.getElementById("normal").innerHTML = "<br>".join(sorted(total_members))
    document.getElementById("total").innerHTML = f"Total Members: {len(total_members)}"

fixed_members()

def adding(event):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    name = f"{first_name} {last_name}".strip()

    total_members.add(name)
    fixed_members()
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""








    
