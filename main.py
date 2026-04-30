# So'z top oyni'
# Komputer o'ylaydi biz topamiz

import random

sozlar = [
    "olma","suv","non", "quyosh","oy","yulduz","daraxt","gul","qush","mushuk","it","baliq","ot",
    "ona","ota","aka","opa","uka","singil","do'st","ustoz","o'quvchi","odam",
    "maktab","sinf","daftar","dars","yozuv","rasm","rang","qora","oq","qizil",
    "ko'k","yashil","sariq","katta","kichik","uzun","qisqa","tez","sekin","yaxshi",
    "yomon","yangi","eski","issiq","sovuq","och","to'q","kulmoq","yig'lamoq","yurmoq",
    "yugurmoq","o'tirish","turish","ichmoq","yemoq","ko'rmoq","eshitmoq","gapirmoq","o'qimoq","yozmoq",
    "bor","yo'q","ha","yo'q","bugun","kecha","ertaga","vaqt","kun","tun",
    "ertalab","kechqurun","hozir","keyin","oldin","ustida","ichida","yonida","bilan","uchun",
    "men","sen","u","biz","siz","ular","nima","qayer","qachon","qanday"
]

taxmin=0
print("So'z topish o'ynini o'ynaymiz,men bir so'z o'ylayman siz esa topishga xarakat qiling!😊")
input("👉Boshlash uchun Enter tugmasini bosing...")
soz = random.choice(sozlar)
print(soz)
while True:

    f_soz = input(f"Men so'z oyladim topishga xarakat qilip ko'riing😉:")
    taxmin = taxmin + 1
    if soz != f_soz:
        print("Xato!😊Yana urinip ko'ring")

    elif soz==f_soz:
        print(f"TABRIKLAYMAN!🎉 siz {soz.upper()} so'zini {taxmin}ta urinishda topdingiz👏")
        break

