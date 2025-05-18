import tkinter as tk
from tkinter import ttk, messagebox

# Extended exchange rates relative to USD (base)
usd_rates = {
    "USD": 1.0,
    "INR": 83.50,
    "EUR": 0.92,
    "GBP": 0.80,
    "JPY": 134.50,
    "CHF": 0.91,
    "CAD": 1.34,
    "AUD": 1.50,
    "NZD": 1.63,
    "ZAR": 18.70,
    "CNY": 7.15,
    "SGD": 1.35,
    "MXN": 17.70,
    "SEK": 10.20,
    "NOK": 10.60,
    "BRL": 5.15,
    "RUB": 90.00,
    "TRY": 26.0
}

# We'll compute cross rates dynamically using USD as intermediary for simplicity
def get_exchange_rate(base_currency, target_currency):
    if base_currency not in usd_rates or target_currency not in usd_rates:
        return None
    # Convert base to USD, then USD to target
    rate = (1 / usd_rates[base_currency]) * usd_rates[target_currency]
    return rate

def convert_currency(event=None):
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()
    amount = amount_entry.get()

    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
    except ValueError:
        original_value_label.config(text="")
        result_value_label.config(text="")
        return

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        original_value_label.config(text=f"{amount:.2f} {base_currency}")
        result_value_label.config(text=f"{converted_amount:.2f} {target_currency}")
    else:
        original_value_label.config(text="")
        result_value_label.config(text="")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("700x350")
root.configure(bg="#f0f4f7")

currency_codes = sorted(usd_rates.keys())

container = tk.Frame(root, bg="#f0f4f7")
container.place(relx=0.5, rely=0.5, anchor="center")

input_frame = tk.Frame(container, bg="#f0f4f7")
input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

result_frame = tk.Frame(container, bg="#f0f4f7")
result_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")

header_label = tk.Label(input_frame, text="Currency Converter", font=("Segoe UI", 20, "bold"), bg="#f0f4f7", fg="#1a73e8")
header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

amount_label = tk.Label(input_frame, text="Amount:", font=("Segoe UI", 12), bg="#f0f4f7")
amount_label.grid(row=1, column=0, sticky="w")
amount_entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=15, bd=2, relief="groove")
amount_entry.grid(row=1, column=1, pady=5)

base_currency_label = tk.Label(input_frame, text="From Currency:", font=("Segoe UI", 12), bg="#f0f4f7")
base_currency_label.grid(row=2, column=0, sticky="w")
base_currency_var = tk.StringVar(value="USD")
base_currency_menu = ttk.Combobox(input_frame, textvariable=base_currency_var, values=currency_codes, state="readonly", font=("Segoe UI", 12), width=13)
base_currency_menu.grid(row=2, column=1, pady=5)

target_currency_label = tk.Label(input_frame, text="To Currency:", font=("Segoe UI", 12), bg="#f0f4f7")
target_currency_label.grid(row=3, column=0, sticky="w")
target_currency_var = tk.StringVar(value="INR")
target_currency_menu = ttk.Combobox(input_frame, textvariable=target_currency_var, values=currency_codes, state="readonly", font=("Segoe UI", 12), width=13)
target_currency_menu.grid(row=3, column=1, pady=5)

result_header_label = tk.Label(result_frame, text="Conversion Result", font=("Segoe UI", 18, "bold"), bg="#f0f4f7", fg="#2e7d32")
result_header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

original_label = tk.Label(result_frame, text="Original Amount:", font=("Segoe UI", 14), bg="#f0f4f7")
original_label.grid(row=1, column=0, sticky="e", padx=(0,10))
original_value_label = tk.Label(result_frame, text="", font=("Segoe UI", 14, "bold"), bg="#f0f4f7", fg="#1a237e")
original_value_label.grid(row=1, column=1, sticky="w")

converted_label = tk.Label(result_frame, text="Converted Amount:", font=("Segoe UI", 14), bg="#f0f4f7")
converted_label.grid(row=2, column=0, sticky="e", padx=(0,10), pady=(10,0))
result_value_label = tk.Label(result_frame, text="", font=("Segoe UI", 14, "bold"), bg="#f0f4f7", fg="#2e7d32")
result_value_label.grid(row=2, column=1, sticky="w", pady=(10,0))

amount_entry.bind("<KeyRelease>", convert_currency)
base_currency_menu.bind("<<ComboboxSelected>>", convert_currency)
target_currency_menu.bind("<<ComboboxSelected>>", convert_currency)

convert_currency()

root.mainloop()
