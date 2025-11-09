import random
import time
accs = {}
def UserStr(User = ""):
    Score = 0
    CountNumber= 0
    CountUpper = 0
    if len(User) > 5:
        Score += 25
    elif User.isalnum():
        Score += 25
    for numba in User:
        if numba.isdigit():
            CountNumber += 1
            if CountNumber >= 2:
                Score += 25
        elif numba.isupper():   
            CountUpper += 1
            if CountUpper >= 2:
                Score += 25
    if Score >= 75:
        print("Kullanıcı adınız gayet güçlü!")
        time.sleep(.5)
        return True
    else:
        print("Seçtiğiniz kullanıcı adı yeterli koşulları sağlamıyor.")
        time.sleep(.5)
        return False
#====================================================================================
def PassStr(Pass = ""):
    Score = 0
    CountNumber = 0
    CountUpper = 0
    if len(Pass) > 5:
        Score += 25
    elif Pass.isalnum():
        Score += 25
    for numba in Pass:
        if numba.isdigit():
            CountNumber += 1
            Score += 25
        elif numba.isupper():
            CountUpper += 1
            if CountUpper >= 2:
                Score += 25
    if Score >= 75:
        print("Şifreniz gayet güçlü!")
        time.sleep(.5)
        return True
    else:
        print("Seçtiğiniz şifre yeterli koşulları sağlamıyor.")
        time.sleep(.5)
        return False
#=======================================================================================
def CheckNum(msg = "Lütfen geçerli bir işlem numarası giriniz: "):
    while True:
        x = input(msg)
        if x.isdigit():
            return x
        else:
            print("Lütfen Tekrar Deneyiniz.")
            time.sleep(.5)
totalaccs = 0 
while True:
    print("Bankamatiğe Hoşgeldiniz!")
    print("1. Kayıt Ol")
    print("2. Giriş Yap")
    print("3. Sistemden Çıkış Yap")
    islem = CheckNum()
    if islem == "1":
        user = input("Kullanıcı adı belirleyiniz: ")
        dogrulukuser = UserStr(user)
        if dogrulukuser == True:
            kullanici_mevcut = False
            for bil in  accs.values():
                if bil["KullaniciAdi"] == user:
                    kullanici_mevcut = True
                    break
            if kullanici_mevcut:
                print("Bu kullanıcı adı daha önce alınmış")
                time.sleep(1)
            else:
                pass1 = input("Şifre belirleyiniz: ") 
                dogrulukpass = PassStr(pass1)
                if dogrulukpass == True:
                    while True:
                        hesapNo = random.randint(10000,99999)
                        if hesapNo not in accs:
                            break
                    
                    accs[hesapNo] = {}   
                    accs[hesapNo]["KullaniciAdi"] = user
                    accs[hesapNo]["Sifre"] = pass1
                    accs[hesapNo]["Bakiye"] = 0
                    totalaccs += 1
                    print(f"Başarıyla Kayıt Olundu! Hesap numaranız: {hesapNo}")
                    time.sleep(1)
    elif islem == "2":
        if accs == {}:
            print("Önce lütfen kayıt olun.")
            time.sleep(1)
        else:
            Enter = input("Lütfen Kullanıcı adınızı giriniz: ")
            Sifre = input("Lütfen şifrenizi giriniz: ")
            AccEntered = None
            EnterSuc = False
            for hesapnum, bilgiler in accs.items():
                if bilgiler["KullaniciAdi"] == Enter and bilgiler["Sifre"] == Sifre:
                    AccEntered = hesapnum
                    EnterSuc = True
                    break
            if EnterSuc:    
                print("Başarıyla Giriş Yaptınız.")
                time.sleep(.5)

                
                print("Yönlendiriliyorsunuz...")
                time.sleep(1.5)
                
                
                while True:
                    print(f"\n--- Bankamatik (Hesap: {AccEntered} | Hoşgeldiniz: {Enter}) ---")
                    print("1. Bakiye Sorgulama")
                    print("2. Para Çekme")
                    print("3. Para Yatırma")
                    print("4. Para Gönder")
                    print("5. Çıkış Yap")
                    islem = CheckNum()
                    if islem == "1":
                        time.sleep(.25)
                        print(f"Hesap Bakiyeniz: {accs[AccEntered]["Bakiye"]}")
                        time.sleep(1) 
                    elif islem == "2":
                        CekMiktar = int(CheckNum("Çekmek İstediğiniz Miktari Giriniz: "))
                        if accs[AccEntered]["Bakiye"] < CekMiktar:
                            print("Hesabınızda yeteri kadar bakiye bulunmamaktadır.")
                            time.sleep(1)
                        else:    
                            accs[AccEntered]["Bakiye"] -= CekMiktar
                            print(f"Çektiğiniz Miktar: {CekMiktar}, Hesapta Kalan Miktar: {accs[AccEntered]["Bakiye"]}")
                            time.sleep(1)
                    elif islem == "3":
                        YatirMiktar = CheckNum("Yatırmak İstediğiniz Miktari Giriniz: ")
                        YatirMiktar = int(YatirMiktar)
                        accs[AccEntered]["Bakiye"] += YatirMiktar
                        print(f"Yatırdığınız Miktar:: {YatirMiktar}, Hesapta Kalan Miktar: {accs[AccEntered]["Bakiye"]}")
                        time.sleep(1)
                    elif islem == "4":
                        if totalaccs > 1:
                            GonderNum = int(CheckNum("Para Göndermek istediğiniz kişinin hesap numarasını yazınız: "))
                            if GonderNum == AccEntered:
                                print("Kendinize para gönderemezsiniz.")
                                time.sleep(1)
                            elif GonderNum in accs:
                                GonderMiktar = CheckNum("Göndermek istediğiniz miktarı giriniz: ")
                                GonderMiktar = int(GonderMiktar)
                                time.sleep(1)
                                if GonderMiktar > accs[AccEntered]["Bakiye"]:
                                    print("Yeterli miktarda bakiye bulunmamaktadır.")
                                    time.sleep(1)
                                else:
                                    accs[AccEntered]["Bakiye"] -= GonderMiktar
                                    accs[GonderNum]["Bakiye"] += GonderMiktar
                                    print(f"İşlem başarılı! {GonderNum} nolu hesaba {GonderMiktar} TL gönderilmiştir.")
                                    time.sleep(1)
                                    print(f"Yeni bakiyeniz: {accs[AccEntered]["Bakiye"]}")
                                    time.sleep(1)
                            else:
                                print("Bu numaraya ait hesap bulunamadı.")
                                time.sleep(1)


                        else: 
                            print("Para Gönderilebilecek hesap yok.")      
                            time.sleep(1)                       
                    elif islem == "5":
                        print("Hesaptan çıkılıyor...")
                        time.sleep(1)
                        print("Başarıyla Çıkış Yapıldı!")
                        time.sleep(1)
                        break
            else:
                print("Kullanıcı adı veya şifreniz hatalı. Tekrar Deneyiniz.")
                time.sleep(1)        
    elif islem == "3":
        print("Görüşmek Üzere!")
        break              
                
    else:
                print("Geçersiz işlem numarası girildi. Tekrar Deneyiniz.")
                time.sleep(1)
            
        


                