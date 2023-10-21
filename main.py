# öğrenci ismi, soyismi, not1 not2 ve not3 notlarını
# hoca tarafından alıp not defterine kaydedeceğiz.
# öğretmen her öğrencinin istediği notuna istediği kadar puan
# ekleyebilir.
# ortalama,bilgisi ekrana yazdırılabilecek
# öğretmen istediği öğrencinin notunu ekranda ismini aratarak
# görebilecek
# bu bir masaüstü uygulama olacak
import tkinter
# --------------------- User Interface -----------------
from tkinter import *
from tkinter import messagebox

notToplami = 0
ogrenciSayisi = 0
window = Tk()
window.title("Not Bilgisi Yönetim Sistemi")
window.config(pady=100,padx=100)
window.configure(bg="blue")

# --------------labeller------------------------------------



ogrenciIsmi = Label(text="OGRENCI ISMINI GIRIN: ",width=20,fg="blue")
ogrenciIsmi.grid(row=1,column=1,pady=5)

ogrenciSoyismi = Label(text="OGRENCI SOYISMI GIRIN: ",width=20,fg="blue")
ogrenciSoyismi.grid(row=2, column=1,pady=5)

ogrenciNot1 = Label(text="NOT1 GIRIN: ",width=20,fg="blue")
ogrenciNot1.grid(row=3,column=1,pady=5)

ogrenciNot2 = Label(text="NOT2 GIRIN:  ",width=20,fg="blue")
ogrenciNot2.grid(row=4,column=1,pady=5)

ogrenciNot3 = Label(text="NOT3 GIRIN:  ",width=20,fg="blue")
ogrenciNot3.grid(row=5,column=1,pady=5)


# --------------------------Girisler------------------------

ogrenciIsmiEntry = Entry(width=25)
ogrenciIsmiEntry.grid(row=1,column=2)

ogrenciSoyismiEntry = Entry(width=25)
ogrenciSoyismiEntry.grid(row=2,column=2)

ogrenciNotEntry1 = Entry(width=25)
ogrenciNotEntry1.grid(row=3,column=2)

ogrenciNotEntry2 = Entry(width=25)
ogrenciNotEntry2.grid(row=4,column=2)

ogrenciNotEntry3 = Entry(width=25)
ogrenciNotEntry3.grid(row=5,column=2)

#-----------------------Functions------------------------------------
def kaydet():
    isim = ogrenciIsmiEntry.get()
    soyisim = ogrenciSoyismiEntry.get()
    not1 = ogrenciNotEntry1.get()
    not2 = ogrenciNotEntry2.get()
    not3 = ogrenciNotEntry3.get()
    isOkey = messagebox.askyesno(title="Onay Kutusu",message=f"Bilgilerinizin Detayı:\nIsim: {isim}\nSoyisim: {soyisim}\nNot1: {not1}\nNot2: {not2}\nNot3: {not3}")
    if isOkey == True:
        with open("notlar.txt","a") as f:
            f.write(f"{isim} {soyisim} {not1} {not2} {not3}\n")
        messagebox.showinfo(title="Bilgi", message="Bilgiler Basariyla Kaydedildi.")

        ogrenciIsmiEntry.delete(0,END)
        ogrenciSoyismiEntry.delete(0,END)
        ogrenciNotEntry1.delete(0,END)
        ogrenciNotEntry2.delete(0,END)
        ogrenciNotEntry3.delete(0,END)
        ogrenciIsmiEntry.focus()

def ortalama():
    global ogrenciSayisi
    global notToplami
    notToplami = 0
    ogrenciSayisi = 0
    with open("notlar.txt","r") as f:
        for i in f:
            ogrenciSayisi = ogrenciSayisi+1
            notToplami = notToplami+int(i.split(" ")[2])*0.2+int(i.split(" ")[3])*0.2+int(i.split(" ")[4])*0.6
    messagebox.showinfo(title="Ortalama Bilgisi",message=f"Ogrenci sayisi: {ogrenciSayisi}, ToplamNot: {notToplami: .2f}\nOrtalama: {(notToplami/ogrenciSayisi): .2f}")




