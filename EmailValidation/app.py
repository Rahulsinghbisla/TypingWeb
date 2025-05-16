email = input("Enter your email :")
if len(email) >= 6:
    if ("@" in email) and (email.count("@")==1):
        if (email[-3]==".") ^ (email[-4]=="."):
            print("Correct")
        else:
            print("Wrong type 3")
    else:
        print("Wrong Email type 2")
else:
    print("Wrong Email type 1")
print(email[-3])