import json

usernumber= input("What' your favorite number ? ")
filename="favoritenumber.json"

with open(filename,"w") as f_obj:
    number=json.dump(usernumber,f_obj)

with open(filename) as f_obj:
    number=json.load(f_obj)
    print("I know your favorite numbers!! It's " + number)


