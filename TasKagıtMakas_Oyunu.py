import random
import sys
oyuncu_mac_galibiyeti=0
bilgisayar_mac_galibiyeti=0
oyun_Sayisi=0
tur_Sayisi=0
oyuncu_Galibiyet_Sayisi=0
bilgisayar_Galibiyet_Sayisi=0
def tas_kagit_makas_AHMET_ERBEY():
   #oyun hakkında genel bilgiler ve kurallar
    print("\n Merhaba! Taş, makas, kağit oyununu hiç duymuş muydun? Eğer duymadiysan endişelenme,\nçünkü ben buradayim ve sana oyunun kurallarini anlatacağim.\n Hem basit hem de eğlenceli bir oyun bu!"

    " Öncelikle, bu oyun iki kişi arasinda oynaniyor ve her oyuncu bir el hareketi seçiyor. Seçeneklerimiz ne mi? \nTaş, \n  makas \n      ya da \n            kağit.\n Evet, bu kadar basit! Şimdi sana hangi hareketin ne anlama geldiğini ve nasil kazandiğini anlatayim:"

    "\n\nTaş: Yumruğunu sikarak oynuyorsun. Taş, makasi yener ama kağit tarafindan sarilir."
    "\nMakas: İşaret ve orta parmağini açarak yapiyorsun. Makas, kağidi keser ama taş tarafindan ezilir."
    "\nKağit: Elini düz bir şekilde açiyorsun. Kağit, taşi sarar ama makas tarafindan kesilir."
    "\n\n( Tabii senle oynarken sadece istediğin hareketi seçmeni ve onu yazmani isteyececeğim hareketi elinle yapmana gerek yok :)   )"
    "\n\nHer iki oyuncu da ayni anda bir hareket seçiyor ve sonra bakiyoruz, kim kimi yendi! Eğer ayni hareketi seçerseniz, o turda kimse kazanmiş sayilmaz, berabere!"

    "\nGenellikle birkaç tur oynariz ve kim daha çok tur kazanirsa oyunu kazanmiş olur. \n")

    oyuncu_baslama_tercihi='evet'     
    global oyuncuismi

    chooses=['tas','kagit','makas']
    bilgisayar_başlamasi=['evet','hayir']
    #oyun için gerekli olan sayaç ,değişkenler ve fonksiyonlar
    def tur_Sayisi_arttirma(tur_Sayisi):
        tur_Sayisi+=1
        return tur_Sayisi
    def yeni_oyun_tercihi(oyun_Sayisi,oyuncu_baslama_tercihi):
        bilgisayar_baslama_tercihi=random.choices(bilgisayar_başlamasi,weights=[5,1],k=1)[0]
        if(oyun_Sayisi==3):
            print('\nBen biraz yoruldum doğrusu bu kadar oyundan sonra biraz ara vermem gerekiyor. \nYine de seninle oynamak büyük zevkti başka bir zaman tekrar oynamaktan zevk alirim görüşürüz')
            return "1"
        elif(oyuncu_baslama_tercihi=='evet'and bilgisayar_baslama_tercihi=='evet'):
            print('\nO zaman yeni oyun başlasin. Ben de tekrardan oynamak için sabirsizlaniyorum')
            return "2"
        elif(oyuncu_baslama_tercihi=='evet'and bilgisayar_baslama_tercihi=='hayir'):
            print('\nKusura bakma benim bazi özel sebeplerden ötürü çikmam lazim başka bir zaman tekrardan oynayabiliriz diye umuyorum görüşürüz')
            return '1'
        else:
            print('\nDemek yeni oyuna başlamak istemiyorsun, başka bir zaman tekrardan oynamaya gel ama bekliyorum')
            return "1"
        
    def sonuca_gore_yorum_yapma(bilgisayar_Galibiyet_Sayisi,oyuncu_Galibiyet_Sayisi):
        if(bilgisayar_Galibiyet_Sayisi==oyuncu_Galibiyet_Sayisi):
            print('\nBerabere kaldik, demek ki benim seviyeme ulaşmayi başardin! Ama unutma, benimle denk olabilmek bile senin için büyük bir başari.')

        elif(bilgisayar_Galibiyet_Sayisi<=oyuncu_Galibiyet_Sayisi):
            global oyuncu_mac_galibiyeti
            
            oyuncu_mac_galibiyeti+=1
            print('\nSeni biraz hafife almişim dişli rakip çiktin\n')
        else:
            global bilgisayar_mac_galibiyeti
            bilgisayar_mac_galibiyeti+=1
            print('\nSaninirim seni yendim pek beklenmedik bir durum değildi zaten yine de seni tebrik ederim')

    def genel_oyun_istatistigi(oyuncu_mac_galibiyeti,bilgisayar_mac_galibiyeti,oyun_Sayisi,oyuncuismi):
        print('\n  Şuan  kadar oynanan maç sayisi:',oyun_Sayisi,'/ senin kazandiğin maç galibiyet sayisi=> ', oyuncu_mac_galibiyeti,'/ ve benim kazandiğim maç galibiyetlerinin sayisi=> ',bilgisayar_mac_galibiyeti, '\n\n   yani genel skor bu şuanlik  => ',oyuncuismi,'(',oyuncu_mac_galibiyeti,'::',bilgisayar_mac_galibiyeti,') Bilgisayar')
    def oyun_algoritmasi_ilk_kisim():
        global tur_Sayisi
        tur_Sayisi=0
        global oyuncu_Galibiyet_Sayisi
        oyuncu_Galibiyet_Sayisi=0
        global bilgisayar_Galibiyet_Sayisi
        bilgisayar_Galibiyet_Sayisi=0
        try:
            global istenilen_Tur_Sayisi
            istenilen_Tur_Sayisi=int(input(' \n kacinci turda oyun sona ersin istersin? \n benim şuanlik enerjim gayet yerinde.   \n Oyunun kaç tur oynanacağini giriniz: '))
            if(type(istenilen_Tur_Sayisi)!=int):
                raise TypeError('tur sayisini int formatinda girmeniz gerekmektedir')
        except:
            print('lütfen int formatinda bir şey giriniz')
            istenilen_Tur_Sayisi=int(input(' \n kacinci turda oyun sona ersin istersin? \n benim şuanlik enerjim gayet yerinde.   \n Oyunun kaç tur oynanacağini giriniz: '))

    def oyun_algoritmasi_orta_kisim(istenilen_Tur_Sayisi,tur_Sayisi,oyuncu_Galibiyet_Sayisi,bilgisayar_Galibiyet_Sayisi):
     
     while(True):

        bilgisayar_Secimi= random.choice(chooses)
        if(tur_Sayisi==0):
            oyuncu_Secimi=input('Madem öyle haydi başlayalim oyuna :)\n'
                                'tas, kagit veya makas seçeneklerinden birini seç de görelim kim kazanicak =)\n'
                                'Ilk seciminizi girin:')
            print('Bilgisayar seçimi: ',bilgisayar_Secimi) 
        else:
            
            oyuncu_Secimi=input('Sizin sonraki seçiminiz: ')
            print('Bilgisayar seçimi: ',bilgisayar_Secimi)            
        
        if(oyuncu_Secimi==bilgisayar_Secimi):
            if(tur_Sayisi==0):
                print('\nDaha ilk turdan berabere kaldik (=|) \n Ama oyun devam ediyor acaba kim ilk galibiyetini alicak\n')
            else:
                print('\nBerabere kaldik (=|) \n')
            
        elif(oyuncu_Secimi=='tas'and bilgisayar_Secimi=='makas' or oyuncu_Secimi=='makas'and bilgisayar_Secimi=='kagit' or oyuncu_Secimi=='kagit'and bilgisayar_Secimi=='tas' ):
            oyuncu_Galibiyet_Sayisi+=1
            if(tur_Sayisi==0):
                print('\nGüzel baslangic daha ilk turdan beni yendin, şans senden yana bu tur için fakat daha oyun devam ediyor hemen kazandiğini düşünme\n')
            else:
                print('\niyi seçim bu turu kazandin =)\n')
        else:
            bilgisayar_Galibiyet_Sayisi+=1
            if(tur_Sayisi==0):
                print('\nSenin için kotu bir başlangic, bende acemi sansi var sanirim :D\n Sanirim şans benden yana bu tur için fakat daha oyun yeni başliyor hemen kaybettiğini düşünme\n')
            else:
                print('\nKaybettin bu turu ne yazik ki =(\n')
        tur_Sayisi=tur_Sayisi_arttirma(tur_Sayisi)   
        print('Şuanki duruma göre ',tur_Sayisi,'inci turdayiz ve sonuc: ',oyuncuismi,'(',oyuncu_Galibiyet_Sayisi,' : ',bilgisayar_Galibiyet_Sayisi,') Bilgisayar')
        if(tur_Sayisi==istenilen_Tur_Sayisi):
            sonuca_gore_yorum_yapma(bilgisayar_Galibiyet_Sayisi,oyuncu_Galibiyet_Sayisi)
            global oyuncu_baslama_tercihi
            
            oyuncu_baslama_tercihi=input( 'Yeni oyun istiyorsan evet veya istemiyorsan hayir yaz veya çikmak için exit yazabilirsin: ')     
            global oyun_Sayisi           
            oyun_Sayisi=oyun_Sayisi+1
            genel_oyun_istatistigi(oyuncu_mac_galibiyeti,bilgisayar_mac_galibiyeti,oyun_Sayisi,oyuncuismi)
            break

    
    oyuncu_baslama_tercihi=input('\nOyuna başlamak istiyorsaniz evet istemiyorsaniz lütfen hayir yaziniz: ')
    if(oyuncu_baslama_tercihi=='hayir'):
        print(' \nCiddi misin gerçekten \n\n Sanirim seni daha başlamadan çok korkuttum cesaretini topladiğin bir zaman tekrardan gel \n ')
        
    elif(oyuncu_baslama_tercihi=='evet'):
        print('\n Güzel sonraki aşamaya geçelim o zaman')
        try:
            oyuncuismi=input(' Merhabalar tekrardan \n  \n Oyuna başlamadan önce adiniz nedir acaba sorabilir miyim sorun olmazsa? \n Adiniz:  ')
            if(type(oyuncuismi)!=str):
                raise TypeError('\nadinizi string formatinda girmeniz gerekmektedir')
        except:
            print('lütfen string formatinda bir şey giriniz')
            oyuncuismi=input(' Merhabalar tekrardan \n  \n Oyuna başlamadan önce adiniz nedir acaba sorabilir miyim sorun olmazsa? \n Adiniz:  ')
    elif oyuncu_baslama_tercihi.lower() == 'exit':
        print("Programdan çikiş yapiliyor...")
        sys.exit()
        
    while (True):
        oyun_algoritmasi_ilk_kisim()
        oyun_algoritmasi_orta_kisim(istenilen_Tur_Sayisi,tur_Sayisi,oyuncu_Galibiyet_Sayisi,bilgisayar_Galibiyet_Sayisi)
        if(yeni_oyun_tercihi(oyun_Sayisi,oyuncu_baslama_tercihi)=="1"):
            break
        
        

    print('\n \n   Güzel oyundu ben eğlendim umarim sen de eğlenmişsindir. Kendine iyi bak ')
    print('\n\n \t\t\tGAME OVER\n')        
            
            
            
#fonksiyonun çağırılması
tas_kagit_makas_AHMET_ERBEY()