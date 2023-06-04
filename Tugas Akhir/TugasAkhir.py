import tkinter as tk
from tkinter import messagebox
from collections import deque

class User:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin

class MoneyChangerApp:
    def __init__(self):
        self.saldo = 0  
        self.main_window = None
        self.transaksi_stack = deque()  
        self.users = [
            User("Ivan", "100304")  
        ]

        self.login_window = tk.Tk()
        self.login_window.title("Sitorus Money Changer - Login")
        self.login_window.geometry("600x500")
        self.login_window.configure(bg="light blue")

        label_username = tk.Label(self.login_window, text="Username:", font=("Helvetica", 20), bg="light blue")
        label_username.pack(pady=10)
        self.entry_username = tk.Entry(self.login_window, font=("Helvetica", 20))
        self.entry_username.pack(pady=5)

        label_pin = tk.Label(self.login_window, text="PIN:", font=("Helvetica", 20), bg="light blue")
        label_pin.pack(pady=10)
        self.entry_pin = tk.Entry(self.login_window, show="*", font=("Helvetica", 20))
        self.entry_pin.pack(pady=5)

        button_login = tk.Button(self.login_window, text="Login", command=self.login, font=("Arial", 20), )
        button_login.pack(pady=20)

        button_create_account = tk.Button(self.login_window, text="Buat Akun Baru", command=self.show_create_account_window, font=("Arial", 20))
        button_create_account.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        pin = self.entry_pin.get()

        for user in self.users:
            if user.username == username and user.pin == pin:
                self.show_main_window()
                return

        messagebox.showerror("Error", "Maaf, username atau PIN tidak terdaftar!")

    def show_create_account_window(self):
        create_account_window = tk.Toplevel(self.login_window)
        create_account_window.title("Buat Akun Baru")
        create_account_window.geometry("600x400")
        create_account_window.configure(bg="light blue")

        label_username = tk.Label(create_account_window, text="Username:", font=("Helvetica", 20),bg="light blue")
        label_username.pack(pady=10)
        entry_username = tk.Entry(create_account_window, font=("Helvetica", 20))
        entry_username.pack(pady=5)

        label_pin = tk.Label(create_account_window, text="PIN:", font=("Helvetica", 20),bg="light blue")
        label_pin.pack(pady=10)
        entry_pin = tk.Entry(create_account_window, show="*", font=("Helvetica", 20))
        entry_pin.pack(pady=5)

        button_create = tk.Button(create_account_window, text="Buat Akun", command=lambda: self.create_account(entry_username.get(), entry_pin.get(), create_account_window), font=("Arial", 20))
        button_create.pack(pady=20)

    def create_account(self, username, pin):
        if username and pin:
            new_user = User(username, pin)
            self.users.append(new_user)
            messagebox.showinfo("Informasi", "Akun berhasil dibuat!")
            create_account_window.destroy()
        else:
            messagebox.showerror("Error", "Username dan PIN tidak boleh kosong!")

        

            

    def masukkan_uang(self):
        masukkan_uang_window = tk.Toplevel(self.main_window)
        masukkan_uang_window.title("Masukkan Uang Tunai")
        masukkan_uang_window.geometry("600x400")

        def submit_uang():
            nominal = int(entry_nominal.get())

            if nominal > 0:
                self.saldo += nominal
                self.transaksi_stack.append(f"Menambahkan {nominal} Rupiah ke saldo")
                messagebox.showinfo("Informasi", f"Transaksi Berhasil.\nSaldo Anda saat ini: {self.saldo} Rupiah")
            else:
                messagebox.showerror("Error", "Nominal tidak valid.")

            masukkan_uang_window.destroy()

        label_nominal = tk.Label(masukkan_uang_window, text="Nominal (Rupiah):",font=("Helvetica", 16))
        label_nominal.pack(pady=10)
        entry_nominal = tk.Entry(masukkan_uang_window)
        entry_nominal.pack(pady=5)

        button_submit = tk.Button(masukkan_uang_window, text="Submit", command=submit_uang, font=("Helvetica", 14))
        button_submit.pack(pady=10)

    def cek_kurs(self):
        cek_kurs_window = tk.Toplevel(self.main_window)
        cek_kurs_window.title("Cek Kurs")
        cek_kurs_window.geometry("800x600")

        label_kurs = tk.Label(cek_kurs_window, text="Kurs Mata Uang",font=("Helvetica", 25))
        label_kurs.pack(pady=30)

        label_dolar = tk.Label(cek_kurs_window, text="1 Dolar Amerika = 14,000 Rupiah",font=("Helvetica", 16))
        label_dolar.pack()

        label_euro = tk.Label(cek_kurs_window, text="1 Euro = 16,000 Rupiah", font=("Helvetica", 16))
        label_euro.pack()

        label_pondsterling = tk.Label(cek_kurs_window, text="1 Poundsterling = 18,000 Rupiah", font=("Helvetica", 16))
        label_pondsterling.pack()

    def cek_saldo(self):
        cek_saldo_window = tk.Toplevel(self.main_window)
        cek_saldo_window.title("Cek Saldo")
        cek_saldo_window.geometry("500x400")

        label_saldo = tk.Label(cek_saldo_window, text=f"Saldo Anda saat ini: {self.saldo} Rupiah", font=("Helvetica", 16))
        label_saldo.pack(pady=20)

    def tukar_uang(self):
        tukar_uang_window = tk.Toplevel(self.main_window)
        tukar_uang_window.title("Tukar Uang")
        tukar_uang_window.geometry("800x600")

        def submit_tukar_uang():
            nominal = int(entry_nominal.get())
            jenis_mata_uang = combo_mata_uang.get()
            kurs = 0

            if jenis_mata_uang == "Dolar Amerika":
                kurs = 14000
            elif jenis_mata_uang == "Euro":
                kurs = 16000
            elif jenis_mata_uang == "Poundsterling":
                kurs = 18000

            if nominal > self.saldo:
                messagebox.showerror("Error", "Saldo tidak mencukupi")

            elif nominal < 0:
                messagebox.showerror("Error", "Nominal tidak valid.")

            else:
                nilai_konversi = nominal / kurs
                self.saldo -= nominal

                review_window = tk.Toplevel(tukar_uang_window)
                review_window.title("Review Tukar Uang")
                review_window.geometry("600x400")

                label_konfirmasi = tk.Label(review_window, text=f"Apakah anda ingin melanjutkan transaksi?", font=("Helvetica", 16))
                label_konfirmasi.pack(pady=10)

                label_nama_nasabah = tk.Label(review_window, text=f"Nama Nasabah: {self.entry_username.get()}", font=("Helvetica", 16))
                label_nama_nasabah.pack(pady=10)

                label_nominal_review = tk.Label(review_window, text=f"Nominal (Rupiah): {nominal}", font=("Helvetica", 16))
                label_nominal_review.pack(pady=10)

                label_mata_uang_review = tk.Label(review_window, text=f"Jenis Mata Uang: {jenis_mata_uang}", font=("Helvetica", 16))
                label_mata_uang_review.pack(pady=10)

                label_konversi_review = tk.Label(review_window, text=f"Hasil Konversi: {nilai_konversi:.2f} {jenis_mata_uang}", font=("Helvetica", 16))
                label_konversi_review.pack(pady=10)

                def confirm_tukar_uang():
                    self.transaksi_stack.append(f"Menukar {nominal} Rupiah menjadi {nilai_konversi:.2f} {jenis_mata_uang}")
                    messagebox.showinfo("Informasi", f"Anda telah menukar uang sebesar {nominal} Rupiah menjadi {nilai_konversi:.2f} {jenis_mata_uang}.\nSilahkan ambil uang anda pada slot penarikan")
                    tukar_uang_window.destroy()
                    review_window.destroy()

                button_teruskan = tk.Button(review_window, text="Teruskan", command=confirm_tukar_uang, font=("Arial", 15))
                button_teruskan.pack(side="right", anchor="se", padx=10, pady=10)

                button_kembali = tk.Button(review_window, text="Kembali", command=review_window.destroy, font=("Arial", 15))
                button_kembali.pack(side="left", anchor="sw", padx=10, pady=10)
            

        label_nominal = tk.Label(tukar_uang_window, text="Nominal (Rupiah):",font=("Helvetica", 20))
        label_nominal.pack(pady=10)
        entry_nominal = tk.Entry(tukar_uang_window, font=("Helvetica",15 ))
        entry_nominal.pack(pady=5)

        label_mata_uang = tk.Label(tukar_uang_window, text="(Jenis Mata Uang)")
        label_mata_uang.pack(pady=10)
        combo_mata_uang = tk.StringVar()
        combo_mata_uang.set("Dolar Amerika")

        def update_label(*args):
            label_mata_uang.config(text=combo_mata_uang.get())

        combo_box = tk.OptionMenu(tukar_uang_window, combo_mata_uang, "Dolar Amerika", "Euro", "Poundsterling", command=update_label)
        combo_box.pack(pady=5)

        label_mata_uang = tk.Label(tukar_uang_window, text=combo_mata_uang.get())
        label_mata_uang.pack()


        button_submit = tk.Button(tukar_uang_window, text="Submit", command=submit_tukar_uang, font=("Helvetica", 13))
        button_submit.pack(pady=10)

    def transaksi_baru(self):
        self.saldo = 0
        self.transaksi_stack.clear()  
        messagebox.showinfo("Informasi", "Sisa saldo telah ditarik")

    def catatan_transaksi(self):
        catatan_transaksi_window = tk.Toplevel(self.main_window)
        catatan_transaksi_window.title("Catatan Transaksi")
        catatan_transaksi_window.geometry("400x400")

        label_title = tk.Label(catatan_transaksi_window, text="Catatan Transaksi", font=("Helvetica", 16))
        label_title.pack(pady=20)

        if self.transaksi_stack:
            transaksi_text = "\n".join(reversed(self.transaksi_stack))
        else:
            transaksi_text = "Tidak ada transaksi"

        label_transaksi = tk.Label(catatan_transaksi_window, text=transaksi_text)
        label_transaksi.pack()

    def show_main_window(self):
        self.login_window.withdraw()
        self.main_window = tk.Tk()
        self.main_window.title("Sitorus Money Changer")
        self.main_window.geometry("1200x800")

        label_title = tk.Label(self.main_window, text="Selamat Datang di Sitorus Money Changer", font=("Helvetica", 16))
        label_title.pack(pady=20)

        actions = [
            ("Masukkan Uang Tunai", self.masukkan_uang),
            ("Cek Kurs", self.cek_kurs),
            ("Cek Saldo", self.cek_saldo),
            ("Tukar Uang", self.tukar_uang),
            ("Tarik Sisa Saldo", self.transaksi_baru),  
            ("Catatan Transaksi", self.catatan_transaksi) 
        ]

        button_width = 20  
        button_height = 3  

        for action in actions:
            button = tk.Button(self.main_window, text=action[0], command=action[1], width=button_width,
                               height=button_height, font=("Arial", 15))
            button.pack(pady=10)

        button_exit = tk.Button(self.main_window, text="Keluar", command=self.main_window.destroy)
        button_exit.pack(side="bottom", anchor="sw", padx=20, pady=20)

    def login(self):
        username = self.entry_username.get()
        pin = self.entry_pin.get()

        for user in self.users:
            if user.username == username and user.pin == pin:
                self.show_main_window()
                return

        messagebox.showerror("Error", "Maaf, username atau PIN tidak terdaftar!")

    def show_create_account_window(self):
        create_account_window = tk.Toplevel(self.login_window)
        create_account_window.title("Buat Akun Baru")
        create_account_window.geometry("600x400")
        self.login_window.configure(bg="light blue")

        label_username = tk.Label(create_account_window, text="Username:", font=("Helvetica", 20))
        label_username.pack(pady=10)
        entry_username = tk.Entry(create_account_window, font=("Helvetica", 20))
        entry_username.pack(pady=5)

        label_pin = tk.Label(create_account_window, text="PIN:", font=("Helvetica", 20))
        label_pin.pack(pady=10)
        entry_pin = tk.Entry(create_account_window, show="*", font=("Helvetica", 20))
        entry_pin.pack(pady=5)

        button_create = tk.Button(create_account_window, text="Buat Akun", command=lambda: self.create_account(entry_username.get(), entry_pin.get()), font=("Arial", 20))
        button_create.pack(pady=20)

    def create_account(self, username, pin):
        if username and pin:
            new_user = User(username, pin)
            self.users.append(new_user)
            messagebox.showinfo("Informasi", "Akun berhasil dibuat!")
        else:
            messagebox.showerror("Error", "Username dan PIN tidak boleh kosong!")

    def run(self):
        self.login_window.mainloop()


if __name__ == "__main__":
    app = MoneyChangerApp()
    app.run()
