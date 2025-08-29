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
    print(f"  Dosya okuma hatası  >> {e}")
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
        file.write(f"{accnum}|0\n")


def showBalance():
  while True :
      accnum = input("  Hesap numaranızı giriniz  >> ")
      with open("money.txt","r",encoding="utf-8") as file :
          for line in file :
              parts = line.strip().split("|")
              storedaccnum,storedmoney = parts
              if accnum == storedaccnum :
                  print(f"  Bakiyeniz  >> {storedmoney}")
                  return True
          x = input("  Bu hesap numarası bulunamadı .Tekrar deneyin veya çıkmak için exit yazın.")
          if x == "exit" :
              return False
          
                  

def deposit():
    accnum = input("  Hesap numaranızı giriniz  >> ")
    amount = int(input("  Yüklemek istediğiniz miktar  >> "))

    with open("money.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    updated_lines = []
    found = False

    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 2:
            storedaccnum, money = parts
            if storedaccnum == accnum:
                dpst = int(money) + amount
                updated_lines.append(f"{storedaccnum}|{dpst}\n")
                found = True
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)  

    if found:
        with open("money.txt", "w", encoding="utf-8") as file:
            file.writelines(updated_lines)
        print("  Para yatırma işlemi başarılı.")

        with open("logs.txt","a",encoding="utf-8") as file :
          file.write(f" {storedaccnum} numaralı hesaba {amount} miktarında para yüklendi bakiye >> {dpst}\n")
    else:
        print("  Hesap numarası bulunamadı.")
        

def withdraw():
    accnum = input("  Hesap numaranızı giriniz  >> ")
    amount = int(input("  Çekmek istediğiniz miktarı giriniz >> "))

    updated_lines = []
    found = False

    with open("money.txt","r",encoding="utf-8") as file :
       lines = file.readlines()
    for line in lines :
       parts = line.strip().split("|")
       if len(parts) == 2:
          storedaccnum,money=parts
          if storedaccnum==accnum :
             wthdrw = int(money) - amount
             if wthdrw < 0 :
                print("  Hesabınızda bu kadar para yok !")
                return False
             updated_lines.append(f"{storedaccnum}|{wthdrw}")
             found = True
          else:
             updated_lines.append(line)
       else:
          updated_lines.append(line)
    
    if found :
      with open("money.txt","w",encoding="utf-8") as file :
          file.writelines(updated_lines)
      print("  Para yatırma işlemi başarılı .")

      with open("logs.txt","a",encoding="utf-8") as file :
         file.write(f" {storedaccnum} numaralı hesaptan {amount} miktarında para çekildi bakiye >> {wthdrw}\n")
    
    else:
       print("  Hesap numarası bulunamadı.")
  

              
     

def send():
    accnum = input("  Hesap numaranızı giriniz  >> ").strip()
    accnum2 = input("  Transfer yapmak istediğiniz hesabın numarasını giriniz  >> ").strip()
    if accnum == accnum2:
        print("  Aynı hesaba transfer yapılamaz.")
        return False

    try:
        amount = int(input("  Yollamak istediğiniz miktarı giriniz  >> ").strip())
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("  Geçerli bir pozitif sayı girin.")
        return False

    try:
        with open("money.txt", "r", encoding="utf-8") as file:
            lines = [line.rstrip("\n") for line in file]
    except FileNotFoundError:
        print("  money.txt bulunamadı.")
        return False

    new_lines = []
    found_from = found_to = False
    bal_from = bal_to = None

    for line in lines:
        parts = line.split("|")
        if len(parts) != 2:
            new_lines.append(line + "\n")
            continue
        stored, money = parts
        try:
            bal = int(money)
        except ValueError:
            bal = 0

        if stored == accnum:
            if bal < amount:
                print("  Hesabınızda bu kadar para yok !")
                return False
            bal_from = bal - amount
            found_from = True
            new_lines.append(f"{stored}|{bal_from}\n")
        elif stored == accnum2:
            bal_to = bal + amount
            found_to = True
            new_lines.append(f"{stored}|{bal_to}\n")
        else:
            new_lines.append(line + "\n")

    if not found_from:
        print("  Gönderen hesap numarası bulunamadı.")
        return False
    if not found_to:
        print("  Alıcı hesap numarası bulunamadı.")
        return False

    with open("money.txt", "w", encoding="utf-8") as file:
        file.writelines(new_lines)

    print("  Transfer başarılı.")
    return True




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
