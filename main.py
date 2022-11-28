
# Mengimport sqlite3, berguna untuk membuat database
# Dan untuk menyimpan data-data yang di inputkan oleh user
import sqlite3

# Mengimport semua(*) package yang ada didalam modul tkinter
from tkinter import *

# Mengimport tema tkinter(Theme Tkinter)
from tkinter import ttk

# Mengimport messagebox
from tkinter.messagebox import showwarning

root = Tk()
root.title("DATA MAHASISWA")
root.geometry("1150x400")
root.resizable(False, False)
my_tree = ttk.Treeview(root)
storeName = "Data Mahasiswa"

# Fugnsi ini berguna untuk menyimpan data kedalam sqlite dengan tuple
# Yang nantinya akan membaca data mulai dari index awal sampai akhir(-1) 
def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

# Fungsi Untuk Query Menambah Data
def insert( nama, nim, jurusan, alamat):
    # Ini berguna ketika program di run akan membuat file baru dengan nama data.db
    conn = sqlite3.connect("data.db") 

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(itemNama TEXT, itemNim TEXT, itemJurusan TEXT, itemAlamat TEXT)""")

    cursor.execute("INSERT INTO inventory VALUES ('" + str(nama) + "','" + str(nim) + "','" + str(jurusan) + "','" + str(alamat) + "')")
    conn.commit()

# Fungsi Untuk Query Menghapus Data
def delete(data):
    # Ini berguna ketika program di run akan membuat file baru dengan nama
    conn = sqlite3.connect("data.db"
    )
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemNama TEXT, itemNim TEXT, itemJurusan TEXT, itemAlamat TEXT)""")

    cursor.execute("DELETE FROM inventory WHERE itemId = '" + str(data) + "'")
    conn.commit()

# Fungsi Untuk Query Mengedit Data
def update(id, name, price, quantity,  idName):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")

    cursor.execute("UPDATE inventory SET itemId = '" + str(id) + "', itemName = '" + str(name) + "', itemPrice = '" + str(price) + "', itemQuantity = '" + str(quantity) + "' WHERE itemId='"+str(idName)+"'")
    conn.commit()

# Fungsi Untuk Query Membaca Data
def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results


# Fungsi Untuk Menambah Data Ke Dalam SQLITE
def insert_data():
    itemNama = str(entryNama.get())
    itemNim = str(entryNim.get())
    itemJurusan = str(entryJurusan.get())
    itemAlamat = str(entryAlamat.get())

    if itemNama == "" or itemNim == " ":
        showwarning(message="Field nama tidak boleh koson!")
    if itemNim == "" or itemNim == " ":
        showwarning(message="Field nim tidak boleh koson!")
    if itemJurusan == "" or itemJurusan == " ":
        showwarning(message="Field jurusan tidak boleh koson!")
    if itemAlamat == "" or itemAlamat == " ":
        showwarning(message="Field alamat tidak boleh koson!")
    else:
        insert(str(itemNama), str(itemNim), str(itemJurusan), str(itemAlamat))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

# Fungsi Untuk Menghapus Data Ke Dalam SQLITE
def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    # Melakukan perulangan untuk mengambil data yang ada pada variabel my_tree
    for data in my_tree.get_children():
        my_tree.delete(data)

    # Melakukan perulangan untuk membaca data yang di ambil dari fungsi read()
    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    # Mengatur Area Tempat Menampilkan Datanya.
    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

# Fungsi Untuk Mengedit Data Ke Dalam SQLITE
def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryNama.get(), entryNim.get(), entryJurusan.get(), entryAlamat.get(), update_name)
    
    # Melakukan perulangan untuk mengambil data yang ada pada variabel my_tree
    for data in my_tree.get_children():
        my_tree.delete(data)

    # Melakukan perulangan untuk membaca data yang di ambil dari fungsi read()
    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    # Mengatur Area Tempat Menampilkan Datanya.
    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

# Membuat judul atau heading yang diambil dari variavel storeName
titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

# Membuat Label.
namaLabel = Label(root, text="Nama", font=('Arial bold', 15))
nimLabel = Label(root, text="Nim", font=('Arial bold', 15))
jurusanLabel = Label(root, text="Jurusan", font=('Arial bold', 15))
alamatLabel = Label(root, text="Alamat", font=('Arial bold', 15))
namaLabel.grid(row=1, column=0, padx=10, pady=10)
nimLabel.grid(row=2, column=0, padx=10, pady=10)
jurusanLabel.grid(row=3, column=0, padx=10, pady=10)
alamatLabel.grid(row=4, column=0, padx=10, pady=10)

# Membuat Entry untuk meminta inputan dari user interface.
entryNama = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryNim = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryJurusan = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryAlamat = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryNama.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryNim.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryJurusan.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryAlamat.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

# Membuat Button untuk fitur tambah data(insert data)
buttonEnter = Button(
    root, text="Tambah", padx=10, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=5, column=1, columnspan=1)

# Membuat Button untuk fitur edit data(update data)
buttonUpdate = Button(
    root, text="Edit", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=5, column=2, columnspan=1)

# Membuat Button untuk fitur hapus data(delete data)
buttonDelete = Button(
    root, text="Hapus", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=5, column=3, columnspan=1)

# Membuat area untuk tempat menampilkan datanya.
style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("Nama", "Nim", "Jurusan", "Alamat")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Nama", anchor=W, width=150)
my_tree.column("Nim", anchor=W, width=150)
my_tree.column("Jurusan", anchor=W, width=200)
my_tree.column("Alamat", anchor=W, width=200)
my_tree.heading("Nama", text="Nama", anchor=W)
my_tree.heading("Nim", text="Nim", anchor=W)
my_tree.heading("Jurusan", text="Jurusan", anchor=W)
my_tree.heading("Alamat", text="Alamat", anchor=W)

# Melakukan perulangan untuk mengambil data yang ada pada variabel my_tree
for data in my_tree.get_children():
    my_tree.delete(data)

# Melakukan perulangan untuk membaca data yang di ambil dari fungsi read()
for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

# Mengatur Area Tempat Menampilkan Datanya.
my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)



root.mainloop()

