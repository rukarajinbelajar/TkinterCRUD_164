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