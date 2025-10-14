f = open("priyansh.txt", "w")

f1 = open("harry.txt", "r")

con = f1.read()

f.write(con)

f.close()
f1.close()
