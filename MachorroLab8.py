#Gary Machorro
#8/24/17
#Lab8:temp conversion
try:
    infile=open("C:\\Users\\gfmachorro\\Downloads\\tempF.txt","r")
    outfile=open("C:\\Users\\gfmachorro\\Downloads\\tempsC.txt","w")
    tempList=[]
    floatList=[]
    stringList=[]
    for line in infile:
        line=line.rsplit()
        tempList=tempList+line
    for i in range(len(tempList)):
        temp=float(tempList[i])
        floatList.append(temp)
    print(floatList)
    for j in range(len(floatList)):
        tempC=((floatList[j])-32)*(5/9)
        tempC=round(tempC,2)
        stringList.append(tempC)
    for k in range(len(stringList)):
        Ctemps=str(stringList[k])
        outfile.write(Ctemps)
        outfile.write("")
    infile.close()
    outfile.close()
except IOError:
    print("File not found.")
    


