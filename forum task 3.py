week = ("sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
sales = []

for days in week:
    money = int(input(f"enter sales for {days}"))
    while money < 0:
        money = int(input(f"Input was invalid. Re-enter the sales for {days}"))
    sales.append(money)
totalsales = sum(sales)
maximumsale = max(sales)
minumumsale = min(sales)
print(f"the total sales is ${totalsales:,d}.00\nthe maximum sale amount was ${maximumsale:,d}.00 and the minimum sale amount was ${minumumsale:,d}.00")
