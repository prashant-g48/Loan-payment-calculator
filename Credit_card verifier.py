#credit card script
import tkinter as tk
from tkinter import messagebox

def show_details():
    card_name = name_entry.get()
    card_num = number_entry.get()
    expiry = expiry_entry.get()
    cvv = cvv_entry.get()

    if not (card_name and card_num and expiry and cvv):
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return

    # New window to display card details
    top = tk.Toplevel(root)
    top.title("Credit Card Preview")
    top.geometry("300x200")

    tk.Label(top, text="Credit Card Details", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(top, text=f"Name: {card_name}").pack()
    tk.Label(top, text=f"Number: {'*' * 12 + card_num[-4:]}").pack()
    tk.Label(top, text=f"Expiry: {expiry}").pack()
    tk.Label(top, text=f"CVV: {'*' * len(cvv)}").pack()

# Main window
root = tk.Tk()
root.title("Credit Card Form")
root.geometry("350x250")

tk.Label(root, text="Enter Credit Card Information", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Cardholder Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Card Number").pack()
number_entry = tk.Entry(root)
number_entry.pack()

tk.Label(root, text="Expiry Date (MM/YY)").pack()
expiry_entry = tk.Entry(root)
expiry_entry.pack()

tk.Label(root, text="CVV").pack()
cvv_entry = tk.Entry(root, show="*")
cvv_entry.pack()

tk.Button(root, text="Submit", command=show_details).pack(pady=15)

root.mainloop()
