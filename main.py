# So'z top oyni'
# Komputer o'ylaydi biz topamiz

import random

sozlar = ["olma","suv","non", "quyosh","oy","yulduz","daraxt","gul","qush","mushuk","it","baliq","ot"]

# taxmin=0
# print("So'z topish o'ynini o'ynaymiz,men bir so'z o'ylayman siz esa topishga xarakat qiling!😊")
# input("👉Boshlash uchun Enter tugmasini bosing...")
# soz = random.choice(sozlar)
# print(soz)
# while True:
#
#     f_soz = input(f"Men so'z oyladim topishga xarakat qilip ko'riing😉:")
#     taxmin = taxmin + 1
#     if soz != f_soz:
#         print("Xato!😊Yana urinip ko'ring")
#
#     elif soz==f_soz:
#         print(f"TABRIKLAYMAN!🎉 siz {soz.upper()} so'zini {taxmin}ta urinishda topdingiz👏")
#         break

# Biz o'ylaymiz koputer esa topadi
taxmin_k=0
print("So'z topish o'ynini o'ynaymiz,siz bir so'z o'ylaysiz men esa topishga xarakat qilaman!😊")

input("👉Boshlash uchun Enter tugmasini bosing...")

while True:
    taxmin_k=taxmin_k+1
    k_soz = random.choice(sozlar)
    javob=input(f"Siz '{k_soz}' so'zini o'ydadingiz, T(tog'ri),F(noto'g'ri)")
    if javob=="T":
        print(f"Men {taxmin_k} ta urinishda topdim!")
        break
    elif javob=="F":
        print("Xato yana urinip ko'ring!")
