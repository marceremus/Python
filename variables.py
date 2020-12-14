#!/usr/bin/env python2

hello_int = 21
hello_bool = True
hello_tuple= (21,32)
hello_list = ["Hello", "ici", "c'est", "Python"]
hello_dict = {"first_name": "Robert", "last_name":"Dupont"}


print(hello_int)
print(hello_bool)
print(hello_tuple)
print(hello_list[0])
hello_list.append("Super")
print(hello_list[4])
print(hello_dict["first_name"] + " " + hello_dict["last_name"])

h_int = 0
h_str = "toto"

for v in hello_list:
    h_int += 1
    print(str(h_int) + "!")
    #print(h_int)

