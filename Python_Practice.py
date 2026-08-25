total_sales = 0
for Employee in range(1, 6):
    sale = float(input(f"Enter sale amount for employees{Employee} in (Rs.) :"))
    if sale <= 50000:
        tax = sale * 0.05
    elif sale <= 100000:
        tax = sale * 0.10
    else:
        tax = sale * 0.15
    print(f"Employee :{Employee}") 
    print(f"Sale Amount Rs: {sale}")
    print(f"Tax Amount Rs :{tax}")
    print("-"* 30)
    total_sales += sale
    average_sale = total_sales / 5
    print("Final Result: ")
    print(f"Total sale :{total_sales}")  
    print(f"Average sale : {average_sale}")
