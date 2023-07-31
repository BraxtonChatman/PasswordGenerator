import tkinter as tk
from tkinter import ttk
from random import choice, randint
import string

class PasswordGUI(tk.Tk):
    """A class representing window with two tabs:
    the first tab generates a new password according to the selected
    requirements, and the second tab validates whether or not a
    password meets given requirements"""
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x250")
        self.title("Password Generator")

        notebook = ttk.Notebook(self)
        notebook.pack()

        for T in (PasswordGenerator, PasswordValidator):
            tab = T(notebook)
            notebook.add(tab, text = tab.tab_title)


class PasswordGenerator(tk.Frame):
    """A class representing the first tab in the notebook
    which creates a new password according to selectable
    requirements."""

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.tab_title = "New Password"
        
        # required characters
        self.char_selection_frame = tk.LabelFrame(self, text = "Select Required Characters")
        self.char_selection_frame.pack(pady = 5)

        # checkbutton selection for required characters
        self.upper_var = tk.BooleanVar(value = False)
        self.lower_var = tk.BooleanVar(value = False)
        self.num_var = tk.BooleanVar(value = False)
        self.special_var = tk.BooleanVar(value = False)        

        upper_check = tk.Checkbutton(
            self.char_selection_frame,
            text = "Include Uppercase Letters",
            variable = self.upper_var,
            onvalue = True, offvalue = False)
        
        lower_check = tk.Checkbutton(
            self.char_selection_frame,
            text = "Include Lowercase Letters",
            variable = self.lower_var,
            onvalue = True, offvalue = False)
       
        num_check = tk.Checkbutton(
            self.char_selection_frame,
            text = "Include Numbers",
            variable = self.num_var,
            onvalue = True, offvalue = False)
       
        special_check = tk.Checkbutton(
            self.char_selection_frame,
            text = "Include Special Characters",
            variable = self.special_var,
            onvalue = True, offvalue = False)

        upper_check.grid(row = 0, column = 0, padx = 5)
        lower_check.grid(row = 1, column = 0, padx = 5)
        num_check.grid(row = 0, column = 1, sticky = "w", padx = 5)
        special_check.grid(row = 1, column = 1, padx = 5)

        # password length spinbox
        self.length_spin = tk.Spinbox(
            self.char_selection_frame,
            from_ = 4, to = 50,
            width = 50, state = 'readonly')
        
        self.length_spin.grid(row = 2, column = 0, columnspan = 2, pady = 10)

        # output entry space
        out_frame = tk.LabelFrame(self, text = "New Password:", width = 200)
        out_frame.pack(fill = tk.X)
                    
        self.out_space_var = tk.StringVar()
        out_space = tk.Entry(out_frame, width = 50, textvariable = self.out_space_var)
        out_space.pack(pady = 5)
        
        # generate password button
        gen_butt = tk.Button(out_frame, text = "Generate", command = self.generate_password)
        gen_butt.pack(pady = 10)

    def generate_password(self):
        """Gets the tkinter variables corresponding to user selected
        password requirements and generates a new password meeting the
        given requirements"""

        must_length = int(self.length_spin.get())
        must_upper = self.upper_var.get()
        must_lower = self.lower_var.get()
        must_num = self.num_var.get()
        must_special = self.special_var.get()

        new_password = ""
        available_lists = []
        pass_list = []
            
        # if selected add uppercase letters to selection list and add one uppercase digit to password
        if must_upper:
            available_lists.append(string.ascii_uppercase)
            pass_list.append(choice(string.ascii_uppercase))

        # if selected add lowercase letters to selection list and add one lowercase digit to password
        if must_lower:
            available_lists.append(string.ascii_lowercase)
            pass_list.append(choice(string.ascii_lowercase))
        
        # if selected add numbers  to selection list and add one digit to password
        if must_num:
            available_lists.append(string.digits)
            pass_list.append(choice(string.digits))
        
        # if selected add special characters to selection list and add one special character to password
        if must_special:
            available_lists.append(string.punctuation)
            pass_list.append(choice(string.punctuation))

        # return empty string if no character types selected
        if not available_lists:
            self.out_space_var.set("")
            return

        # pick a random digit from one of the available lists and add to pass list
        while len(pass_list) < must_length:
            pick_list = choice(available_lists)
            new_digit = choice(pick_list)
            pass_list.append(new_digit)

        # add digits from pass_list to new_password randomly
        new_password = ""
        while pass_list:
            new_digit_index = randint(0, len(pass_list)-1)
            new_password += pass_list.pop(new_digit_index)

        print(new_password)
        self.out_space_var.set(new_password)


class PasswordValidator(tk.Frame):
    """A class representing the second tab in the notebook
    which validates a  password according to preset requirements."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.tab_title = "Check Password"

        validate_password_frame = tk.LabelFrame(self, text = "Input Password to Check")
        validate_password_frame.pack(fill = tk.BOTH, expand = True, pady = 5)

        # password entry space and validation text bullet points
        password_space = tk.Entry(validate_password_frame, width = 50)
        password_space.grid(row = 0, column = 0, padx =25, pady = 10)

        self.length_label = tk.Label(validate_password_frame, text = "• At least 8 characters", fg = "red")
        self.length_label.grid(row = 1, column = 0, sticky = "w", padx = 25)

        self.upper_label = tk.Label(validate_password_frame, text = "• Contains an upper case letter", fg = "red")
        self.upper_label.grid(row = 2, column = 0, sticky = "w", padx = 25)

        self.lower_label = tk.Label(validate_password_frame, text = "• Contains a lower case letter", fg = "red")
        self.lower_label.grid(row = 3, column = 0, sticky = "w", padx = 25)

        self.number_label = tk.Label(validate_password_frame, text = "• Contains a number", fg = "red")
        self.number_label.grid(row = 4, column = 0, sticky = "w", padx = 25)

        self.special_label = tk.Label(validate_password_frame, text = "• Contains a special character", fg = "red")
        self.special_label.grid(row = 5, column = 0, sticky = "w", padx = 25)

        password_space.bind("<KeyRelease>", lambda event: self.change_labels(password_space))

    def change_labels(self, password_space):
        """method to change the color of the labels on the
        password validation tab. labels are changed to green
        if the label requirement is met by the password,
        otherwise label is set to red"""
        
        password = password_space.get()

        self.length_label.config(fg = "red")
        self.upper_label.config(fg = "red")
        self.lower_label.config(fg = "red")
        self.number_label.config(fg = "red")
        self.special_label.config(fg = "red")

        # check length of password
        if len(password) > 8:
            self.length_label.config(fg = "green")

        # check for given character types in password
        for character in password:
            if character in string.ascii_uppercase:
                self.upper_label.config(fg = "green")
            if character in string.ascii_lowercase:
                self.lower_label.config(fg = "green")
            if character in string.digits:
                self.number_label.config(fg = "green")
            if character in string.punctuation:
                self.special_label.config(fg = "green")


if __name__ == "__main__":
    app = PasswordGUI()
    app.mainloop()
