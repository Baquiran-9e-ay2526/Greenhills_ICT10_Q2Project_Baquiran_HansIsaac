# Candidate Verification Checker
from pyscript import document, display, when

@when("click", "#submit-btn")
def check_user(event):
    document.getElementById('output').innerHTML = ''

    first_name = document.getElementById('student_name').value.strip()
    last_name = document.getElementById('surname').value.strip()
    
    candidate_name = f"{first_name} {last_name}".title()

    cocc_members = ["Hans Baquiran", "Zarina Perez", "Nathan Bautista", "Maryam Ledesma", "Rico Gozum", "Osrhi Gonzales", "Zoe Reyes", "Ethan Valerio", "Aiva Suson", "David Valeriano", "Renzo Madrono", "Thea Correa", "Ramon Santiago", "Jamielle Orduna", "Reign Macachor"]

    candidate_checker = candidate_name in cocc_members

    display_message = (f"Sorry {candidate_name}, you are not part of the COCC Club.",f"Congratulations {candidate_name}! You are now part of the COCC club.")

    display(display_message[candidate_checker], target='output', append=False)