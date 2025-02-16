import random
import tkinter as tk
from tkinter import messagebox
import ctypes


number = random.randint(1, 1000)


def new_game():
    global number, attempt_count
    number = random.randint(1, 1000)  # New random number
    attempt_count = 0  # Reset attempt counter
    label_result.config(text="")  # Clear result label
    entry.delete(0, tk.END)  # Clear input field
    messagebox.showinfo("🔄 Restart!", "Jeszcze Raz ")

def hint(guess, number):
    difference = abs(guess-number)
    if difference >=100:
        return " ❄️ Zimno "
    elif difference >=10:
        return " 🌡️ Cieplej! "
    else:
        return " 🔥 Gorąco! " 


def check_guess():
    user_input = entry.get()
    attempt_count +=1

    if user_input.lower()=="exit":
        root.destroy()  #zamyka okno


    try: 
        guess=int(user_input)
        
        if guess < 1 or guess > 1000:
            label_result.config(text="❌ Zła liczba, podaj liczbe w zakresie 1-1000.", fg="red")
            return

        if guess > number:
            label_result.config(text=f"⬆️ Za duzo! {hint(guess, number)}", fg="blue")
        elif guess < number:
            label_result.config(text=f"⬇️ Za malo! {hint(guess, number)}", fg="blue")
        else:
            messagebox.showinfo("Wygrana!", "🎉 Poggers, zgadles!")
            new_game() #restart


    except ValueError:
        label_result.config(text="❌ Liczba mordo :3", fg="red")

#creates a window
root = tk.Tk()
root.title("Zgadnij liczbe! ")
root.geometry("450x350")
root.configure(bg="#f0f0f0")  # Light grey background

# UI Elements
label_title = tk.Label(root, text="🎯 Zgadnij liczbę (1-1000)", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333")
label_title.pack(pady=10) #text

entry = tk.Entry(root, font=("Arial", 14), justify="center", bg="#ffffff", fg="#333", relief="solid", bd=2)
entry.pack(pady=5, ipadx=5, ipady=5) #input

btn_guess = tk.Button(root, text="🔍 Zgadnij", command=check_guess, font=("Arial", 12), bg="#5cacee", fg="white", relief="flat", padx=10, pady=5)
btn_guess.pack(pady=5) #guzik zgadywania

label_result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
label_result.pack(pady=5) #output

btn_restart = tk.Button(root, text="🔄 Restart", command=new_game, font=("Arial", 12), bg="#ffcc00", fg="black", relief="flat", padx=10, pady=5)
btn_restart.pack(pady=5)  #guzik reset

btn_exit = tk.Button(root, text="❌ Wyjście", command=root.quit, font=("Arial", 12), fg="white", bg="#ff4c4c", relief="flat", padx=10, pady=5)
btn_exit.pack(pady=10) #guzik wyjscie

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("GuessGame")
root.iconbitmap("Ikona.ico")  # force zmiany na taskbarze


#run
root.mainloop()