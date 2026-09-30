with open("dati.txt","r") as f:
    for line in f:
        print(line.strip())
        
with open("dati2.txt","r") as f:
    for line in f:
        line_s=line.split(",")
        print(line_s)
        
with open("output.txt","w") as fw:
    fw.write("3")