import tkinter
import pyperclip
from random import choice
from random import randint
from random import shuffle
from tkinter import messagebox


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
    file = "data.txt"

    if len(web_input) == 0 or len(pass_input) == 0:
        messagebox.showinfo(title="Oh No!",
                            message="Make sure there are no blank fields...")
    else:
        is_ok = messagebox.askokcancel(title=web_input,
                                       message=f"""User: \n{user_input}\n
                                                Password: \n{pass_input}\n"""
                                       )

    if is_ok:
        with open(file, 'a') as data:
            info = f"{web_input} \t| {user_input} \t| {pass_input}\n"
            data.write(info)

# ---------------------------- UI SETUP ------------------------------------- #


def main():
    # Window settings
    window = tkinter.Tk()
    window.title("PassMaster")
    window.config(padx=20, pady=20)

    # Canvas
    canvas = tkinter.Canvas(width=220, height=220, highlightthickness=0)
    pass_img = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(110, 110, image=pass_img)

    # Labels
    web_label = tkinter.Label(text="Website: ")
    user_label = tkinter.Label(text="Email/Username: ")
    pass_label = tkinter.Label(text="Password: ")

    # Entry
    web_input = tkinter.Entry(width=35)
    web_input.focus()
    user_input = tkinter.Entry(width=35)
    user_input.insert(0, "someone@example.com")
    pass_input = tkinter.Entry(width=21)

    def save_info():
        write_info(web_input.get(), user_input.get(), pass_input.get())
        web_input.delete(0, "end")
        pass_input.delete(0, "end")

    def make_pass():
        new_pass = generate_password()
        pass_input.insert(0, new_pass)

    # Button
    gen_pass = tkinter.Button(text="Generate Pass", width=10,
                              command=make_pass)
    add_entry = tkinter.Button(text="Add", width=36, command=save_info)

    # Alignment
    canvas.grid(column=1, row=0)
    web_label.grid(column=0, row=1)
    web_input.grid(column=1, row=1, columnspan=2)
    user_label.grid(column=0, row=2)
    user_input.grid(column=1, row=2, columnspan=2)
    pass_label.grid(column=0, row=3)
    pass_input.grid(column=1, row=3, columnspan=1)
    gen_pass.grid(column=2, row=3, columnspan=1)
    add_entry.grid(column=1, row=4, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()
