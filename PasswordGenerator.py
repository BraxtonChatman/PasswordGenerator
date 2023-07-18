import tkinter as tk
from random import choice, randint
import string


def generate_password(upper=8, lower=8, let_lower=True, let_upper=True, let_nums=True, let_special=True):
    """Generates a random password according to given parameters
    
    upper and lower inputs are the length limits for the password
    let_lower, let_upper, let_nums, let_special are bool inputs that allow
    the respective types of digits to be included"""
    
    available_lists = []
    pass_list = []

    # if selected add lowercase letters to selection list and add one lowercase digit to password
    if let_lower:
        available_lists.append(string.ascii_lowercase)
        pass_list.append(choice(string.ascii_lowercase))
        
    # if selected add uppercase letters to selection list and add one uppercase digit to password
    if let_upper:
        available_lists.append(string.ascii_uppercase)
        pass_list.append(choice(string.ascii_uppercase))
    
    # if selected add numbers  to selection list and add one digit to password
    if let_nums:
        available_lists.append(string.digits)
        pass_list.append(choice(string.digits))
    
    # if selected add special characters to selection list and add one special character to password
    if let_special:
        available_lists.append(string.punctuation)
        pass_list.append(choice(string.punctuation))

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






# root = tk.Tk()
# root.title("Password Generator")







# root.mainloop()
