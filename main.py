from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','$','&','*','%','-']



    password_letters = [choice(letters) for _ in range(randint(8,10))]

    password_numbers = [choice(numbers) for _ in range((randint(2,4)))]

    password_symbols= [choice(symbols) for _ in range((randint(2,4)))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops",message="Plz don't leave any of the fields empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file ,indent=4)
 
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving new data
                json.dump(data , data_file , indent=4)
        
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END) 


# ---------------------------- FND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops",message="No Data File Found." )

    else:
        if website in data:
            email = data[website]["email"]
            password  = data[website]["password"]
            messagebox.showinfo(title=website , message=f"Emmail:{email}\nPassword:{password}")
        else:
             messagebox.showerror(title="Oops" , message=f"No details for {website} exists")

    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70,pady=70)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)
 
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_username_label = Label(text="Email /Username:")
email_username_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

search_button = Button(text="Search",width=20,command=find_password)
search_button.grid(column=3,row=1,columnspan=2)

website_entry = Entry(width=40)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0,"Aryan@gmail.com")

password_entry = Entry(width=40)
password_entry.grid(column=1,row=3)


generate_password_button = Button(text="Generate Password" , width=20, command=password_generator)
generate_password_button.grid(column=3,row=3)


add_button = Button(text="Add",width=34,command=save)
add_button.grid(column=1,row=4,columnspan=2)


canvas.mainloop()