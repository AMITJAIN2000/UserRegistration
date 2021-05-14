import csv
data={"UserName":["amit","prakhar","praveen"]
      ,"password":["1","2","3"],
      "email":["aj@gmail.com","ps@gmail.com","psv@gmail.com"],
      }

with open("4.csv", mode="w", newline="") as f:
    read = csv.writer(f, delimiter=",")
    
    read = csv.writer(f, delimiter=",")
    for i in zip(data['UserName'], data['password'], data['email']):
        read.writerow(i)

def Userinfo():
    Name = input("enter the Name:-")
    Password = input("enter the password:-")
    Email = input("enter the email:-")
    return Name,Password,Email

def newUser():
    Name = input("enter the Name:-")
    Password = input("enter the password:-")
    Email = input("enter the email:-")

    lst=[Name,Password,Email]
    with open("4.csv", mode="a", newline="") as f:
        r = csv.writer(f, delimiter=",")
        r.writerow(lst)
    print("New Registration is confirmed")

def login(attempt=3):
    Name,Password,Email=Userinfo()

    with open("4.csv", mode="r") as f:
        count=0
        for i in f:
            a=Name+","+Password+","+Email+"\n"
            if a==i:
                print(f"Welcome {Name} you are logged in")
                count+=1
                break
        if count==0:
            if attempt==1:
                print("Your user id is temperary blocked!")
            else:
                attempt-=1
                # print(attempt)
                print(f"attempt left only {attempt} please put correct information")
                login(attempt)
def logout():
    print("Succesfully logout")




x=1
while x==1:
    print(" 1.SignUp""\n"
          " 2.Login""\n"
          " 3.Logout""\n")

    try:
        take = int(input("enter what you want to do operation in above:-"))
        if take==1:
            newUser()

        elif take==2:
            login()

        elif take==3:
            logout()

        else:
            print("please select correct one")
    except:
        print("please select one")

    x=int(input("press 1 to perform more action\n"))
print("Thank you")
print("\U0001f600")