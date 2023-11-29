def main(tuple1):
    if isinstance(tuple1, tuple):
        return tuple1[0]
    else:
        # agar kiritilgan ma'lumot tuple bo'lmasa, xatolik chiqarish
        raise TypeError("Kiritilgan ma'lumot tuple bo'lishi kerak")
# tuple ni o'zgaruvchiga saqlash
tuple1 = ('kd', 2, 3, 4, 5)
# funksiyani chaqirish va natijani chop etish
print(main(tuple1))
