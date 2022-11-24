#inputan 
bangun=int(input('bangun ruang yang ingin dihitung volume: \n1.limas \n2.bola \n3.prisma \n4.kerucut \nmasukan pilihan anda :'))
if bangun == 1:
    int(input('pilih: \n1.limas segitiga \n2.limas  '))
elif bangun == 2 : 
    r=int(input('masukan jari jari: '))
    hasilbola=(4/3)*(22/7)*(r^3)
    print(hasilbola)
elif bangun == 4 : 
    rkrucut=int(input('masukan jari jari alas: '))
    tkrucut=int(input('masukan tinggi krucut: '))
    hasilkrucut=(1/3)*(22/7)*rkrucut*rkrucut*tkrucut
    print(("volume nya:",hasilkrucut,))
elif bangun== 3:
    pilihprisma=int(input('pilih prisma nya: \n1.pris segitiga \n2.pris segiempat n\3.pris segilima'))
    if pilihprisma== 1:
        alaspsgitiga=int(input('masukan alas sgitiga: '))
        tinggi_prisma_alas_sgitiga=(input('masukan tinggi alas: '))
        tinggi_prisma_sgitiga=(input('masukan tinggi prisma segitiga:'))
        hasilpsgitiga=(1/2)*alaspsgitiga*tinggi_prisma_alas_sgitiga*tinggi_prisma_sgitiga
        print('volumenya:',hasilpsgitiga)
    elif pilihprisma==2:
        panjangalaspsgiempat=int(input('masukan lebar sgiempat: '))
        lebar_prisma_alas_sgiempat=(input('masukan panjang alas: '))
        tinggi_prisma_sgiempat=(input('masukan tinggi prisma segiempat:'))
        hasilpsgiempat= alaspsgiempat*t
else: 
    print('ga bisa gue itung bro...')