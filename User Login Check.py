username = 'admin'
password = '1234'

uname = input("Enter Username :")
upass = input("Enter Password: ")

if(uname == username and upass == password):
    print(f"Hello {uname}! Login Successful!")
else:
    print("Invalid Credentials")