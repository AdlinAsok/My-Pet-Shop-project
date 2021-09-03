item = {1: ["Cat food", 101.25, 2.5],
        2: ["Dog food", 303.75, 5],
        3: ["Cat toy", 10, 10],
        4: ["Dog toy", 50, 1],
        5: ["Dog leash", 1000, 3]}
print("How many items", end=" ")
TotalItems = int(input())
Totalprice = 0
for i in range(TotalItems):
    print("Enter the item no:", end=" ")
    Itemno = int(input())
    print("Enter the Quantity:", end=" ")
    Quantity = float(input())
    product = []
    product = item[Itemno]
    Price = (product[1]*Quantity)+((product[1]*product[2])/100)
    Price = round(Price,2)
    print("Price of", product[0], Price)
    Totalprice = Totalprice + Price
print("Please pay : ", Totalprice)
