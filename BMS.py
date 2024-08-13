import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re
from datetime import datetime
import csv
import random
import string
from cryptography.fernet import Fernet

# Key for encryption/decryption 
key = Fernet.generate_key()
cipher_suite = Fernet(key)

class BankingSystemGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Banking System App")
        # Load the background image
        self.background_image = Image.open("background_image.jpg")
        self.bg_image = ImageTk.PhotoImage(self.background_image)
        self.show_welcome()
        # Open the transaction history CSV file in append mode
        self.transaction_file = open("transaction_history.csv", mode='a', newline='')
        self.transaction_writer = csv.writer(self.transaction_file)
        # Write the header if the file is empty
        if self.transaction_file.tell() == 0:
            self.transaction_writer.writerow(["Date", "Username", "Transaction Type", "Amount"])

    def set_background(self, window):
        # Create a canvas and set the background image
        canvas = tk.Canvas(window, width=self.background_image.width, height=self.background_image.height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Place all widgets on the canvas
        return canvas
    def show_welcome(self):
        # Create the welcome window
        welcome_canvas = self.set_background(self.root)
        # Welcome message
        welcome_label = tk.Label(self.root, text="Welcome to Advanced SE Banking System", font=("Helvetica", 16), bg="white")
        welcome_canvas.create_window(300, 50, window=welcome_label)

        # Options
        login_button = tk.Button(self.root, text="Login", command=self.show_login)
        welcome_canvas.create_window(300, 150, window=login_button)

        register_button = tk.Button(self.root, text="Create Account", command=self.show_registration_form)
        welcome_canvas.create_window(300, 200, window=register_button)

    def edit_account(self):
        # Implementation of account editing functionality
        pass

    def create_account(self):
        def save_account():
            # Get values from entry fields
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            age = age_entry.get()
            id_number = id_entry.get()
            gender = gender_var.get()
            contact_number = contact_entry.get()
            account_type = account_type_var.get()

            # Perform validation checks
            # Add your validation checks here

            # If all checks pass, save the account details to user_data.txt
            with open("user_data.txt", "a") as file:
                file.write(
                    f"Username: {username}, Password: {password}, Email: {email}, Age: {age}, ID: {id_number}, Gender: {gender}, Contact: {contact_number}, Account Type: {account_type}\n")

            messagebox.showinfo("Success", "Account created successfully!")
            create_account_window.destroy()

        create_account_window = tk.Toplevel(self.root)
        create_account_window.title("Create Account")

        # Username
        username_label = tk.Label(create_account_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(create_account_window)
        username_entry.pack()

        # Password
        password_label = tk.Label(create_account_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(create_account_window, show="*")
        password_entry.pack()

        # Email
        email_label = tk.Label(create_account_window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(create_account_window)
        email_entry.pack()

        # Age
        age_label = tk.Label(create_account_window, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(create_account_window)
        age_entry.pack()

        # ID card number
        id_label = tk.Label(create_account_window, text="ID Card Number:")
        id_label.pack()
        id_entry = tk.Entry(create_account_window)
        id_entry.pack()

        # Gender
        gender_var = tk.StringVar(create_account_window)
        gender_var.set("Male")  # Default gender
        gender_label = tk.Label(create_account_window, text="Gender:")
        gender_label.pack()
        gender_menu = tk.OptionMenu(create_account_window, gender_var, "Male", "Female", "Other")
        gender_menu.pack()

        # Contact number
        contact_label = tk.Label(create_account_window, text="Contact Number:")
        contact_label.pack()
        contact_entry = tk.Entry(create_account_window)
        contact_entry.pack()

        # Account Type
        account_type_var = tk.StringVar(create_account_window)
        account_type_var.set("Personal")  # Default account type
        account_type_label = tk.Label(create_account_window, text="Account Type:")
        account_type_label.pack()
        account_type_menu = tk.OptionMenu(create_account_window, account_type_var, "Personal", "Business")
        account_type_menu.pack()

        save_button = tk.Button(create_account_window, text="Save", command=save_account)
        save_button.pack(pady=10)

    def close_account(self):
        # Delete account details from user_data.txt
        with open("user_data.txt", "r") as file:
            lines = file.readlines()

        found = False
        updated_lines = []  # To store updated lines without the closed account
        for line in lines:
            if self.username_entry.get() in line:
                found = True
            else:
                updated_lines.append(line)

        if not found:
            messagebox.showerror("Error", "User not found.")
            return

        # Update user_data file with the updated lines
        with open("user_data.txt", "w") as file:
            file.writelines(updated_lines)

        messagebox.showinfo("Success", "Account closed successfully!")
        self.root.destroy()  # Close the current window after closing the account

    def show_login(self):
        # Create login window
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")

        # Set background
        login_canvas = self.set_background(login_window)

        # Username
        username_label = tk.Label(login_window, text="Username:", bg="white")
        login_canvas.create_window(150, 50, window=username_label)
        self.username_entry = tk.Entry(login_window)
        login_canvas.create_window(300, 50, window=self.username_entry)

        # Password
        password_label = tk.Label(login_window, text="Password:", bg="white")
        login_canvas.create_window(150, 100, window=password_label)
        self.password_entry = tk.Entry(login_window, show="*")
        login_canvas.create_window(300, 100, window=self.password_entry)

        login_button = tk.Button(login_window, text="Login", command=self.login)
        login_canvas.create_window(300, 150, window=login_button)

    def show_registration_form(self):
        # Clear the welcome screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Registration form
        registration_label = tk.Label(self.root, text="Create Account", font=("Helvetica", 16))
        registration_label.pack(pady=20)
        # Account Type
        account_type_var = tk.StringVar(self.root)
        account_type_var.set("Personal")  # Default account type
        account_type_label = tk.Label(self.root, text="Account Type:")
        account_type_label.pack()
        account_type_menu = tk.OptionMenu(self.root, account_type_var, "Personal", "Business")
        account_type_menu.pack()
        # Username
        self.username_entry = tk.Entry(self.root)
        username_label = tk.Label(self.root, text="Username:")
        username_label.pack()
        self.username_entry.pack()

        # Password
        self.password_entry = tk.Entry(self.root, show="*")
        password_label = tk.Label(self.root, text="Password:")
        password_label.pack()
        self.password_entry.pack()

        # Email
        self.email_entry = tk.Entry(self.root)
        email_label = tk.Label(self.root, text="Email:")
        email_label.pack()
        self.email_entry.pack()

        # Age
        self.age_entry = tk.Entry(self.root)
        age_label = tk.Label(self.root, text="Age:")
        age_label.pack()
        self.age_entry.pack()

        # ID card number
        self.id_entry = tk.Entry(self.root)
        id_label = tk.Label(self.root, text="ID Card Number:")
        id_label.pack()
        self.id_entry.pack()

        # Gender
        self.gender_var = tk.StringVar(self.root)
        self.gender_var.set("Male")  # Default gender
        gender_label = tk.Label(self.root, text="Gender:")
        gender_label.pack()
        gender_menu = tk.OptionMenu(self.root, self.gender_var, "Male", "Female", "Other")
        gender_menu.pack()



        # Contact number
        self.contact_entry = tk.Entry(self.root)
        contact_label = tk.Label(self.root, text="Contact Number:")
        contact_label.pack()
        self.contact_entry.pack()

        register_button = tk.Button(self.root, text="Create", command=self.register)
        register_button.pack(pady=10)

    def register(self):
        # Get values from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        id_number = self.id_entry.get()
        gender = self.gender_var.get()  # Get selected gender from the variable
        contact_number = self.contact_entry.get()

        # Perform validation checks
        if not re.match(r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,}$", password):
            messagebox.showerror("Error",
                                 "Password must contain at least one number, one uppercase letter, one lowercase letter, one symbol, and be at least 8 characters long.")
            return

        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        if not age.isdigit() or int(age) < 18:
            messagebox.showerror("Error", "Age must be a number and 18 or older.")
            return

        if len(id_number) != 13 or not id_number.isdigit():
            messagebox.showerror("Error", "ID Card Number must be 13 digits long and contain only digits.")
            return

        # If all checks pass, registration is successful
        messagebox.showinfo("Success", "Registration successful!")
        # Save the account details to account.txt
        with open("account.txt", "a") as file:
            file.write(
                f"Username: {username}, Password: {password}, Email: {email}, Age: {age}, ID: {id_number}, Gender: {gender}, Contact: {contact_number}\n")

    # Close the registration window
        # Close the registration window
        self.root.destroy()

        # Open the login window
        self.show_login()

    def view_account_info(self):
        # Read all user information from account.txt
        with open("account.txt", "r") as file:
            lines = file.readlines()

        # Initialize user_info as an empty string to accumulate user information
        user_info = ""

        # Iterate through each line in the file
        for line in lines:
            # Split the line into parts based on the separator
            parts = line.strip().split(", Password: ")
            
            # Extract the username from the parts
            username = parts[0].split(": ")[1]
            
            # Check if the username matches the one entered by the user
            if username == self.username_entry.get():
                # If there's a match, add the line (user information) to user_info
                user_info += line + "\n"

        # Check if user_info is empty, meaning the specified user was not found
        if not user_info:
            messagebox.showerror("Error", "User not found.")
        else:
            # Display the user information
            messagebox.showinfo("Account Information", user_info)

    # Add method to generate random code for 2FA
    '''
    def generate_2fa_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        '''
    def is_2fa_required(self, username):
        # Placeholder method to determine if 2FA is required for the given username
        # You can implement your logic here to check if 2FA is required for the user
        return True  # Placeholder value; modify based on your requirements

    def generate_2fa_code(self):
        # Placeholder method to generate a 2FA code
        # You can implement your logic here to generate a random 2FA code
        return '123456'  # Placeholder value; modify based on your requirements
    
    def login(self):
        # Get entered username and password
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        # Check credentials against stored credentials
        with open("credentials.txt", "r") as file:
            for line in file:
                print("Line read from credentials file:", line)  # Debugging line
                username_password = line.strip().split(", ")
                print("Username and password split:", username_password)  # Debugging line
                username = username_password[0].split(": ")[1]
                password = username_password[1].split(": ")[1]
                print("Extracted username:", username)  # Debugging line
                print("Extracted password:", password)  # Debugging line
                if username == entered_username and password == entered_password:
                    # Check if 2FA is required
                    if self.is_2fa_required(username):
                        # Generate and send 2FA code
                        code = self.generate_2fa_code()
                        # Send code via email or SMS
                        # Prompt user for 2FA code
                        code_entry_window = tk.Toplevel(self.root)
                        code_entry_window.title("Enter 2FA Code")
                        code_label = tk.Label(code_entry_window, text="Enter 2FA code sent to your email/phone:")
                        code_label.pack()
                        code_entry = tk.Entry(code_entry_window)
                        code_entry.pack()

                        def verify_2fa():
                            entered_code = code_entry.get()
                            if entered_code == code:
                                messagebox.showinfo("Success", "Login successful!")
                                self.show_banking_interface()
                                code_entry_window.destroy()
                            else:
                                messagebox.showerror("Error", "Invalid 2FA code.")

                        verify_button = tk.Button(code_entry_window, text="Verify", command=verify_2fa)
                        verify_button.pack()
                    else:
                        messagebox.showinfo("Success", "Login successful!")
                        self.show_banking_interface()
                    return

        messagebox.showerror("Error", "Invalid username or password.")


        def verify_2fa():
            entered_code = code_entry.get()
            if entered_code == code:
                messagebox.showinfo("Success", "Login successful!")
                self.show_banking_interface()
                code_entry_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid 2FA code.")
            
        verify_button = tk.Button(code_entry_window, text="Verify", command=verify_2fa)
        verify_button.pack()

    # Encrypt sensitive information before storing
    def encrypt_data(self, data):
        return cipher_suite.encrypt(data.encode()).decode()

    # Decrypt sensitive information when needed
    def decrypt_data(self, encrypted_data):
        return cipher_suite.decrypt(encrypted_data.encode()).decode()

    def log_activity(self, username, action):
        # Log user activity with timestamp
        with open("activity.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {username}: {action}\n")

    def show_banking_interface(self):
        # Show banking interface
        banking_window = tk.Toplevel(self.root)
        banking_window.title("Banking Interface")
        
        # Set background
        banking_canvas = self.set_background(banking_window)

        # View Account Info button
        view_account_button = tk.Button(banking_window, text="View Account Info", command=self.view_account_info)
        banking_canvas.create_window(250, 50, window=view_account_button)

        # Withdraw button
        withdraw_button = tk.Button(banking_window, text="Withdraw", command=self.withdraw)
        banking_canvas.create_window(250, 90, window=withdraw_button)

        # Deposit button
        deposit_button = tk.Button(banking_window, text="Deposit", command=self.deposit)
        banking_canvas.create_window(250, 130, window=deposit_button)

        # Check Balance button
        check_balance_button = tk.Button(banking_window, text="Check Balance", command=self.check_balance)
        banking_canvas.create_window(250, 170, window=check_balance_button)

        # Close Account button
        close_account_button = tk.Button(banking_window, text="Close Account", command=self.close_account)
        banking_canvas.create_window(250, 210, window=close_account_button)

        # Request Checkbook button
        request_checkbook_button = tk.Button(banking_window, text="Request Checkbook", command=self.request_checkbook)
        banking_canvas.create_window(250, 250, window=request_checkbook_button)

        # Request Debit/Credit Card button
        request_card_button = tk.Button(banking_window, text="Request Debit/Credit Card", command=self.request_debit_credit_card)
        banking_canvas.create_window(250, 290, window=request_card_button)

        # Setup Recurring Payments button
        setup_recurring_button = tk.Button(banking_window, text="Setup Recurring Payments", command=self.setup_recurring_payment)
        banking_canvas.create_window(250, 330, window=setup_recurring_button)

        # Setup Direct Debit button
        setup_direct_debit_button = tk.Button(banking_window, text="Setup Direct Debit", command=self.setup_direct_debit)
        banking_canvas.create_window(250, 370, window=setup_direct_debit_button)

    def deposit(self):
        # Implement deposit functionality
        pass

    def check_balance(self):
        # Read balance from user_data.txt
        with open("user_data.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if parts[0].split(": ")[1] == self.username_entry.get():
                    balance = float(parts[2].split(": ")[1].replace('$', '').replace(',', ''))
                    print(balance)# Extract balance
                    messagebox.showinfo("Balance", f"Your balance is: ${balance:,.2f}")
                    return
    def deposit(self):
        def deposit_amount():
            # Get the entered amount
            amount = float(amount_entry.get())

            # Read user data from user_data.txt
            with open("user_data.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_lines = []  # To store updated lines with balance
            for line in lines:
                parts = line.strip().split(", ")
                if parts[0].split(": ")[1] == self.username_entry.get():
                    balance = float(parts[2].split(": ")[1].replace('$', '').replace(',', ''))  # Extract balance
                    new_balance = balance + amount  # Update balance
                    updated_line = f"{parts[0]}, {parts[1]}, Balance: ${new_balance:,.2f}\n"  # Updated line with new balance
                    updated_lines.append(updated_line)
                    found = True
                else:
                    updated_lines.append(line)  # Keep other lines unchanged

            if not found:
                messagebox.showerror("Error", "User not found.")
                deposit_window.destroy()
                return

            # Update user data file with the updated lines
            with open("user_data.txt", "w") as file:
                file.writelines(updated_lines)

            # Generate deposit slip
            deposit_slip = f"Deposited Amount: ${amount:,.2f}\nTotal Balance: ${new_balance:,.2f}"

            # Log deposit activity
            self.log_activity(self.username_entry.get(), f"Deposited ${amount:,.2f}. New balance: ${new_balance:,.2f}")

            # Write transaction details to CSV file
            self.transaction_writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                               self.username_entry.get(), "Deposit", amount])

            # Show success message with deposit slip
            messagebox.showinfo("Success",
                                f"Deposited ${amount:,.2f}. New balance: ${new_balance:,.2f}\n\n{deposit_slip}")
            deposit_window.destroy()
            # Close the transaction file
            self.transaction_file.close()

        # Create a window to enter the amount to deposit
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Deposit")

        # Amount Entry
        amount_label = tk.Label(deposit_window, text="Enter amount to deposit:")
        amount_label.pack()
        amount_entry = tk.Entry(deposit_window)
        amount_entry.pack()

        # Deposit Button
        deposit_button = tk.Button(deposit_window, text="Deposit", command=deposit_amount)
        deposit_button.pack()
    def withdraw(self):
        def withdraw_amount():
            # Get the entered amount
            amount = float(amount_entry.get())

            # Read user data from user_data.txt
            with open("user_data.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_lines = []  # To store updated lines with balance
            for line in lines:
                parts = line.strip().split(", ")
                if parts[0].split(": ")[1] == self.username_entry.get():
                    balance = float(parts[2].split(": ")[1].replace('$', '').replace(',', ''))  # Extract balance
                    if balance >= amount:
                        new_balance = balance - amount  # Update balance
                        updated_line = f"Username: {parts[0].split(': ')[1]}, Password: {parts[1].split(': ')[1]}, Balance: ${new_balance:,.2f}\n"  # Updated line with new balance
                        updated_lines.append(updated_line)
                        found = True
                    else:
                        messagebox.showerror("Error", "Insufficient balance.")
                        withdraw_window.destroy()
                        return
                else:
                    updated_lines.append(line)  # Keep other lines unchanged

            if not found:
                messagebox.showerror("Error", "User not found.")
                withdraw_window.destroy()
                return

            # Update user data file with the updated lines
            with open("user_data.txt", "w") as file:
                file.writelines(updated_lines)

            # Generate withdrawal slip
            withdrawal_slip = f"Withdrawn Amount: ${amount:,.2f}\nTotal Balance: ${new_balance:,.2f}"

            # Log withdrawal activity
            self.log_activity(self.username_entry.get(), f"Withdrawn ${amount:,.2f}. New balance: ${new_balance:,.2f}")

            # Write transaction details to CSV file
            self.transaction_writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                               self.username_entry.get(), "Withdrawal", amount])
            # Show success message with withdrawal slip
            messagebox.showinfo("Success",
                                f"Withdrawn ${amount:,.2f}. New balance: ${new_balance:,.2f}\n\n{withdrawal_slip}")
            withdraw_window.destroy()
            # Close the transaction file
            self.transaction_file.close()

        # Create a window to enter the amount to withdraw
        withdraw_window = tk.Toplevel(self.root)
        withdraw_window.title("Withdraw")

        # Amount Entry
        amount_label = tk.Label(withdraw_window, text="Enter amount to withdraw:")
        amount_label.pack()
        amount_entry = tk.Entry(withdraw_window)
        amount_entry.pack()

        # Withdraw Button
        withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=withdraw_amount)
        withdraw_button.pack()
    def request_checkbook(self):
        # Implement request checkbook functionality
        messagebox.showinfo("Checkbook Request", "Checkbook requested successfully!")
    def request_debit_credit_card(self):
        # Implement request debit/credit card functionality
        messagebox.showinfo("Debit/Credit Card Request", "Debit/Credit Card requested successfully!")

    def setup_recurring_payment(self):
        def setup_recurring():
            # Placeholder for setting up recurring payment functionality
            pass

        # Create a window to set up recurring payments
        recurring_window = tk.Toplevel(self.root)
        recurring_window.title("Setup Recurring Payments")

        # Recurring Payment Setup Label
        setup_label = tk.Label(recurring_window, text="Setup Recurring Payments")
        setup_label.pack(pady=10)

        # Recurring Payment Setup Description
        description_label = tk.Label(recurring_window, text="Enter details to set up recurring payments:")
        description_label.pack()

        # Recipient Username Entry
        recipient_username_label = tk.Label(recurring_window, text="Recipient Username:")
        recipient_username_label.pack()
        recipient_username_entry = tk.Entry(recurring_window)
        recipient_username_entry.pack()

        # Amount Entry
        amount_label = tk.Label(recurring_window, text="Enter recurring amount:")
        amount_label.pack()
        amount_entry = tk.Entry(recurring_window)
        amount_entry.pack()

        # Frequency Entry
        frequency_label = tk.Label(recurring_window, text="Enter frequency (e.g., monthly, weekly):")
        frequency_label.pack()
        frequency_entry = tk.Entry(recurring_window)
        frequency_entry.pack()

        # Setup Recurring Button
        setup_button = tk.Button(recurring_window, text="Setup Recurring Payment", command=setup_recurring)
        setup_button.pack()

    def setup_direct_debit(self):
        def setup_direct():
            # Placeholder for setting up direct debit functionality
            pass

        # Create a window to set up direct debit
        direct_window = tk.Toplevel(self.root)
        direct_window.title("Setup Direct Debit")

        # Direct Debit Setup Label
        setup_label = tk.Label(direct_window, text="Setup Direct Debit")
        setup_label.pack(pady=10)

        # Direct Debit Setup Description
        description_label = tk.Label(direct_window, text="Enter details to set up direct debit:")
        description_label.pack()

        # Payee Username Entry
        payee_username_label = tk.Label(direct_window, text="Payee Username:")
        payee_username_label.pack()
        payee_username_entry = tk.Entry(direct_window)
        payee_username_entry.pack()

        # Amount Entry
        amount_label = tk.Label(direct_window, text="Enter direct debit amount:")
        amount_label.pack()
        amount_entry = tk.Entry(direct_window)
        amount_entry.pack()

        # Setup Direct Debit Button
        setup_button = tk.Button(direct_window, text="Setup Direct Debit", command=setup_direct)
        setup_button.pack()



    def transfer_funds(self):
        def transfer():
            # Get the entered recipient username and amount
            recipient_username = recipient_username_entry.get()
            amount = float(amount_entry.get())

            # Perform transfer operation (update balances for sender and recipient)
            # Add your code to update balances in the user_data.txt file here

            # Log transfer activity
            self.log_activity(self.username_entry.get(), f"Transferred ${amount:,.2f} to {recipient_username}")

            # Write transaction details to CSV file
            self.transaction_writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                               self.username_entry.get(), "Transfer", amount])

            # Show success message
            messagebox.showinfo("Success", f"Funds transferred successfully to {recipient_username}!")
            transfer_window.destroy()

        # Create a window to enter recipient username and amount to transfer
        transfer_window = tk.Toplevel(self.root)
        transfer_window.title("Transfer Funds")

        # Recipient Username Entry
        recipient_username_label = tk.Label(transfer_window, text="Recipient Username:")
        recipient_username_label.pack()
        recipient_username_entry = tk.Entry(transfer_window)
        recipient_username_entry.pack()

        # Amount Entry
        amount_label = tk.Label(transfer_window, text="Enter amount to transfer:")
        amount_label.pack()
        amount_entry = tk.Entry(transfer_window)
        amount_entry.pack()

        # Transfer Button
        transfer_button = tk.Button(transfer_window, text="Transfer", command=transfer)
        transfer_button.pack()
        

    def run(self):
        self.root.mainloop()


# Instantiate the GUI and run it
banking_system_gui = BankingSystemGUI()
banking_system_gui.run()
