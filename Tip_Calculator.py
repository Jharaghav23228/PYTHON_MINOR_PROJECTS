print("WELCOME TO TIP CALCULATOR: ")
bill=float(input("What is your total bill?"))
tip=int(input("How much tip would you like to give?"))
people=int(input("How many people would you like to split?"))
bill_with_tip= bill+tip
print("Your bill with tip is :"+ str(bill_with_tip))
split= (bill+tip)/people
print("Each shoud give "+str(split)+" rupees")