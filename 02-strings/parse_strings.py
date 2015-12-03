# my_name = "katherine"
# print list(my_name)

# numbers = "1,2,3,4,5"
# numbers = numbers.split(",")
# print numbers

# my_fish = "one fish two fish red fish blue fish"
# my_fish = my_fish.split("fish")
# print my_fish

# str = "item:apples, quantity:4, price: 1.50\n"
# def calculate_bil(str_input):
# 	split_str = str_input.split(",")
# 	quantity = float(split_str[1].split(":")[1])
# 	price = float(split_str[2].split(":")[1])
# 	return quantity * price
# print calculate_bil(str)

items = ["item:apples, quantity:4, price:1.50\n", "item:pears, quantity:5, price:2.00\n", "item:cereal, quantity:1, price:4.49\n"]
def calculate_bill(item_input):
	bill = 0
	for string in item_input:
		split_str = string.split(",")
		quantity = float(split_str[1].split(":")[1])
		price = float(split_str[2].split(":")[1])
		bill += quantity * price
	return bill 
print calculate_bill(items)