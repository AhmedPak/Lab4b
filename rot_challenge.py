
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#"0","1","2","3","4","5","6","7","8","9"]

plain_text = "3ncrypt 2 this Text"

rot = 13

cipher = ""

for i in range(len(plain_text)):
    if plain_text[i] == " ":
        cipher = cipher + " "
        #do not rotate digits
    elif plain_text[i].isdigit():
        cipher = cipher + plain_text[i]

    for j in range(len(alphabet)):
        if plain_text[i] == alphabet[j]:
            if j + rot > 25:
                diff = (j + rot) - 25
                cipher = cipher + (alphabet[diff - 1])
            else:
                cipher = cipher + (alphabet[j + rot])
print("")
print("Cipher text is " + cipher)
