import tkinter as tk
import random
from datetime import datetime
import time
from tkinter import messagebox

def generate_random_number():
    try:
        with open('output.txt', 'a') as file:
            lower_bound = int(min_value.get())
            upper_bound = int(max_value.get())
            k = int(num_value.get())
            if prime_var.get():
                lst = []
                while len(lst) < k:
                    random_number = random.randint(lower_bound, upper_bound)
                    ok = 1
                    for d in range(2,int(random_number/2)+1):
                        if random_number % d == 0:
                            ok = 0
                            break
                    if ok == 0:
                        continue
                    else:
                        lst.append(random_number)
                now = datetime.now()
                data_time = now.strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{data_time} ->{lst}\n")
            if even_var.get():
                lst = []
                while len(lst) < k:
                    random_number = random.randint(lower_bound, upper_bound)
                    if random_number % 2 != 0:
                        continue
                    else:
                        lst.append(random_number)
                now = datetime.now()
                data_time = now.strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{data_time} ->{lst}\n")
            if odd_var.get():
                lst = []
                while len(lst) < k:
                    random_number = random.randint(lower_bound, upper_bound)
                    if random_number % 2 == 0:
                        continue
                    else:
                        lst.append(random_number)
                now = datetime.now()
                data_time = now.strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{data_time} ->{lst}\n")
            result_label.config(text=f"{lst}", font=('Arial', 14), bg='#BD9289')
    except ValueError:
        result_label.config(text="Please enter valid integers for the interval", bg='#BD9289')

root = tk.Tk()
root.geometry("420x350")
root.title('Generator de numere')
root.resizable(False, False)  # nu mai pot sa modific dimensiunile

main_frame = tk.Frame(root, width=420, height=350, bg='#BD9289')
main_frame.grid(row=0, column=0)

tk.Label(main_frame, text="Alegeti tipul de numar:", font=('Arial', 12), bg='#AD7B71').grid(row=0, column=0)

minim = tk.Label(main_frame, text="Min: ", font=('Arial', 12), bg='#AD7B71')
minim.grid(row=6, column=0, padx=3, pady=3)

maxim = tk.Label(main_frame, text="Max: ", font=('Arial', 12), bg='#AD7B71')
maxim.grid(row=7, column=0, padx=5, pady=5)

min_value = tk.Entry(main_frame, font=('Arial', 12), fg='black')
min_value.grid(row=6, column=1, padx=3, pady=3)

max_value = tk.Entry(main_frame, font=('Arial', 12), fg='black')
max_value.grid(row=7, column=1, padx=5, pady=5)

tk.Label(main_frame, text="Numarul de numere generate:", font=('Arial', 12), bg='#AD7B71').grid(row=4, column=0)
num_value = tk.Entry(main_frame, font=('Arial', 12))
num_value.grid(row=4, column=1, padx=5, pady=5)

prime_var = tk.BooleanVar()
prime_checkbox = tk.Checkbutton(main_frame, text="Numar prim ", font=('Arial', 14), bg='#BD9289', variable=prime_var)
prime_checkbox.grid(row=1, column=0, columnspan=4)

even_var = tk.BooleanVar()
even_checkbox = tk.Checkbutton(main_frame, text="Numar par",  font=('Arial', 14), bg='#BD9289', variable=even_var)
even_checkbox.grid(row=2, column=0, columnspan=4)

odd_var = tk.BooleanVar()
odd_checkbox = tk.Checkbutton(main_frame, text="Numar impar",  font=('Arial', 14), bg='#BD9289', variable=odd_var)
odd_checkbox.grid(row=3, column=0, columnspan=4)

tk.Button(main_frame, text='Generate', command=generate_random_number).grid(row=8, column=1, sticky=tk.E + tk.W)  # sticky modifica dimensiunea butonului facand-o egala cu intrarea

# Create a label to display the result
tk.Label(main_frame, text="Random number: ", font=('Arial', 12), bg='#AD7B71').grid(row=9, column=0)
result_label = tk.Label(main_frame, text="", bg='#BD9289')
result_label.grid(row=9, column=1, sticky=tk.E + tk.W)


main_frame.grid_propagate(False) #dim sau proprietatile frame ului meu nu vor mai fi modificate de catre widgeturile adaugate

with open('output.txt','w') as file:
    pass

#
# Mini-joc de ghicit numere
global secret_num
first = 0
second = 200
secret_num = random.randint(first, second)
print(secret_num)

def verificare():
    guess = int(guess_value.get())
    if guess == num_value:
        result_label2.config(text='Felicitari! Ai ghicit din prima', font=('Helvetica',14))
    else:
        repeat()

global nr_incercari
nr_incercari = 0

def repeat():
    guess = int(guess_value.get())
    if guess < secret_num:
        result_label2.config(text='Valoarea introdusa este prea mica', font=('Helvetica',14))
        nr_incercari +=1
    else:
        result_label2.config(text='Valoarea introdusa este prea mare', font=('Helvetica', 14))
        nr_incercari += 1
    guess_value.delete(0, 'end')

root2 = tk.Tk()
root2.geometry("600x200")
root2.title('Mini-joc')
root2.resizable(False, False)  # nu mai pot sa modific dimensiunile

second_frame = tk.Frame(root2, width=600, height=200, bg='#84C1EE')
second_frame.grid(row=0)

#label1 = tk.Label(second_frame, text='Scopul jocului este sa ghiciti numarul generat', font=('Helvetica', 14), bg='#84C1EE')
#label1.grid(row=0, column=0)

guess_label = tk.Label(second_frame, text='Introduceti un numar:', font=('Helvetica',14), bg='#84C1EE')
guess_label.grid(row=1, column=0)

guess_value = tk.Entry(second_frame, font=('Helvetica',14), bg='#649DC8', width=25)
guess_value.grid(row=1, column=1)

guess_button = tk.Button(second_frame, text='Check', command=verificare)
guess_button.grid(row=2, column=1)

result_label2 = tk.Label(second_frame, text="", bg='#84C1EE')
result_label2.grid(row=3, column=1)

second_frame.grid_propagate(False)

root.mainloop()
root2.mainloop()