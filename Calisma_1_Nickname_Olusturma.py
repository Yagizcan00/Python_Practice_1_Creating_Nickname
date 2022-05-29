print("Nickname oluşturma programına hoşgeldiniz :)\nLütfen sizden istediğimiz bilgilerinizi giriniz;")

ad = input("\nLütfen ön adınızı giriniz: ")
soyad = input("Lütfen soyadınızı giriniz: ")

print("\nAdınız ve soyadınız kaydediliyor.")
print(".....")
print("Adınız ve soyadınız kaydedildi.")

print("\nİşte sizin için tavsiye ettiğimiz kullanıcı adı (nickname): " + ad[0:3] + "00" + soyad[-4:-1])

#Başarılı olundu.