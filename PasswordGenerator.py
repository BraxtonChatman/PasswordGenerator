import tkinter as tk
from tkinter import ttk
from random import choice, randint
import string


def generate_password(upper=8, lower=8, let_upper=True, let_lower=True, let_nums=True, let_special=True):
    """Generates a random password according to given parameters
    
    upper and lower inputs are the length limits for the password
    let_lower, let_upper, let_nums, let_special are bool inputs that allow
    the respective types of digits to be included"""

    available_lists = []
    pass_list = []
        
    # if selected add uppercase letters to selection list and add one uppercase digit to password
    if let_upper:
        available_lists.append(string.ascii_uppercase)
        pass_list.append(choice(string.ascii_uppercase))

    # if selected add lowercase letters to selection list and add one lowercase digit to password
    if let_lower:
        available_lists.append(string.ascii_lowercase)
        pass_list.append(choice(string.ascii_lowercase))
    
    # if selected add numbers  to selection list and add one digit to password
    if let_nums:
        available_lists.append(string.digits)
        pass_list.append(choice(string.digits))
    
    # if selected add special characters to selection list and add one special character to password
    if let_special:
        available_lists.append(string.punctuation)
        pass_list.append(choice(string.punctuation))

    # return empty string if no character types selected
    if not available_lists:
        return ""

    # pick a random digit from one of the available lists and add to pass list
    pass_length = randint(lower, upper)
    while len(pass_list) < pass_length:
        pick_list = choice(available_lists)
        new_digit = choice(pick_list)
        pass_list.append(new_digit)

    # add digits from pass_list to new_password randomly
    new_password = ""
    while pass_list:
        new_digit_index = randint(0, len(pass_list)-1)
        new_password += pass_list.pop(new_digit_index)

    return new_password


def validate_password(password, length=8, need_upper=True, need_lower=True, need_nums=True, need_special=True):
    """validate that password meets given requirements
    
    length is the length requirement for the given password
    need_lower, need_upper, need_nums, need_special are bool
    inputs to check if password contains given types of digits
    
    returns list containing bool value at index 0 of whether or
    not password is valid and subsequent entries contain bools
    sepcifying which requirements weren't met
    e.g.  [valid,  meets_length,  has_upper,  has_lower,  has_nums]
    given that the corresponding values were selected as required as inputs"""
    
    out_list = []
    meets_reqs = True

    meets_len = False
    meets_upper = False
    meets_lower = False
    meets_nums = False
    meets_special = False

    # check length requirement
    if len(password) >= length:
        meets_len = True

    # for each digit, check if given requirements are met
    for digit in password:
        if need_upper and digit in string.ascii_uppercase:
            meets_upper = True
        if need_lower and digit in string.ascii_lowercase:
            meets_lower = True
        if need_nums and digit in string.digits:
            meets_nums = True
        if need_special and digit in string.punctuation:
            meets_special = True

    # add whether each requirement was met to output list
    meets_reqs = meets_reqs and meets_len
    out_list.append(meets_len)

    if need_upper:
        meets_reqs = meets_reqs and meets_upper
        out_list.append(meets_upper)

    if need_lower:
        meets_reqs = meets_reqs and meets_lower
        out_list.append(meets_lower)

    if need_nums:
        meets_reqs = meets_reqs and meets_nums
        out_list.append(meets_nums)

    if need_special:
        meets_reqs = meets_reqs and meets_special
        out_list.append(meets_special)

    out_list = [meets_reqs] + out_list
    return out_list


def button_generate(upper, lower, let_upper, let_lower, let_nums, let_special, out_space_var):
    """Gets the tkinter variables corresponding to user selected
    password requirements and inputs them to generate_password
    function to return new password"""

    have_upper = let_upper.get()
    have_lower = let_lower.get()
    have_nums = let_nums.get()
    have_special = let_special.get()
    upper_lim = int(upper.get())
    lower_lim = int(lower.get())

    new_password = generate_password(upper = upper_lim, lower = lower_lim, let_upper = have_upper, let_lower = have_lower, let_nums = have_nums, let_special = have_special)
    print(new_password)
    out_space_var.set(new_password)


def rnfun(special_label):
    special_label.config(fg = "blue")


