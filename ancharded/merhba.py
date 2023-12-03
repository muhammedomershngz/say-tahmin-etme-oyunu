import random
import time
print('bir sayi tahmin etme oyunu oynayalim')
pc_sayisi=random.randint(1,10)
kullanici_sayisi=int(input('1 ile 10 arasinda bir sayi seç'))
while True
if pc_sayisi == kullanici_sayisi:
    print('doğru bildin')
else
    print('yanliş bildin')