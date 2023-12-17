from tkinter import *
from tkinter import ttk
from datetime import datetime

def main():
    
    # create tkinter root window
    window = Tk()
    
    #create the main window
    mainFrm = Frame(window)
    window.title("Sakau Connect LLC")
    mainFrm.configure(background="brown")
    mainFrm.pack()
    
    populate_window(mainFrm=mainFrm)
    
    
    window.mainloop()
    
    
def populate_window(mainFrm):

    # create user info window inside main window
    user_info = LabelFrame(mainFrm, text="BUYER INFO")
    user_info.grid(row=0, column=0, padx=20, pady=20)
    
    # add user info labels inside user info window
    first_name_label = Label(user_info, text="First Name")
    first_name_label.grid(row=0, column=1)
    last_name_label = Label(user_info, text="Last Name")
    last_name_label.grid(row=0, column=2)
    title = Label(user_info, text="Title")
    title.grid(row=0, column=0)
    
    # create entry boxes
    first_name_entry = Entry(user_info)
    last_name_entry = Entry(user_info)
    first_name_entry.grid(row=1, column=1)
    last_name_entry.grid(row=1, column=2)
    title_combobox = ttk.Combobox(user_info, values=["","Mr.", "Ms.", "Dr."])
    title_combobox.grid(row=1, column=0)
    
    # Create window for order info
    order_info = LabelFrame(mainFrm, text="CHOOSE YOUR SAKAU")
    order_info.grid(row=1, column=0, padx=20, pady=20)
    
    # Add sakau grade info
    grade_label = Label(order_info, text="Select Grade")
    grade_label.grid(row=0, column=0)
    grade_combobox = ttk.Combobox(order_info, values=["A", "B", "C", "F"])
    grade_combobox.grid(row=1, column=0)
    
    # Add Sakau weight info
    weight_label = Label(order_info, text="Weight (10 - 150)")
    weight_label.grid(row=0, column=2)
    weight_entry = Entry(order_info)
    weight_entry.grid(row=1, column=2)
    
    def conditionBind(event):
        if condition_combobox.get() == "Pounded":
            condition_price_info.config(text=f"plus $55.00")
        elif condition_combobox.get() == "Cut Short":
            condition_price_info.config(text=f"plus $45.00")
        elif condition_combobox.get() == "Powdered":
            condition_price_info.config(text=f"plus $35.00")
    
    # add sakau condition info
    condition_label = Label(order_info, text="Conditions")
    condition_label.grid(row=0, column=1)
    condition_combobox = ttk.Combobox(order_info, values=["Powdered", "Cut Short", "Pounded"])
    condition_combobox.grid(row=1, column=1)
    
    # add condition price info
    condition_price_info = Label(order_info, text="")
    condition_price_info.grid(row=2, column=1)
    
    # bind combobox
    condition_combobox.bind("<<ComboboxSelected>>", conditionBind)
    
    def gradeBind(event):
        if grade_combobox.get() == "A":
            grade_price.config(text=f"A:   $15 / lb")
        elif grade_combobox.get() == "B":
            grade_price.config(text="B:   $10 / lb")
        elif grade_combobox.get() == "C":
            grade_price.config(text="C:   $8 / lb")
        elif grade_combobox.get() == "F":
            grade_price.config(text="F (Frozen): $5 / lb")
    
    # create grade price info when a grade is selected
    grade_price = Label(order_info, text="")
    grade_price.grid(row=2, column=0, pady=5)
    
    # bind combobox
    grade_combobox.bind("<<ComboboxSelected>>", gradeBind)
    
    # create window for displaying total price
    total_price_lbl = Label(order_info, text="Total:")
    total_price_lbl.grid(row=2, column=2)
    
    def accept():
        order_button.config(state=ACTIVE)
        order_button.config()

    
    #Declare a variable for the order details passed from the get_order_details function
    # order = get_order_details(title_combobox, first_name_entry, last_name_entry, grade_combobox, condition_combobox, weight_entry)
    
    # create terms window
    terms_wndw = LabelFrame(mainFrm, text="Terms & Conditions")
    terms_wndw.grid(row=2, column=0)
    terms_check = Checkbutton(terms_wndw, text="I accept the terms and conditions.", command=accept)
    terms_check.grid(row=0, column=0)
        
    def clicker():
        if weight_entry.get() < "10" or grade_combobox.get() == "" or condition_combobox.get() == "":
            button_msg.config(text="Please complete your order first!")
        else:
            # title.config(text="")
            # first_name_entry.delete()
            # last_name_entry.config(text="")
            # grade_combobox.config(text="")
            # condition_combobox.config(text="")
            # weight_entry.config(text="")
            button_msg.config(text="Your order has been placed!")
            
        
    # create calculate total button
    order_button = Button(mainFrm, text="Place Order", command=clicker, state=DISABLED)
    order_button.grid(row=3, column=0, padx=10, pady=5)
    
    # Add a empty label at the bottom that changes when
    # user clicks the place order button
    
    button_msg = Label(mainFrm, background="brown", text="")
    button_msg.grid(row=4, column=0, padx=10, pady=5)
    
    
    
    #order_button.bind("<Button-1>", clicker)
    #terms_check.bind("<Button-1>", accept)
    
    
    # change padding on all children windows    
    for widget in user_info.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        
    for widget in order_info.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        
    for widget in terms_wndw.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        
    
    
    VALUE_INDEX = 0
    
    condDict = {
        "Pounded": [55.00],
        "Powdered": [35.00],
        "Cut Short": [45.00],
    }
    
    gradeDict = {
        "A": [15],
        "B": [10],
        "C": [8],
        "F": [5],
    }
        
    def calculate(event):
        
        try:
            # get the weight of the product
            weight = float(weight_entry.get())
            
            if weight < 10:
                total_price_lbl.config(text="Minimum weight requirement: 10lbs")
            
            else:
                
            
                # get the grade of the product
                grade = grade_combobox.get()
            
                # get the condition
                condition = condition_combobox.get()
            
                if condition in condDict:
                    value = condDict[condition]
                    condition_price = float(value[VALUE_INDEX])
                
                
                if grade in gradeDict:
                    value = gradeDict[grade]
                    gradePrice = int(value[VALUE_INDEX])
            
                total = (weight * gradePrice) + condition_price
            
            total_price_lbl.config(text=f"Total: {total:.2f}")
        
        except ValueError:
            total_price_lbl.config(text="")
            
            
    weight_entry.bind("<KeyRelease>", calculate)
    
    
if __name__ == "__main__":
    main()