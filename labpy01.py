print ("mencari bilangan pertama terbesar dari tiga bilangan")

a = int(input("masukkan bilangan pertama :" ))
b = int(input("masukkan bilangan kedua :"))
c = int(input("masukkan bilangan ketiga :"))

if a > b and a > c :
    print ("\nbilangan terbesar adalah :%s" %a)
elif b > a and b > c :
    print ("\nbilangan terbesar adalah :%s" %b)
else :
    print ("\nbilangan terbesar adalah :%s" %c)

