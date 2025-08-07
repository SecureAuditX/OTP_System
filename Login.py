import bcrypt # hash password
import re  # regular expression check for password
from database import database_connection # Database connection
from otp_authenticate import generate_and_send_otp, verify_otp
import stdiomask # for password masking

connection = database_connection()
cursor = connection.cursor()


def sign_form():
    '''REGISTRATION PAGE'''
    try:
        print(">>>>>>>>>>>>>> REGISTER <<<<<<<<<<<<<<")
        print("Kindly provide the details below:")
        first_name = input("\nFIRST NAME: ").strip()
        if not first_name:
            print("First name cannot be empty")
            return sign_form()
    
        last_name = input("LAST NAME: ").strip()
        if not last_name:
            print("Last name cannot be empty")
            return sign_form()
    
        username = input("USERNAME: ").lower().strip()
        if not username:
            print("Username cannot be empty")
            return sign_form()
        
        email = input("EMAIL: ").strip()
        if not email:
            print("Email cannot be empty")
            return sign_form()
        
        # Email validation check
        def valid_email(email):
            email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            return re.match(email_pattern, email)
                
        if not valid_email(email):
            print("Invalid email, try again")
            return sign_form()
        
    
        password = stdiomask.getpass(prompt = "PASSWORD: ", mask = '*').strip()
        if not password:
            print("Confirm password cannot be empty")
            return sign_form()
    
        confirm_password = stdiomask.getpass(prompt = "CONFIRM PASSWORD: ", mask = '*').strip()
        if not confirm_password:
            print("Confirm password cannot be empty")
            return sign_form()
        
        if password != confirm_password:
            print("Password Mismatched, Try again!")
            return sign_form()
        
        # Password validation
        def secure_password(password):
            return (len(password) >= 8 and
                re.search(r"[A-Z]", password) and
                re.search(r"[a-z]", password) and
                re.search(r"[0-9]", password) and
                re.search(r"[@#$%&*!?]", password)
                )
        if not secure_password(password):
            print("Password is Weak!!!")
            return sign_form()
        
        # OTP generation and verification step
        generate_and_send_otp(email)
        
        # Ask user for the otp for verification
        entered_otp = input("Enter the OTP sent to your email: ").strip()
        # verify the otp
        if not verify_otp(email, entered_otp):
            print("OTP Verification Failed. Registration Not Completed.")
            return
        
        # Secure user password (hash)
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # inserting data into user table
        cursor.execute("""
                       INSERT INTO USERS (first_name, last_name, username, email)
                       VALUES (%s, %s, %s, %s)
                       """,(first_name, last_name, username, email))
        # inserting other data into login table
        cursor.execute("""
                       INSERT INTO LOGIN (username, password)
                       VALUES (%s, %s)
                       """, (username, hash_password))
        connection.commit()
        print("Registration Sucessful!")
        # Return Login Form after successfully registration
    
        return email
    except ValueError:
        print("Error Occured, try again")   
    except Exception as e:
        print(f"ERROR: {e}")    
        
def login_form():
    '''LOGIN OTP PAGE'''
    try:
        print(">>>>>>>>>>>>> LOGIN <<<<<<<<<<<<<")
        username = input("\nUSERNAME: ").lower().strip()
        password = stdiomask.getpass(prompt = "PASSWORD: ", mask = '*').strip()
        
        # Detecting & Preventing SQL Injection
        sqli_patterns = [
            r"(?i)or\s+1=1",
            r"(?i)union\s+select",
            r"(?i)drop\s+table",
            r"--",
            r";",
            r"'",
            r'"'
        ]
        def detect_sqli_and_kick_user(*inputs):
            """Once the attack is detected it will kick out the user (session will terminate)"""
            for user_input in inputs:
                for attack in sqli_patterns:
                    if re.search(attack, user_input):
                        print("\n[SECURITY ALERT] SQL Injection attempt detected!")
                        print("SESSION TERMINATED.")
                        return True
            return False
        # detect and terminate
        if detect_sqli_and_kick_user(username, password):
            return  # Exit the function
        
        # validating login details
        cursor.execute("""
                       SELECT PASSWORD FROM LOGIN 
                       WHERE USERNAME = %s
                       """, (username,))
        result = cursor.fetchone()
        if result:
            hashed_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                print("Login Successfully")
                print("\n    WELCOME BACK!!!")
        
            else:
                print("Invalid Credentials, try again")
                return login_form()
        else:
            print("User Not Found")
            return
        
    except Exception as e:
        print(f"Login Failed: {e}")   