def ogrenciAra():
    def goster():
        with open("notlar.txt","r") as f:
            for i in f:
                if i.split(" ")[0] == ogrenciAraIsimEntry.get():
                    if i.split(" ")[1] == ogrenciAraSoyisimEntry.get():
                        isim = i.split(" ")[0]
                        soyisim = i.split(" ")[1]
                        not1 = i.split(" ")[2]
                        not2 = i.split(" ")[3]
                        not3 = i.split(" ")[4]
                        messagebox.showinfo(title="Ogrenci Bilgisi", message=f"Isim: {isim}\nSoyisim: {soyisim}\nNot1: {not1}\nNot2: {not2}\nNot3: {not3}")

    #-----------------LABELS--------------------------------
    ogrenciAraPenceresi = tkinter.Toplevel(window)
    ogrenciAraPenceresi.title("Ogrenci Arama ")
    ogrenciAraOgrenciIsmi = Label(ogrenciAraPenceresi,text="Ogrenci Adi: ",width=25)
    ogrenciAraOgrenciIsmi.grid(row=1,column=1)
    ogrenciAraOgrenciSoyismi = Label(ogrenciAraPenceresi,text="Ogrenci Soyadi: ",width=25)
    ogrenciAraOgrenciSoyismi.grid(row=2,column=1)
    ogrenciAraPenceresi.config(padx=100,pady=100)


    #--------------------ENTRY-----------------------------------
    ogrenciAraIsimEntry = Entry(ogrenciAraPenceresi,width=25)
    ogrenciAraIsimEntry.grid(row=1, column=2)

    ogrenciAraSoyisimEntry = Entry(ogrenciAraPenceresi,width=25)
    ogrenciAraSoyisimEntry.grid(row=2,column=2)


    aramaIslemi = Button(ogrenciAraPenceresi,text="Ara",width=25,command=goster)
    aramaIslemi.grid(row=3,column=1,pady=10)
    ogrenciAraPenceresi.mainloop()




import matplotlib.pyplot as plt
def grafikGoster():
    toplamlarinListesi = list()
    genelListe = [1,2,3]
    toplam1 = 0
    toplam2 = 0
    toplam3 = 0
    with open("notlar.txt","r") as f:
        for i in f:
            toplam1 = toplam1 + int(i.split(" ")[2])
            toplam2 = toplam2 + int(i.split(" ")[3])
            toplam3 = toplam3 + int(i.split(" ")[4])
    toplamlarinListesi.append(toplam1)
    toplamlarinListesi.append(toplam2)
    toplamlarinListesi.append(toplam3)

    plt.plot(genelListe,toplamlarinListesi)
    plt.title("Sinavlarin Genel Grafigi")
    plt.xlabel("Sınav Türü")
    plt.ylabel("Ortalaması")
    plt.show()


#---------------------------END-Function--------------------






bilgileriKaydet = Button(text="Bilgileri Kaydet",width=25,fg="red",bg="yellow",command=kaydet)
bilgileriKaydet.grid(row=6,column=1,pady=10, padx=10)

ortalamaGoster = Button(text="Ortalama Goster", width=25, fg="red",bg="yellow",command=ortalama)
ortalamaGoster.grid(row=6,column=2,pady=20)


ogrenciyeOzelBilgi = Button(text="Ogrenci Ara", width=25,fg="red",bg="yellow",command=ogrenciAra)
ogrenciyeOzelBilgi.grid(row=8,column=1,pady=20)

sinavGrafigiGoster = Button(text="Sınavlar Grafiğini Göster", width=25,fg="red",bg="yellow", command=grafikGoster)
sinavGrafigiGoster.grid(row=8,column=2)









window.mainloop()







# -------------------Dosya işlemleri-----------------------------
