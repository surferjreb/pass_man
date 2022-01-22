from tkinter import Label
from tkinter import Entry
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
from random import choice
from random import randint
from random import shuffle
import pyperclip
import json

"""Locally saved JSON file of passwords"""
FILE_PATH = "data.json"


# ---------------------------- PASSWORD GENERATOR --------------------------- #
def generate_password():
    new_pass_list = []
    new_pass = ''
    pass_letters_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                      'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                      'w', 'x', 'y', 'z',
                      ]
    pass_letters_u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                      'V', 'W', 'X', 'Y', 'Z',
                      ]
    pass_symbols = ['!', '@', '#', '$', '&', '*', '#']
    pass_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    lower_letters = [choice(pass_letters_l) for _ in range(randint(8, 10))]
    upper_letters = [choice(pass_letters_u) for _ in range(randint(1, 2))]
    symbols = [choice(pass_symbols) for _ in range(randint(1, 2))]
    pass_numbers = [choice(pass_numbers) for _ in range(randint(1, 2))]

    new_pass_list = lower_letters + upper_letters + symbols + pass_numbers

    shuffle(new_pass_list)
    new_pass = ''.join(new_pass_list)
    pyperclip.copy(new_pass)
    return new_pass


# ---------------------------- SAVE PASSWORD -------------------------------- #
def write_info(web_input, user_input, pass_input):

    new_data = {
        web_input: {
            "Email": user_input,
            "Password": pass_input,
        },
    }

    if len(web_input) == 0 or len(pass_input) == 0:
        messagebox.showinfo(title="Oh No!",
                            message="Make sure there are no blank fields...")
    else:
        try:
            with open(FILE_PATH, 'r') as json_data:
                data = json.load(json_data)

        except FileNotFoundError:
            with open(FILE_PATH, 'w') as json_data:
                json.dump(new_data, json_data, indent=4)

        else:
            if web_input in data:
                messagebox.showinfo(title="Already Exists",
                                    message="Try searching...")
            else:
                data.update(new_data)

                with open(FILE_PATH, 'w') as json_data:
                    json.dump(data, json_data, indent=4)

# ----------------------------- SEARCH -------------------------------------- #


def search_data(user_web):
    try:
        with open(FILE_PATH, 'r') as json_data:
            data = json.load(json_data)

            if user_web in data:
                user_email = data[user_web]["Email"]
                user_pass = data[user_web]["Password"]
            else:
                raise KeyError

    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message="File not Found")
    except KeyError:
        messagebox.showinfo(title="Error",
                            message="Website not in File")
    else:
        return (user_email, user_pass)

# ---------------------------- UI SETUP ------------------------------------- #


def main():
    # Window settings
    window = Tk()
    window.title("PassMaster")
    window.config(padx=20, pady=20)

    # Canvas
    canvas = Canvas(width=220, height=220, highlightthickness=0)
    pass_img = PhotoImage(file="logo.png")
    canvas.create_image(110, 110, image=pass_img)

    # Labels
    web_label = Label(text="Website: ")
    user_label = Label(text="Email/Username: ")
    pass_label = Label(text="Password: ")

    # Entry
    web_input = Entry(width=35)
    web_input.focus()
    user_input = Entry(width=47)
    user_input.insert(0, "someone@example.com")
    pass_input = Entry(width=35)

    def save_info():
        write_info(web_input.get(), user_input.get(), pass_input.get())
        web_input.delete(0, "end")
        pass_input.delete(0, "end")

    def make_pass():
        new_pass = generate_password()
        pass_input.insert(0, new_pass)

    def search_info():
        info = search_data(web_input.get())
        user_input.delete(0, "end")
        pass_input.delete(0, "end")
        user_input.insert(0, info[0])

        pass_input.insert(0, info[1])

    # Button
    gen_pass = Button(text="Generate Pass", width=10,
                      command=make_pass)
    add_entry = Button(text="Add", width=36, command=save_info)
    search_b = Button(text="Search", width=10, command=search_info)

    # Alignment
    canvas.grid(column=1, row=0)
    web_label.grid(column=0, row=1)
    web_input.grid(column=1, row=1)
    user_label.grid(column=0, row=2)
    user_input.grid(column=1, row=2, columnspan=2)
    pass_label.grid(column=0, row=3)
    pass_input.grid(column=1, row=3, columnspan=1)
    gen_pass.grid(column=2, row=3, columnspan=1)
    add_entry.grid(column=1, row=4, columnspan=2)
    search_b.grid(column=2, row=1)

    window.mainloop()


if __name__ == '__main__':
    main()
