trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = puzzles * 2.60
doll_price = dolls * 3
bear_price = bears * 4.10
minion_price = minions * 8.20
truck_price = trucks * 2

total_sum = puzzle_price + doll_price + bear_price + minion_price + truck_price

toy_count = puzzles + dolls + bears + minions + trucks
bonus = 0

if toy_count >= 50:
    bonus = total_sum * 0.25

bill = total_sum - bonus
rent = bill * 0.1
profit = bill - rent

if profit >= trip_price:
    trip_money = (profit - trip_price)
    print(f"Yes! {trip_money:.2f} lv left.")
if profit < trip_price:
    trip_money = abs(profit - trip_price)
    print(f"Not enough money! {trip_money:.2f} lv needed.")





