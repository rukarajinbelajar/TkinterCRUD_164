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

header = tk.Frame(root, bg=HEADER)
header.grid(row=0, column=0, sticky="ew")
header.columnconfigure(0, weight=1)
tk.Label(header, text="Prediksi Fakultas", font=("Arial", 20, "bold"),
         bg=HEADER, fg="white").grid(row=0, column=0, pady=(18, 2))
tk.Label(header, text="Masukkan nilaimu, temukan fakultas yang cocok",
         font=("Arial", 10, "italic"), bg=HEADER, fg="#fff0f5").grid(row=1, column=0, pady=(0, 15))

card = tk.Frame(root, bg=CARD, highlightbackground="#ffb6c1", highlightthickness=2)
card.grid(row=1, column=0, pady=25, padx=30, sticky="ew")
card.columnconfigure(0, weight=1)
 
 
def buat_entry(teks, baris):
    tk.Label(card, text=teks, font=("Arial", 11, "bold"),
             bg=CARD, fg=TEKS).grid(row=baris, column=0, pady=(12, 0))
    entry = tk.Entry(card, width=30, bg="white", fg=TEKS, font=("Arial", 11),
                     justify="center", bd=0, insertbackground="#ff1493",
                     highlightthickness=2, highlightbackground="#ffb6c1",
                     highlightcolor="#ff1493")
    entry.grid(row=baris + 1, column=0, ipady=5, pady=(3, 0), padx=25)
    return entry
 
 
