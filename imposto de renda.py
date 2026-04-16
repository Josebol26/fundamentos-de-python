income = float(input("Entre com os rendimentos anuais "))
print(income < 85528)
if income <= 85528:
 tax = income * 0.18 - 556.02
else:
 tax = 14839.02 + 0.32 * (income - 85528)
 tax = round(tax, 2)
print("A taxa é:", tax, "thalers") 
 