def gb_to_mb(gb):
    return gb * 1024

def mb_to_gb(mb):
    return mb / 1024

def tb_to_gb(tb):
    return tb * 1024
while True:
   
    print("1) GB to MB  2) MB to GB 3) TB to GB 4) Exit")
    
    choice = input("Choose an option: ")

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid option. Choose 1-4.")
        continue    
    try:
        amount = float(input("Enter the amount: "))
    
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == "1":
        print(amount, "GB =", gb_to_mb(amount), "MB")

    elif choice == "2":
        print(amount, "MB =", mb_to_gb(amount), "GB")

    elif choice == "3":
        print(amount, "TB =", tb_to_gb(amount), "GB")