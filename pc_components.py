budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_card_price = video_cards * 250
processor_price = processors * video_card_price * 0.35
ram_memory_price = ram_memory * video_card_price * 0.1

discount = 0

total = video_card_price + processor_price + ram_memory_price

if video_cards > processors:
    discount = total * 0.15

final_bill = total - discount
if budget >= final_bill:
    money_left = budget - final_bill
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = final_bill - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")