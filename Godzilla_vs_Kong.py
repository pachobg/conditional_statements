budget = float(input())
actors = int(input())
costumes = float(input())

decor = budget * 0.1
costume_price = costumes * actors
discount = 0

if actors >= 150:
    discount = costume_price * 0.1

money_spend = decor + costume_price - discount

if money_spend > budget:
    needed_money = money_spend - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
if money_spend <= budget:
    needed_money = abs(money_spend - budget)
    print("Action!")
    print(f"Wingard starts filming with {needed_money:.2f} leva left.")