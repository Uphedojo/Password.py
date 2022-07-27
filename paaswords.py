from cryptography.fernet import  Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)

write_key()

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("password.txt","r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print(f"User: {user} | Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account Name: ")
    pwd = input("Passsword: ")
    with open("password.txt","a") as file:
        file.write(f"{name} | {fer.encrypt(pwd.encode()).decode()} \n")
    
while True:
    mode = input("Would you like to add a new Password or view existing Password--(VIEW/ADD) or type 'Q' to quit: ").upper()
    if mode == "Q":
        break
    elif mode == "ADD":
        add()
    elif mode == "VIEW":
        view()
    else:
        print("You did not type a valid option")
        continue


