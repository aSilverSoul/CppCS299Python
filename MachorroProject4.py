#Gary Machorro
#8/25/17
#Project 4:Lists and file input/output

from tkinter.filedialog import askopenfilename, asksaveasfilename
## gets the temperature and adds them to a list
# @return the temperature list
#
def getTemp():
    stringTempList=[]
    tempList=[]
    infileName = askopenfilename()
    infile = open(infileName, "r")
    for line in infile:
        line=line.split()
        stringTempList=stringTempList+line
    for i in range(len(stringTempList)):
        temp=float(stringTempList[i])
        tempList.append(temp)
    return tempList

    infile.close()
## gets the highest value in the list
# @param tempList the list of values
# @return the highest value
def getHighest(tempList):
    highest=max(tempList)
    return highest
## gets the lowest value in the list
# @param tempList the list of values
# @return the lowest value
def getLowest(tempList):
    lowest=min(tempList)
    return lowest
## gets the average value in the list
# @param tempList the list of values
# @return the average value
def getAverage(tempList):
    tempSum=sum(tempList)
    listLength=len(tempList)
    tempAvg=tempSum/listLength
    return tempAvg
##
#This program allows the user to choose input and output file to compute
#the max,min,and average
#
def main():
    tempList=getTemp()
    highest=str(getHighest(tempList))
    lowest=str(getLowest(tempList))
    average=round(getAverage(tempList),2)
    tempAvg=str(average)
    

    outfileName = asksaveasfilename()
    outfile = open(outfileName, "w")
    outfile.write("highest temperature:")
    outfile.write(highest)
    outfile.write("\nlowest temperature:")
    outfile.write(lowest)
    outfile.write("\naverage temperature:")
    outfile.write(tempAvg)
    outfile.close()
    
main()