def change_label_color(length_label, upper_label, lower_label, number_label, special_label, password_space):
    #length_label.config(fg = "green")
    check_string = password_space.get()
    meets_reqs = validate_password(check_string, 8, True, True, True, True)



def main():
    # main window
    root = tk.Tk()
    root.geometry("400x250")
    root.title("Password Generator")

    # notebook for tabs
    notebook = ttk.Notebook(root)
    notebook.pack()

    new_frame = tk.Frame(notebook)
    new_frame.pack()

    check_frame = tk.Frame(notebook)
    check_frame.pack()

    notebook.add(new_frame, text = "New Password")
    notebook.add(check_frame, text = "Check Password")

    # labelframe for required characters
    char_selection_frame = tk.LabelFrame(new_frame, text = "Select Required Characters")
    char_selection_frame.pack(pady = 5)

    # checkbutton selection for required characters
    upper_var = tk.BooleanVar(value = False)
    lower_var = tk.BooleanVar(value = False)
    num_var = tk.BooleanVar(value = False)
    special_var = tk.BooleanVar(value = False)

    upper_check = tk.Checkbutton(char_selection_frame, text = "Include Uppercase Letters", variable = upper_var, onvalue = True, offvalue = False)
    lower_check = tk.Checkbutton(char_selection_frame, text = "Include Lowercase Letters", variable = lower_var, onvalue = True, offvalue = False)
    num_check = tk.Checkbutton(char_selection_frame, text = "Include Numbers", variable = num_var, onvalue = True, offvalue = False)
    special_check = tk.Checkbutton(char_selection_frame, text = "Include Special Characters", variable = special_var, onvalue = True, offvalue = False)

    upper_check.grid(row = 0, column = 0, padx = 5)
    lower_check.grid(row = 1, column = 0, padx = 5)
    num_check.grid(row = 0, column = 1, sticky = "w", padx = 5)
    special_check.grid(row = 1, column = 1, padx = 5)

    # password length spinbox
    length_spin = tk.Spinbox(char_selection_frame, from_ = 4, to = 50, width = 50, state = 'readonly')
    length_spin.grid(row = 2, column = 0, columnspan = 2, pady = 10)

    # output entry space
    out_frame = tk.LabelFrame(new_frame, text = "New Password:", width = 200)
    out_frame.pack(fill = tk.X)
                   
    out_space_var = tk.StringVar()
    out_space = tk.Entry(out_frame, width = 50, textvariable = out_space_var)
    out_space.pack(pady = 5)
    
    # generate password button
    gen_butt = tk.Button(out_frame, text = "Generate", command = lambda: button_generate
                         (length_spin, length_spin, upper_var, lower_var, num_var, special_var, out_space_var))
    gen_butt.pack(pady = 10)


    # second tab for validating password
    validate_password_frame = tk.LabelFrame(check_frame, text = "Input Password to Check")
    validate_password_frame.pack(fill = tk.BOTH, expand = True, pady = 5)

    # password entry space and validation text bullet points
    password_space = tk.Entry(validate_password_frame, width = 50)
    password_space.grid(row = 0, column = 0, padx =25, pady = 10)

    length_label = tk.Label(validate_password_frame, text = "• At least 8 characters", fg = "red")
    length_label.grid(row = 1, column = 0, sticky = "w", padx = 25)

    upper_label = tk.Label(validate_password_frame, text = "• Contains an upper case letter")
    upper_label.grid(row = 2, column = 0, sticky = "w", padx = 25)

    lower_label = tk.Label(validate_password_frame, text = "• Contains a lower case letter")
    lower_label.grid(row = 3, column = 0, sticky = "w", padx = 25)

    number_label = tk.Label(validate_password_frame, text = "• Contains a number")
    number_label.grid(row = 4, column = 0, sticky = "w", padx = 25)

    special_label = tk.Label(validate_password_frame, text = "• Contains a special character")
    special_label.grid(row = 5, column = 0, sticky = "w", padx = 25)

    password_space.bind("<KeyRelease>", lambda event: change_label_color
                              (length_label, upper_label, lower_label, number_label, special_label, password_space))



    root.mainloop()


if __name__ == "__main__":
    main()
