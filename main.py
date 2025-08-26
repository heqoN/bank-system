import sys
import time
import random
import os


def createFiles():
  if not os.path.exists("accounts.txt"):   
    with open("accounts.txt", "w", encoding="utf-8"):
      pass
  if not os.path.exists("money.txt"):   
    with open("money.txt", "w", encoding="utf-8"):
      pass
            
  if not os.path.exists("logs.txt"):   
    with open("logs.txt", "w", encoding="utf-8"):
      pass

createFiles()

def shutdown():
  print("  Çıkış yapılıyor ...")
  time.sleep(3)
  sys.exit()


def register():
  name = input("  İsminizi giriniz (tam isim)  >> ")
  date = int(input("  Doğum yılınızı giriniz  >> "))
  age = 2025 - date
  if age < 18 :
    print("  18 yaşından küçük olduğunuz için hesap oluşturulamıyor .")
    shutdown()
  email = input("  Eposta adresinizi giriniz  >> ")
  try:
        with open("accounts.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) != 5:
                    continue
                _, _, storedemail, _, _ = parts
                if email == storedemail:
                    print("  Bu eposta adresi ile zaten kayıt yapılmış!")
                    return False
  except Exception as e:
    print(f"Dosya okuma hatası: {e}")
    return False
        
        

  iban = random.randint(10**15,10**16-1)
  while True :
    passw1 = input("  Oluşturmak istediğiniz şifrenizi giriniz  >> ")
    passw2 = input("  Tekrar giriniz  >> ")
    if passw1 == passw2 :
      print("  Başarıyla kayıt oldunuz .")
      with open("accounts.txt","a",encoding="utf-8") as file :
        file.write(f"{name}|{date}|{email}|{passw1}|{iban}\n")
      return True
    else:
      x = input("  Girdiğiniz şifreler uyuşmuyor . Tekrar deneyiniz veya çıkış yapmak istiyorsanız exit yazın .")
      if x == "exit" :
        shutdown()
      else:
        continue


def login():
    while True :
      email = input("  Emailinizi giriniz. >> ")
      passw = input("  Şifrenizi giriniz. >> ")
      with open("accounts.txt","r",encoding="utf-8") as file:
        found = False
        for line in file :
          parts = line.strip().split("|")
          if len(parts) != 5:
            continue
          storedname,storeddate,storedemail,storedpassw,storediban = parts
          if email==storedemail and passw==storedpassw :
            print("  Başarıyla giriş yaptınız .")
            print(f"\n\n  Hoşgeldiniz {storedname} . Iban numaranız. >> {storediban}")
            found = True
            return True
        if not found :
          x = input("  Girdiğiniz eposta veya şifre hatalı . Tekrar deneyiniz veya çıkmak istiyorsanız exit yazınız  >> ")
          if x == "exit":
             shutdown()
          else:
            continue
def getAccnum():
    accnum = random.randint(1000,9999)
    print(f"\n  Hesap numaranız  >> {accnum} \n  Hesap numaranızı kaybetmemeniz önemlidir.")
    with open("money.txt","a",encoding="utf-8") as file :
        file.write(accnum+"|"+0+"\n")

def showBalance():
  isexit = False
  while isexit == False :
      accnum = input("  Hesap numaranızı giriniz  >> ")
      with open("money.txt","r",encoding="utf-8") as file :
          for line in file :
              parts = line.strip().split("|")
              storedaccnum,storedmoney = parts
              if accnum == storedaccnum :
                  print(f"  Bakiyeniz  >> {storedmoney}")
                  isexit = True
          x = input("  Bu hesap numarası bulunamadı .Tekrar deneyin veya çıkmak için exit yazın.")
          if x == "exit" :
              isexit = True
          
                  

def deposit():
  pass

def withdraw():
  pass

def send():
  pass


def loginmenu():
  isexit = False
  while isexit==False :
    print("\n\n"+"Seçenekler".center(25,"-"))
    order2 = input("\n   Bakiye görüntüle -1\n   Para yatır -2\n   Para çek -3\n   Para gönder -4\n   Çıkış yap -5\n   Hesap numarası al -6\n\n     >>> ")
    if order2 == "1" :
      showBalance()
    elif order2 == "2" :
      deposit()
    elif order2 == "3" :
      withdraw()
    elif order2 == "4" :
      send()
    elif order2 == "5" :
      shutdown()
    elif order2 == "6" :
        getAccnum()
    else:
      print("yanlış tuşlama".center(50,"*"))
    



def adminlogin():
  
  adminmail = "admin@heqon.com"
  adminpassw = "1453"
  while True :
    email = input("  Emaili giriniz  >> ")
    passw = input("  Şifreyi giriniz  >> ")
    if email==adminmail and passw==adminpassw :
      print("  Başarıyla giriş yapıldı .")
      return True
    else :
      x = input("  Email veya şifre hatalı . Tekrar deneyin veya exit yazarak çıkış yapın.")
      if x == "exit" :
        shutdown()
      else:
        continue
        
  




print("by heqoN".center(100,"-"))
print("  Banka sistemi projeme hoşgeldiniz.")
isquit = False
while isquit == False :
  order1 = input("SEÇENEKLER".center(25,"*")+"\n\n   Kayıt ol -1\n  Giriş yap -2\n Çıkış yap -3\n  Admin girişi  -4\n\n   >>> ")
  if order1 == "1" :
    register()
  elif order1 == "2" :
    login()
    loginmenu()
  elif order1 == "3" :
    print("  Çıkış yapılıyor ... ")
    isquit = True
  elif order1 == "4" :
    adminlogin()
  else :
    print("  Bir hata oluştu.")
    shutdown()
