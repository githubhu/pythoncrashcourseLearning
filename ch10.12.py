import json

filename="favoritenumber.json"
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except IOError:
    with open(filename,"w") as f_obj:
        number=input("What' your favorite number ? ")
        json.dump(number,f_obj)
        print("get your favorite number" + number)
else:
    print("I know your favorite numbers!! It's " + number)
