import tkinter as tk
import random
import string


def generate_password(upper=8, lower=8, let_lower=True, let_upper=True, let_nums=True, let_special=True):
    available_lists = []
    pass_list = []

    if let_lower:
        available_lists.append(string.ascii_lowercase)
        pass_list.append(random.choice(string.ascii_lowercase))
        
    
    if let_upper:
        available_lists.append(string.ascii_uppercase)
        pass_list.append(random.choice(string.ascii_uppercase))
    
    if let_nums:
        available_lists.append(string.digits)
        pass_list.append(random.choice(string.digits))
    
    if let_special:
        available_lists.append(string.punctuation)
        pass_list.append(random.choice(string.punctuation))


  





# root = tk.Tk()
# root.title("Password Generator")







# root.mainloop()
