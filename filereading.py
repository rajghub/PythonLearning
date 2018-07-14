f = open("demofile.html", "r")
for x in f:
    print(x)

b = open("demofile.html", "a")
b.write("\n Its a new line")

c = open("demofile.html", "r")
for x in c:
    print(x)

b.write("\n Its another line")
for x in c:
    print(x)