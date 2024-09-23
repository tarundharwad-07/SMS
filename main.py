import mysql.connector
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

# Function to define database
def Database():
    global conn, cursor
    # MySQL database configuration
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Tarun@123',
        'database': 'studentmanagementsys'  # Replace 'your_database_name' with your actual database name
    }
    # Connecting to MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    # Creating STUD_REGISTRATION table if not exists
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUDENT (STU_ID INT AUTO_INCREMENT PRIMARY KEY, STU_NAME VARCHAR(255), STU_Fee_details VARCHAR(255), STU_Exam_result VARCHAR(255), STU_USN VARCHAR(255), STU_BRANCH VARCHAR(255))")

# Function to insert data into database
def register():
    # Database connection
    Database()
    # Getting form data
    name1 = name.get()
    fee_details1 = fee_details.get()
    exam_result1 = exam_result.get()
    usn1 = usn.get()
    branch1 = branch.get()
    # Applying empty validation
    if name1 == '' or fee_details1 == '' or exam_result1 == '' or usn1 == '' or branch1 == '':
        tkMessageBox.showinfo("Warning", "Fill the empty field!!!")
    else:
        # Execute query
        cursor.execute('INSERT INTO STUDENT (STU_NAME, STU_Fee_details, STU_Exam_result, STU_USN, STU_BRANCH) \
            VALUES (%s, %s, %s, %s, %s)', (name1, fee_details1, exam_result1, usn1, branch1))
        conn.commit()
        tkMessageBox.showinfo("Message", "Stored successfully")
        # Refresh table data
        DisplayData()
        conn.close()

# Function to display data
def DisplayData():
    # Open database connection
    Database()
    # Clear current data
    tree.delete(*tree.get_children())
    # Create cursor object
    cursor = conn.cursor()
    # Select query
    cursor.execute("SELECT * FROM STUDENT")
    # Fetch all data from database
    fetch = cursor.fetchall()
    # Loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    # Close cursor and connection
    cursor.close()
    conn.close()

# Function to create GUI layout
def DisplayForm():
    # Creating window
    display_screen = Tk()
    # Setting width and height for window
    display_screen.geometry("900x400")
    # Setting title for window
    display_screen.title("RUAS PORTAL")
    # Declaring variables
    global tree
    global SEARCH
    global name, fee_details, exam_result, usn, branch
    SEARCH = StringVar()
    name = StringVar()
    fee_details = StringVar()
    exam_result = StringVar()
    usn = StringVar()
    branch = StringVar()
    # Creating frames for layout
    # Top view frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    # First left frame for registration from
    LFrom = Frame(display_screen, width="350")
    LFrom.pack(side=LEFT, fill=Y)
    # Second left frame for search form
    LeftViewForm = Frame(display_screen, width=500, bg="cyan")
    LeftViewForm.pack(side=LEFT, fill=Y)
    # Mid frame for displaying students record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    # Label for heading
    lbl_text = Label(TopViewForm, text="Student Management System", font=('verdana', 18), width=600, bg="#1C2833",
                     fg="white")
    lbl_text.pack(fill=X)
    # Creating registration form in first left frame
    Label(LFrom, text="Name  ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Fee_details ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=fee_details).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Exam_result ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=exam_result).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="USN ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=usn).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Branch ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=branch).pack(side=TOP, padx=10, fill=X)
    Button(LFrom, text="Submit", font=("Arial", 10, "bold"), command=register).pack(side=TOP, padx=10, pady=5, fill=X)

    # Creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter name to Search", font=('verdana', 10), bg="gray")
    lbl_txtsearch.pack()
    # Creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    # Creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    # Creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    # Creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    # Creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    # Setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Student Id", "Name", "Fee_details", "Exam_result", "USN", "Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # Setting headings for the columns
    tree.heading('Student Id', text="Student Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Fee_details', text="Fee_details", anchor=W)
    tree.heading('Exam_result', text="Exam_result", anchor=W)
    tree.heading('USN', text="USN", anchor=W)
    tree.heading('Branch', text="Branch", anchor=W)
    # Setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

# Function to search data
def SearchRecord():
    # Open database
    Database()
    # Checking search text is empty or not
    if SEARCH.get() != "":
        # Clearing current display data
        tree.delete(*tree.get_children())
        # Select query with where clause
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENT WHERE STU_NAME LIKE %s", ('%' + SEARCH.get() + '%',))
        # Fetch all matching records
        fetch = cursor.fetchall()
        # Loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

# Function to reset fields
def Reset():
    # Clear current data from table
    tree.delete(*tree.get_children())
    # Refresh table data
    DisplayData()
    # Clear search text
    SEARCH.set("")
    name.set("")
    fee_details.set("")
    exam_result.set("")
    usn.set("")
    branch.set("")

# Function to delete data
def Delete():
    # Open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM STUDENT WHERE STU_ID = %s", (selecteditem[0],))
            conn.commit()
            cursor.close()
            conn.close()

# Main code starts here
if __name__ == '__main__':
    # Running the application
    DisplayForm()
    mainloop()
