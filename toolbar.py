from tkinter import *
root = Tk()

toolbar = Frame(root, bg="pink")

# tkinter using drop down


def menu_function():
    print("menu clicked")


my_menu = Menu(root)
root.config(menu=my_menu)

sub_menu = Menu(my_menu)

my_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Project", command=menu_function)
sub_menu.add_command(label="Save", command=menu_function)

sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=toolbar.quit)

new_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=new_menu)
new_menu.add_command(label="Quit", command=menu_function)

insert_button = Button(toolbar, text="insert files", command=menu_function)
insert_button.pack(side=LEFT, padx=2, pady=3)

print_button = Button(toolbar, text="print", command=menu_function)
print_button.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

root.mainloop()
