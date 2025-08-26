import sys
import time
import random


def createFiles():
  with open("accounts.txt","w",encoding="utf-8"):
    continue

def exit():
  print("  Çıkış yapılıyor ...")
  time.sleep(3)
  sys.exit()

def register():
  name = input("  İsminizi giriniz (tam isim)  >> ")
  date = int(input("  Doğum yılınızı giriniz  >> "))
  age = 2025 - date
  if age < 18 :
    print("  18 yaşından küçük olduğunuz için hesap oluşturulamıyor .")
    exit()
  email = input("  Eposta adresinizi giriniz  >> ")
  while True :
    passw1 = input("  Oluşturmak istediğiniz şifrenizi giriniz  >> ")
    passw2 = input("  Tekrar giriniz  >> ")
    if passw1 == passw2 :
      print("  Şifreniz başarıyla oluşturuldu.")
      return True
    else:
      x = input("  Girdiğiniz şifreler uyuşmuyor . Tekrar deneyiniz veya çıkış yapmak istiyorsanız exit yazın .")
      if x == "exit" :
        exit()
      else:
        continue
    


def login():
  pass

def adminlogin():
  pass




print("by heqoN".center(100,"-")
print("  Banka sistemi projeme hoşgeldiniz.")
order1 = input("SEÇENEKLER".center(25,"*")+"\n\n   Kayıt ol -1\n  Giriş yap -2\n Çıkış yap -3\n  Admin girişi  -4\n\n   >>> ")
if order1 == "1" :
  register()
elif order1 == "2" :
  login()
elif order1 == "3" :
  exit()
elif order1 == "4" :
  adminlogin()
else :
  print("  Bir hata oluştu.")
  exit()
