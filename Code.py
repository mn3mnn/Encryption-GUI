
from tkinter import *
from tkinter import messagebox


def encrypt():
    """ function to encrypt text and return it """

    e_text = input_field.get("1.0", 'end-1c')
    new_text = ""

    try:
        # encrypt method
        for letter in e_text:
            if letter == " ":
                pass

            elif 65 <= ord(letter) < 90:
                new_ord = ord(letter) + 1 + 32
                new_letter = chr(new_ord)
                new_text += str(new_letter)

            elif 97 <= ord(letter) < 122:
                new_ord = ord(letter) + 1
                new_letter = chr(new_ord)
                new_text += str(new_letter)

            elif ord(letter) == 122 or ord(letter) == 90:
                new_letter = chr(97)
                new_text += str(new_letter)

            else:
                new_text += letter
        # show the encrypted text
        r = Text(app, bg="#F9F9F9", border=0, width=23, height=15)
        r.insert("1.0", "your encrypted text is:\n\n")
        r.insert("2.0", "-> " + new_text)

        r.place(x=15, y=137)

    except:
        messagebox.showerror("ERROR ", "please enter only english letters ")
        return "Error"

    return new_text


def decrypt():
    """ function to decrypt text and return it """

    d_text = input_field2.get("1.0", 'end-1c')
    origin_text = ""

    # decrypt method
    for letter in d_text:
        if 97 <= ord(letter) <= 122:
            new_ord = ord(letter) - 1
            new_letter = chr(new_ord)
            origin_text += str(new_letter)

        else:
            origin_text += str(letter)

    # show the text
    r = Text(app, bg="#F9F9F9", border=0, width=23, height=15)
    r.insert("1.0", "your decrypted text is:\n\n")
    r.insert("2.0", "-> " + origin_text)

    r.place(x=15, y=137)

    return origin_text

# set up the app


app = Tk()


app.title("Encryption & Decryption")
app.geometry("800x600")
app.config(bg="black")

# place the labels on the window
Label(app, text=" enter text to encrypt ", font=("arial", 16), bg="#19d1a0", fg="black", border=0).place(x=15, y=90)
input_field = Text(app, bg="#F9F9F9", border=0, width=60, height=8)
input_field.place(x=250, y=40)

# place encrypt button
encrypt_btn = Button(app, text=" Encrypt ", bg="#19d1a0", border=0, width=15, height=2, command=lambda: encrypt())
encrypt_btn.place(x=460, y=190)

# decrypt text

# place the labels on the window
Label(app, text=" enter text to decrypt ", font=("arial", 16), bg="#19d1a0", fg="black", border=0).place(x=15, y=400)
input_field2 = Text(app, bg="#F9F9F9", border=0, width=60, height=8)
input_field2.place(x=250, y=350)

# place decrypt button
decrypt_btn = Button(app, text=" Decrypt ", bg="#19d1a0", border=0, width=15, height=2, command=lambda: decrypt())
decrypt_btn.place(x=460, y=500)

# run the app
app.mainloop()
