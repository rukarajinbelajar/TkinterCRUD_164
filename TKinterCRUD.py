import tkinter as tk
from tkinter import messagebox 
import sqlite3

def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists nilai_siswa (
            id integer primary key autoincrement,
            nama_siswa tect not null,
            biologi integer not null,
            fisika integer not null,
            inggris integer not null,
            prediksi_fakultas text not null
            )
        """)
    conn.commit()
    conn.close()

create_db()

def prediksi_fakultas(biologi,fisika,inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak Dapat ditemukan"

def submit_nilai():
    nama = entry_nama.get().strip()
    try:
        bio = int(entry_bio.get())
        fis = int(entry_fis.get())
        ing = int(entry_ing.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai harus berupa angka!")
        return

    hasil_prediksi = prediksi_fakultas(bio, fis, ing)

    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute("""
        insert into nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        values (?, ?, ?, ?, ?)
    """, (nama, bio, fis, ing, hasil_prediksi))
    conn.commit()
    conn.close()

    messagebox.showinfo("Hasil Prediksi", f"Prediksi fakultas: {hasil_prediksi}")

    entry_nama.delete(0, tk.end)
    entry_bio.delete(0, tk.end)
    entry_fis.delete(0, tk.end)
    entry_ing.delete(0, tk.end)

def on_enter(e):
    btn_submit["bg"] = "#50fa7b"
    btn_submit["fg"] = "black"

def on_leave(e):
    btn_submit["bg"] = "#44475a"
    btn_submit["fg"] = "black"

#======== TAMPILAN GUI=======#
BG = "#ffe4ec"
HEADER = "#ff69b4"
CARD = "#fff5f8"
TEKS = "#8b1a4a"
 
root = tk.Tk()
root.title("Prediksi Fakultas Siswa")
root.geometry("440x600")
root.configure(bg=BG)
root.resizable(False, False)
root.columnconfigure(0, weight=1)