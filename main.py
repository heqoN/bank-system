import sys
import time

def createFiles():
  pass

def exit():
  print("  Çıkış yapılıyor ...")
  time.sleep(3)
  sys.exit()

def register():
  pass

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
