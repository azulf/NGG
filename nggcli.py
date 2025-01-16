import random
import os
import sys
import argparse

def main() :
    if len(sys.argv) < 2:
        print("Selamat datang di NGG (Number Guessing Game)")
        print("Number Guessing Game adalah permainan menggunakan CLI")
        print("Kamu akan disuruh untuk menebak angka yang dipikirkan oleh program")
        print("Angka yang diberikan berkisar antara 1 - 100")
        print("Kamu memiliki 5 kesempatan untuk menebak")
    angka = saving_number()
    # print(angka) # for debug
    diffy = int(input("""Pilih Kesulitan 
          1. Hard   = 3  chance
          2. Medium = 5  chance
          3. Easy   = 10 chance
          """))
    kesempatan = difficulty_option(diffy)
    angka_tebakan = int(input("Masukkan Angka : "))

    while angka != angka_tebakan and kesempatan > 1 :
        kesempatan -= 1
        if angka > angka_tebakan :
            print("Angka kamu lebih kecil !")
        elif angka < angka_tebakan :
            print("Angka kamu lebih besar !")
        print("Salah ! ")
        print(f"Kesempatan Kamu tinggal : {kesempatan}")
        angka_tebakan = int(input("Masukkan Angka : "))
    if angka == angka_tebakan :
        print("Congrats kamu berhasil menebaknya ! ")
    else :
        print("Kamu kalah kesempatan kamu sudah habis !")
        print(f"Angka yang harus ditebak adalah {angka}")
    
    
# saving number that should be guessed
def saving_number() :
    number = random.randint(1, 100)
    return number

# option for difficulty 
def difficulty_option(diffy) :
    hard = 3
    medium = 5
    easy = 10

    if  diffy == 'hard' or diffy == 1 :
        diffy = hard
    elif diffy == 'medium' or diffy == 2 :
         diffy = medium
    elif diffy == 'easy' or diffy == 3 :
         diffy = easy

    return diffy

if __name__ == '__main__':
    main()
    
       