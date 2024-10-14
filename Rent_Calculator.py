#input we need from the user 
#Total rent
#Total food orderd for snacking 
#Electricity units spend 
#Charge per unit 
#persons living in room

#Output
#Total amount you have to pay is

rent=int(input("Enter your hostel/flat rent="))
food=int(input("Enter your amount of food ordered= "))
electricity_spend=int(input("Enter your total Electricity spend amount= "))
charge_per_unit=int(input("Enter the charge per unit= "))
persons_living_in_room=int(input("Enter the number of persons living in room/flat= "))

total_bill=electricity_spend *charge_per_unit
output=(rent +food + total_bill) //persons_living_in_room

print("Each person will pay", output)
