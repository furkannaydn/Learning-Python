from tkinter import *
from tkinter import messagebox
import base64
import os

# === Şifreleme Fonksiyonları (Vigenere Cipher) ===
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

# === Dosya Konumu (Masaüstü) ===
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "mysecret.txt")

# === Notları Kaydet ve Şifrele ===
def save_and_encrypt_notes():
    title = title_entry.get().strip()
    message = input_text.get("1.0", END).strip()
    master_secret = master_secret_input.get().strip()

    if not title or not message or not master_secret:
        messagebox.showerror(title="Hata!", message="Lütfen tüm bilgileri girin!")
        return

    # Mesajı şifrele
    message_encrypted = encode(master_secret, message)

    try:
        with open(desktop_path, "a") as data_file:
            data_file.write(f'\n---\n{title}\n{message_encrypted}\n')
        messagebox.showinfo("Başarılı!", "Not kaydedildi ve şifrelendi!")
    except Exception as e:
        messagebox.showerror("Hata!", f"Dosya kaydedilirken bir hata oluştu: {e}")

    # Alanları temizle
    title_entry.delete(0, END)
    master_secret_input.delete(0, END)
    input_text.delete("1.0", END)

# === Notları Şifre Çöz ===
def decrypt_notes():
    master_secret = master_secret_input.get().strip()

    if not master_secret:
        messagebox.showerror(title="Hata!", message="Lütfen şifre anahtarınızı girin.")
        return

    try:
        with open(desktop_path, "r") as data_file:
            lines = data_file.readlines()

        decrypted_text = ""
        for line in lines:
            line = line.strip()
            
            # Eğer satır boşsa veya ayırıcı çizgiyse atla
            if not line or line.startswith("-"):
                continue  

            try:
                decoded_line = decode(master_secret, line)
                
                # Eğer decode başarılı olduysa ekle
                if decoded_line:
                    decrypted_text += decoded_line + "\n"

            except Exception:
                pass  # Hatalı satırları atla

        if decrypted_text:
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_text)
        else:
            messagebox.showerror("Hata!", "Şifre çözme başarısız! Bilgilerinizi kontrol edin.")
    except FileNotFoundError:
        messagebox.showerror("Hata!", "Dosya bulunamadı!")

# === Arayüz (UI) ===
window = Tk()
window.title("Gizli Notlar")
window.config(padx=30, pady=30)

canvas = Canvas(height=100, width=100)
logo = PhotoImage(file=r"C:\Users\faydn\OneDrive\Desktop\secret_notes\top_secret_small.png")
canvas.create_image(50, 50, image=logo)
canvas.pack()

title_info_label = Label(text="Başlık Giriniz:", font=("Verdana", 12, "normal"))
title_info_label.pack()

title_entry = Entry(width=40)
title_entry.pack()

input_info_label = Label(text="Gizli Notunuzu Giriniz:", font=("Verdana", 12, "normal"))
input_info_label.pack()

input_text = Text(width=50, height=10)
input_text.pack()

master_secret_label = Label(text="Şifre Anahtarınızı Girin:", font=("Verdana", 12, "normal"))
master_secret_label.pack()

master_secret_input = Entry(width=30, show="*")  # Şifre gizli girilecek
master_secret_input.pack()

save_button = Button(text="Kaydet & Şifrele", command=save_and_encrypt_notes)
save_button.pack(pady=5)

decrypt_button = Button(text="Şifreyi Çöz", command=decrypt_notes)
decrypt_button.pack()

window.mainloop()
