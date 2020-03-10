import sys

digits_list = []
card_num = input('Please enter your card number here: ')


def input_validator():
    if len(card_num) == 8:
       for i in card_num:
            digits_list.append(int(i))
    else:
        print('enter 5 digits to check')


input_validator()

# double every second digit and if > 10 add the result
for i in range(1, len(digits_list), 2):
    digits_list[i] = digits_list[i] * 2
    if digits_list[i] >= 10:
        digits_list[i] = digits_list[i] % 10 + 1
print(digits_list)
total = sum(digits_list)
print(total)

if total % 10 != 0:
#   Grand_total = total // 10
 #  Grand_total *= 10

 print("This is not a valid card. Please a valid card")
else: print('Your card has been verified. Payment approved :)')



