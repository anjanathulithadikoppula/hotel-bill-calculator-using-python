print("welcome to my first code, here you can calculate bill of your food with tip addon!! happy food!!")

currency = input("\nenter the currency you are using:-")
bill_amount = input("\nenter the bill amount:-")
bill=float(bill_amount)
people = input("\nenter how many people are going to share the bill to pay:-")
ppl=int(people)
tip_select = input("\nhow much percent of the bill you want to tip? 10, 12 or 15?:-")
tip = int(tip_select)

tip_addon = (bill * (tip/100))
final_bill = bill + tip_addon
per_person = (final_bill / ppl)

message = f'\nAfter {tip} percent of tip add-on\nthe total bill is {round(final_bill, 3)} {currency}\neach person needs to pay {round(per_person, 3)} {currency}'

print("\n"+message+"\n")