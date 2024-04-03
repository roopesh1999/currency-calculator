from tkinter import *
mw = Tk()
mw.title("Currency calculator")
mw.geometry("300x200")

CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

# Write code here
def to_usd(currency_code, amount):
    if currency_code not in CURRENCIES.keys():      
        raise Exception(f"{currency_code} is not supported")
    elif amount < 0:
        raise Exception("Invalid amount")
    else:
        temp = CURRENCIES[currency_code]
        res = amount * temp
        return res

def from_usd(currency_code, amount):
    if currency_code not in CURRENCIES.keys():
        raise Exception(f"{currency_code} is not supported")
    elif amount < 0:
        raise Exception("Invalid amount")
    else:
        temp = CURRENCIES[currency_code]
        res = amount / temp
        return res

def convert(from_currency, amount, to_currency):
    try:
        if to_currency == "USD":
            res = to_usd(from_currency, amount)
            output_label.config(text=f"{amount} {from_currency} is {round(res,4)} {to_currency}")
        elif from_currency == "USD":
            res = from_usd(to_currency, amount)
            output_label.config(text=f"{amount} {from_currency} is {round(res,4)} {to_currency}")
        else:
            if from_currency not in CURRENCIES.keys():
                raise Exception(f"{from_currency} is not supported")
            elif to_currency not in CURRENCIES.keys():
                raise Exception(f"{to_currency} is not supported")                
            elif amount < 0:
                raise Exception("Invalid amount")
            else:
                from_currency_price = CURRENCIES[from_currency]
                to_currency_price = CURRENCIES[to_currency]
                res = amount * from_currency_price / to_currency_price
                output_label.config(text=f"{amount} {from_currency} is {round(res, 4)} {to_currency}")
    except Exception as e:
        output_label.config(text=str(e))

def get_output(event=None):
    from_currency = from_currency_var.get()
    amount_str = input2.get()
    to_currency = to_currency_var.get()
    if from_currency !='' and amount_str !='' and to_currency !='':
        try:
            amount = float(amount_str)
            convert(from_currency, amount, to_currency)
        except ValueError:
            output_label.config(text="Enter a valid amount")

# label1 = Label(mw, text='Convert from:', font=('Arial', 12))
# label1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# label2 = Label(mw, text='Convert to:', font=('Arial', 12))
# label2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

label1 = Label(mw, text='Enter amount:', font=('Arial', 12))
label1.grid(row=0, column=0, padx=10, pady=5, sticky='w')

input2 = Entry(mw, width=10, font=('Arial', 10))
input2.grid(row=0, column=1, sticky='w')

from_currency_var = StringVar(mw)
from_currency_var.set("USD")
from_currency_option = OptionMenu(mw, from_currency_var, *CURRENCIES.keys())
from_currency_option.grid(row=1, column=0, padx=30, pady=10, sticky='w')

label1 = Label(mw, text='⏩', font=('Calibri', 12))
label1.grid(row=1, column=1, padx=20, pady=5, sticky='w')

to_currency_var = StringVar(mw)
to_currency_var.set("USD")
to_currency_option = OptionMenu(mw, to_currency_var, *CURRENCIES.keys())
to_currency_option.grid(row=1, column=2, padx=10, pady=10, sticky='w')

btn = Button(mw, text='Convert', font=('Arial', 12), command=get_output)
btn.grid(row=3, column=1, columnspan=2, pady=5, sticky='w')

output_label = Label(mw, text='', font=('Arial', 12))
output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='w')
    
mw.mainloop()