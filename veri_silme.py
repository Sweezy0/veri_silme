import sqlite3
con=sqlite3.connect("Şirket.db")
cursor=con.cursor()
def veri_sil():
    cursor.execute("Delete from elemanlar where isim='Salih'")
    con.commit()
    print("kayıt silindi",con.total_changes)
veri_sil()
con.close