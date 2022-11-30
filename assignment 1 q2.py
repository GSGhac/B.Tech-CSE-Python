#Program to compute income tax
#Taking user input for parameters
gross_income=int(input("Please enter gross input: "))
dependents=int(input("Please enter number of dependents: "))
#calculating taxable income
taxable_income= gross_income - 10000 - (3000*dependents)
#Calculating tax amount
tax_amount=0.2*taxable_income
#Displaying output using print
print("Income tax amount to ","$", tax_amount, sep="")
