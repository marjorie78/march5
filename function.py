def greeting(name, sex):
    if sex=="m":
        prefix="Mr."
    elif sex=="f":
        prefix="Mrs."
    else:
        prefix=""
    print ("Hello {} {}, how are you".format(prefix,name))
    print("My name is Bogdan")
    print("It is my pleasure")
person=input("Who do you want to greet?")
sex=input("sex?")
greeting(person,sex)
print ("what if I want to greet someone else")
greeting ("Bob", "m")
greeting("Fluffy","dog")


#homework

fp=open("harrypotter.txt", "r")
punct = ".,!?-"
for line in fp:
    for p in punct:
        line=line.replace(p,"")
        #call the split method on line
    if x in list: