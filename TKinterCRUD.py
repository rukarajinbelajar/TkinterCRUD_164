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
