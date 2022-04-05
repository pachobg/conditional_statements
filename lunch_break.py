from math import floor, ceil

serial_name = input()
episode_duration = int(input())
lunch_time = int(input())

eat_time = lunch_time / 8
rest_time = lunch_time / 4

time_left = lunch_time - (eat_time + rest_time)

if time_left >= episode_duration:
    free_min = time_left - episode_duration
    print(f"You have enough time to watch {serial_name} and left with {ceil(free_min)} minutes free time.")
else:
    needed_min = episode_duration - time_left
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(needed_min)} more minutes.")
