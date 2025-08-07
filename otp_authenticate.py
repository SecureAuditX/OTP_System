# OTP verification Logic
import pyotp # OTP module
import hashlib # hashing otp lib
import time 
from database import database_connection
import smtplib # email protocol
from email.mime.text import MIMEText # creating the email body as plaintext
from email.mime.multipart import MIMEMultipart # creating email with multiple part (subject, body, etc)
from configure import Company_email, Company_email_password
from datetime import datetime

# DB connection
connection = database_connection()
cursor = connection.cursor()

def send_email(to_email, subject, body):
    '''SENDING EMAIL TO USER '''
    sender_email = Company_email
    sender_password = Company_email_password
    
    # set-up MIME for email
    message = MIMEMultipart()
    message["from"] = sender_email
    message["to"] = to_email
    message["subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    try:
        # set-up SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() # Starting TLS (encryption of secure email transmission)
        server.login(sender_email, sender_password) # login to sender Gmail Account
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()
        print(f"\nWe Have send otp verification to {to_email}, kindly check")
        
    except Exception as e:
        print(f"ERROR: {e}")


def generate_and_send_otp(user_email):
    '''GENERATING OTP CODE + SENDING THE OTP'''
    otp_code = pyotp.random_base32()[:6] # generating otp #[:6] = shorten if needed
    
    # Expiry time (5 minutes from now)
    expiration_timestamp = int(time.time()) + 300  # 5 mins from now
    expiration_time = datetime.fromtimestamp(expiration_timestamp)
    formatted_time = expiration_time.strftime('%Y-%m-%d %H:%M:%S')
    
    hashed_otp = hashlib.sha256(otp_code.encode()).hexdigest() # Hash the otp and stored in 
    
    # delete already expired otp from the db
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
        DELETE FROM otp WHERE EXP_TIME < %s
    """, (current_time,))
    
    cursor.execute("""
                   INSERT INTO OTP(otp_code, email, exp_time)
                   VALUES (%s, %s, %s)
                   """, (hashed_otp, user_email, formatted_time))
    
    connection.commit()
    
    # send otp to user's email
    send_email(user_email, "Your OTP Code", f"Your OTP is: {otp_code}. It will expire in 5minutes.")
    print(f"OTP send to {user_email}, Expiration time: {formatted_time}")


def verify_otp(user_email, entered_otp):
    # Retrieve stored otp from the database
    cursor.execute("""
                   SELECT OTP_CODE, EXP_TIME FROM OTP
                   WHERE EMAIL = %s ORDER BY EXP_TIME DESC LIMIT 1
                   """,(user_email,))
    result = cursor.fetchone()
    if result:
        stored_hashed_otp, stored_expiration_time = result
        
        # current time as datetime
        current_time = datetime.now()
        # Checking if otp expired
        if current_time > stored_expiration_time:
            print("OTP Expired! Try again")
            return False
        # Hash and compared the otp
        hashed_entered_otp = hashlib.sha256(entered_otp.encode()).hexdigest()
        
        if hashed_entered_otp == stored_hashed_otp:
            print("OTP Verified Successfully")
            return True
        else:
            print("Invalid OTP")
            return False
    else:
        print("No OTP found for this email")
        return False