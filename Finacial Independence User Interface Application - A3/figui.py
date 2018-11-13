#!/usr/bin/env python

"""
The purpose of this application is to provide a simple graphical user interface
which provides a basic analyse of the important data from the finacially independent
Monte Carlo simulation. The application gives the ability to select and open the
output.txt file created by the Monte Carlo simulation, and displays the maximum,
minimum, and average balance for the final year of the simulation.
"""

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox


def select_file():
    """
    Opens a select file window so the user can select the file to be analysed.
    Once the file has been analysed the maximum, minumum and average values are determined.
    The labels on the main window for maximum, minumum and average are then configured to
    include these values.
    """
    filename = filedialog.askopenfilename()
    final_amounts = analyse_file(filename)
    try:
        max_label.config(text="Maximum balance: $ " + str(max(final_amounts)))
        min_label.config(text="Minimum balance: $ " + str(min(final_amounts)))
        avg_label.config(text="Average balance: $ " + str("%.2f" % (sum(final_amounts)/len(final_amounts))))
    # A TypeError is raised whenever the select file window is opened and the user cancels without selecting any file,
    # this returns a NoneType. This error is passed so that the current max_label, min_label and avg_label remain unchanged.
    except (TypeError):
        pass
    # A ValueError is raised whenever a selected file is unable to be opened or does not contain the correct information,
    # this means an empty list is returned for final_amounts. This error is passed so that the current max_label,
    # min_label and avg_label remain unchanged.
    except (ValueError):
        pass


def analyse_file(filename):
    """
    Opens the selected file and checks that the file format is consistant with the output
    of the Monte Carlo simulation. The file is checked to ensure that each line has the same
    number of items, that each line ends with the string "successful" or "unsuccessful", and
    that each item (except the final item of each row) is a float.

    Arguments:
    filename -- The path to the selected file to be opened.

    Returns a list containing the final finacial amounts from each line of the selected file
    """
    # The selected file is checked to ensure it is consistent with the output.txt from the Monte Carlo simulation.
    # The first check ensures that each item within the file can be a float type, except the last item on each line.
    # The second check ensures that the last item in each line is either the string "successful" or "unsuccessful".
    # The third check ensures the lengths of each line are equal by comparing each line to the length of the first line.
    try:
        with open(filename) as f:
                num_items = []
                last_number = []
                for line in f:
                    line_items = line.split(" ")
                    # First check. If any item cannot become a float type than ValueError is raised.
                    for item in line_items[:-1]:
                        float(item)
                    # Second check. If any item is not "successful" or "unsuccessful" an empty list is returned.
                    if line_items[-1] != "successful\n" and line_items[-1] != "unsuccessful\n":
                        messagebox.showerror('Error', 'The selected file does not contain the correct finacial '\
                            'information. Please review the file or select another file and try again')
                        # An empty list is returned whenever there is an error as this gives the user the opportuntiy to
                        # go back to the main window and review the file before trying to select another. This also allows
                        # for the existing max_label, min_label and avg_label values to remain unchanged.
                        return []
                    # The length of each line is stored in a list called num_items
                    num_items.append(len(line_items))
                    # The last number of each line is stored in a list called last_number
                    last_number.append(float(line_items[-2]))
                # Third check. If any line length is not equal an empty list is returned.
                for num in num_items:
                    if num != num_items[0]:
                        messagebox.showerror('Error', 'The selected file does not contain the correct finacial '\
                            'information. Please review the file or select another file and try again')
                        # Return an empty list
                        return []
                # Returns the list containg the last numbers from each line
                return last_number
    # An UnicodeDecodeError is raised whenever a file is selected that can not be opened correctly
    except UnicodeDecodeError:
        messagebox.showerror('UnicodeDecodeError', 'The selected file was unable to be opened correctly. '\
            'Please review the file or select another file and try again')
        # Return an empty list
        return []
    # A TypeError is raised the first time the select file window is opened and the user cancels without selecting any file,
    # the FileNotFoundError is raised anytime after this that a user cancels without selecting any file.
    # Boths errors are passed, this also allows for the existing max_label, min_label and avg_label values to remain unchanged.
    except (TypeError, FileNotFoundError):
        pass
    # A ValueError is raised whenever a file contains an item that is not a float, based on the first check.
    except ValueError:
        messagebox.showerror('ValueError', 'The selected file does not contain the correct finacial '\
            'information. Please review the file or select another file and try again')
        # Return an empty list
        return []
    # A PermissionError is raised if the user try's to open a file they don't have the correct permissions to access
    except PermissionError:
        messagebox.showerror('PermissionError', 'You do not have permission to open the selected file. '\
            'Please review your permission settings or select another file and try again')
        # Return an empty list
        return []


root = Tk()
# Set window title
root.title("Financial Independence GUI")

# Create content frame
content = ttk.Frame(root, width=500, height=500)

# Create widgets for button and labels
button1 = Button(content, command=select_file, text = "Open...", padx=20, pady=5)
max_label = ttk.Label(content, text="Maximum balance: $ ")
min_label = ttk.Label(content, text="Minimum balance: $ ")
avg_label = ttk.Label(content, text="Average balance: $ ")

# Set font size for buttons and labels
my_font = font.Font(size=14, weight='bold')
button1['font'] = my_font
max_label['font'] = my_font
min_label['font'] = my_font
avg_label['font'] = my_font

# Position widgets
content.grid(column=0, row=0, sticky=(N, S, E, W))
button1.place(relx=0.5, rely=0.15, anchor=CENTER)
max_label.place(relx=0.5, rely=0.35, anchor=CENTER)
min_label.place(relx=0.5, rely=0.55, anchor=CENTER)
avg_label.place(relx=0.5, rely=0.75, anchor=CENTER)

# Set resizing weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)

root.mainloop()
