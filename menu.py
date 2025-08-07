from Login import sign_form, login_form


def menu():
    print("Hello! And Welcome")
    while True:
        print("\n1. SIGN_UP")
        print("2. LOGIN")
        print("3. EXIT")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            sign_form()
        elif choice == 2:
            login_form()
            break
        elif choice == 3:
            print("Good Bye.")
            exit()
        else:
            print("Invalid input, Try again")
            
menu()