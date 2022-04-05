old_record = float(input())
meters = float(input())
sec_per_meter = float(input())

slowdown = meters // 15 * 12.5
total_time = meters * sec_per_meter + slowdown

if total_time < old_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    fail_time = total_time - old_record
    print(f"No, he failed! He was {fail_time:.2f} seconds slower.")
