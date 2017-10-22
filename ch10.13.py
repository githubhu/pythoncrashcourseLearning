import json

def get_new_username():
    username=input("What's your name? ")
    filename="username.json"
    with open(filename,"w") as f_obj:
        json.dump(username,f_obj)
    return username
def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except IOError:
        return None
    else:
        return username



def greet_user():
    username=get_stored_username()
    if username:
        correct=input("Are you " + username + " ? ")
        if correct=="y" or correct =="Y":
            print ("Welcome back " + username)
            return
    username =get_new_username()
    print("We'll remember you when you are back " + username + "!")

greet_user()
