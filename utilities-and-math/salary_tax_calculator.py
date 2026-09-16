maxLowGross=10000
minHighGross=25000
maxHighGross=50000
lowRate=85/100  #low tax rate is %15
medRate=80/100   #medium tax rate is %20
highRate=75/100   #high tax rate is %25
lowCounter=0 
medCounter=0 
highCounter=0 
higherCounter=0 
totalLowGrossSalary=0
totalMedGrossSalary=0
totalHighGrossSalary=0
totalHigherGrossSalary=0
totalNetLowSalary=0
totalNetMedSalary=0
totalNetHighSalary=0
taxPaid=0
grossSalary= float(input("\nEnter Your Gross Salary ($): "))
#can be written like x=1  and  while x=='1':  grossSalary=float(input()) x=input("Do You Want to Continue (Yes:1/No:0))
while grossSalary not in (0,-9999999999):
    
    if grossSalary<=maxLowGross:
        netSalary= grossSalary*lowRate
        totalLowGrossSalary+=grossSalary
        totalNetLowSalary+=netSalary
        taxPaid += grossSalary-netSalary
        tax= grossSalary-netSalary
        lowCounter+=1
        print(f"Your Gross Salary: {grossSalary:.2f} \nYour Net Salary: {netSalary:.2f} \nYou're Paying {tax:.2f} Income Tax to State.")
        
    elif maxLowGross<grossSalary<minHighGross:
        netSalary= grossSalary*medRate
        totalNetMedSalary+=netSalary
        totalMedGrossSalary+=grossSalary
        taxPaid += grossSalary-netSalary
        tax= grossSalary-netSalary
        medCounter+=1
        print(f"Your Gross Salary: {grossSalary:.2f} \nYour Net Salary: {netSalary:.2f} \nYou're Paying {tax:.2f} Income Tax to State.")
    
    elif minHighGross<=grossSalary<=maxHighGross:
        netSalary= grossSalary*highRate
        totalNetHighSalary+=netSalary
        totalHighGrossSalary+=grossSalary
        taxPaid += grossSalary-netSalary
        tax= grossSalary-netSalary
        highCounter+=1
        print(f"Your Gross Salary: {grossSalary:.2f} \nYour Net Salary: {netSalary:.2f} \nYou're Paying {tax:.2f} Income Tax to State.")
        
    elif maxHighGross<grossSalary:
        netSalary= grossSalary*highRate
        totalHighGrossSalary+=grossSalary
        totalHigherGrossSalary+=grossSalary
        totalNetHighSalary+=netSalary
        taxPaid += grossSalary-netSalary
        tax= grossSalary-netSalary
        highCounter+=1
        higherCounter+=1
        print(f"Your Gross Salary: {grossSalary:.2f} \nYour Net Salary: {netSalary:.2f} \nYou're Paying {tax:.2f} Income Tax to State.")
   
    grossSalary= float(input("\nEnter Your Gross Salary ($): "))


perHigher= higherCounter/highCounter*100 #Percentage of representatives with more than  50k$ salary
totalGrossSalary= totalHighGrossSalary+totalMedGrossSalary+totalLowGrossSalary
totalNetSalary= totalNetHighSalary+totalNetLowSalary+totalNetMedSalary
totalRep= lowCounter+medCounter+highCounter #Number of representatives
avgNet= totalNetSalary/totalRep
perTax= taxPaid/totalGrossSalary*100  #Percentage Of Taxes Paid to Total Gross Salary
print("\n\n\n\t\t\t\t*****RESULTS*****\n\n")
print(f"Number of Sales Representatives With Low Gross Salary: {lowCounter}")
print(f"Number of Sales Representatives With Medium Gross Salary: {medCounter}")
print(f"Number of Sales Representatives With High Gross Salary: {highCounter}")
print(f"Number of Sales Representatives With More Than 50K$  Gross Salary: {higherCounter} ")
print(f"Percentage of Representatives Which Gets More Than 50K$ Gross Salary: %{perHigher:.2f}")
print(f"Average of All Representatives' Net Salary ($): {avgNet:.2f}")
print(f"Total Amount of Income Tax to be Paid to State: {taxPaid:.2f}$ \nPercentage of Taxes Amount to Total Gross Salary: %{perTax:.2f}")

#all of this can be written in one print but to read it easier i wrote with more prints
            