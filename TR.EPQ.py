import tkinter as tk
from tkinter import ttk, messagebox
import math

def calculate():
    try:
        talep = int(entry_talep.get())
        uretim_hizi = int(entry_uretim_hizi.get())
        birim_uretim_maliyeti = float(entry_birim_uretim_maliyeti.get())
        setup_maliyeti = float(entry_setup_maliyeti.get())
        elde_bulundurma_yuzdesi = float(entry_elde_bulundurma_yuzdesi.get())
        
        hazirlik_maliyeti = setup_maliyeti
        EOQ = math.sqrt((2 * talep * setup_maliyeti) / ((elde_bulundurma_yuzdesi * birim_uretim_maliyeti) * (1 - (talep / uretim_hizi))))
        optimal_uretim_suresi = EOQ / uretim_hizi * 365
        optimal_envanter_cevrim_suresi = (EOQ / talep) * 365
        toplam_maliyet = (talep * birim_uretim_maliyeti) + (setup_maliyeti * (talep / EOQ)) + ((EOQ * elde_bulundurma_yuzdesi * birim_uretim_maliyeti) / 2)
        
        result_window = tk.Toplevel(root)
        result_window.title("Sonuçlar")
        ttk.Label(result_window, text="a. Ekonomik Üretim Boyutu (EPQ):").grid(row=0, column=0, sticky="w")
        ttk.Label(result_window, text=f"{EOQ:.2f}").grid(row=0, column=1, sticky="w")
        ttk.Label(result_window, text="b. Optimal Üretim Süresi:").grid(row=1, column=0, sticky="w")
        ttk.Label(result_window, text=f"{optimal_uretim_suresi:.2f}").grid(row=1, column=1, sticky="w")
        ttk.Label(result_window, text="c. Optimal Envanter Çevrim Süresi:").grid(row=2, column=0, sticky="w")
        ttk.Label(result_window, text=f"{optimal_envanter_cevrim_suresi:.2f}").grid(row=2, column=1, sticky="w")
        ttk.Label(result_window, text="d. Toplam Maliyet:").grid(row=3, column=0, sticky="w")
        ttk.Label(result_window, text=f"{toplam_maliyet:.2f}").grid(row=3, column=1, sticky="w")
        
    except ValueError as e:
        messagebox.showerror("Hata", "Lütfen geçerli değerler girin.")

root = tk.Tk()
root.title("Stok Planlama Hesaplayıcı")


ttk.Label(root, text="Talep:").grid(row=0, column=0, sticky="e")
entry_talep = ttk.Entry(root)
entry_talep.grid(row=0, column=1)

ttk.Label(root, text="Üretim Hızı:").grid(row=1, column=0, sticky="e")
entry_uretim_hizi = ttk.Entry(root)
entry_uretim_hizi.grid(row=1, column=1)

ttk.Label(root, text="Birim Üretim Maliyeti:").grid(row=2, column=0, sticky="e")
entry_birim_uretim_maliyeti = ttk.Entry(root)
entry_birim_uretim_maliyeti.grid(row=2, column=1)

ttk.Label(root, text="Set-up Maliyeti:").grid(row=3, column=0, sticky="e")
entry_setup_maliyeti = ttk.Entry(root)
entry_setup_maliyeti.grid(row=3, column=1)

ttk.Label(root, text="Elde Bulundurma Yüzdesi:").grid(row=4, column=0, sticky="e")
entry_elde_bulundurma_yuzdesi = ttk.Entry(root)
entry_elde_bulundurma_yuzdesi.grid(row=4, column=1)

calculate_button = ttk.Button(root, text="Hesapla", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
