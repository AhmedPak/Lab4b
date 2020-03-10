import sys
from random import Random

vendor_dict = {"34": "American Express", "37": "American Express", "62": "China UnionPay", "3528": "JCB", "6304": "Laser", "6759": "Master UK", "50": "Maestro", "5019":"Dankort", "4571": "Dankort Co-branded", "2200": "MIR", "2221": "Mastercard", "51": "Mastercard", "6334": "Solo", "4903": "Switch", "4": "Visa", "1":"UATP"}

card_num = input("enter first two digits of your card number: ")
if card_num in vendor_dict:
    print(vendor_dict.get(card_num))
else: print('enter a valid card number')
print()
vendor_list = ["American Express", "Master Card", "Visa Debit", " China UnionPay", " Switch", " Solo"]
print("Vendors are: ", vendor_list)
select = input("select your vendor: ")
if select in vendor_list:
    print('your selection is :' + select)
else: print("Enter a valid vendor")
mastercardPrefixList = [
        ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]
generator = Random()


def credit_card_number(num, length):
    result = []
    while len(result < 16)
        result.append()
    pass


mastercard = credit_card_number (generator, mastercardPrefixList)

