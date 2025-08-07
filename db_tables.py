# Database tables
from database import database_connection # DB Connection

# Connection module
connection = database_connection()
cursor = connection.cursor()

def user_table():
    '''USER TABLE FOR STORING PERSONAL INFO'''
    try:
        cursor.execute("""
                   CREATE TABLE IF NOT EXISTS USERS(
                       USER_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                       FIRST_NAME VARCHAR(50) NOT NULL,
                       LAST_NAME VARCHAR(50) NOT NULL,
                       USERNAME VARCHAR(50) NOT NULL,
                       EMAIL VARCHAR(100) NOT NULL
                   )
                   """)
        connection.commit()
        print("User Table Creation is Successfully")
        
    except Exception as e:
        print(f"ERROR: {e}")
        
def login_table():
    '''LOGIN DETAILS TABLE HANDLER'''
    try:
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS LOGIN(
                          LOGIN_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                           USERNAME VARCHAR(50) NOT NULL,
                           PASSWORD VARCHAR(300) NOT NULL
                       )
                       """)
        connection.commit()
        print("Login Table Creation is Successfully")
        
    except Exception as e:
        print(f"ERROR: {e}")
        
        
def otp_table():
    '''OTP STORING TABLE'''
    try:
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS OTP(
                          OTP_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                          OTP_CODE INT NOT NULL,
                          EMAIL VARCHAR(100) NOT NULL,
                          EXP_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       )
                       """)  
        connection.commit()
        print("OTP Table Creation is Successfully")
        
    except Exception as e:
        print(f"ERROR: {e}")
        