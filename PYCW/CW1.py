import random

# Store juice volumes
apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

# Calculate total volume
total_volume = apple_juice + orange_juice + grape_juice

# Print total volume
print("Total volume of juice sold:", total_volume)

# Convert total volume to integer and print
total_volume_int = int(total_volume)
print("Total volume as integer:", total_volume_int)

# Convert total volume to string and print with a message
total_volume_str = str(total_volume)
print("The total juice sold today is " + total_volume_str + " liters.")

# Add a random bonus between 5 and 10 liters
bonus_liters = random.randint(5, 10)
final_total = total_volume + bonus_liters

# Print final total
print("Bonus liters added:", bonus_liters)
print("Final total volume including bonus:", final_total)

