import tkinter as tk
from tkinter import messagebox




class GrindHockeyDevelopmentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grind Hockey Development")
        self.root.geometry("1000x800")

        self.pages = {}
        self.current_page = None

        self.create_widgets()
        self.show_welcome_page()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="black")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.pages["Signup"] = self.create_signup_page()
        self.pages["Confirmation"] = self.create_confirmation_page()
        self.pages["Welcome"] = self.create_welcome_page()

    def create_welcome_page(self):



        welcome_frame = tk.Frame(self.frame, bg="black")

        try:
            image = tk.PhotoImage(file="img_2.png" )
        except tk.TclError as e:
            print("Error loading image:", e)
            return welcome_frame

            # Add the image to the welcome page
        image_label = tk.Label(welcome_frame, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack(pady=10)
        # Welcome message



        tk.Label(welcome_frame, text="Welcome to Grind Hockey Development\n", fg="yellow", bg="black", font=("Arial", 20)).pack(pady=10)
        tk.Label(welcome_frame, text="Where good players become great\n ", fg="yellow", bg="black", font=("Arial", 20)).pack(pady=10)

        #Get Started Button
        get_started_button = tk.Button(welcome_frame, text="Let's Get Started", bg="yellow", fg="black",
                                       font=("Arial", 14), command=self.show_signup_page)
        get_started_button.pack(pady=10)

        description_text = "Grind Hockey Development is a premier hockey training program\n" \
                           "that offers various packages to improve your skills and\n" \
                           "performance on the ice. Get started today and take\n" \
                           "your game to the next level!\n" \
                           "This Training program is run by Jordan Degouw. \n" \
                           "There are 3 packages that can help carry you to the next level:\n"\
                           "The Hattrick gives you 3 icetimes per week and 3 1on1 sessions in the gym per week.\n" \
                           "The Bardown gives you 2 icetimes per week and  2 1on1 sessions in the gym per week.\n" \
                           "The Ovi gives you 1 icetime per week and  1 1on1 session in the gym per week.\n" \
                           "Players will receive a Tshirt, training shorts and a jersey upon arrival to their first session after signup!!\n"   \
                            "All packages include exclusive access to our state of the art facilities!\n"   \
                            "MONTHLY PAYMENTS RESET ON THE 1st OF EVERY MONTH!!"



        text_box = tk.Text(welcome_frame, wrap=tk.WORD, bg="light grey", fg="black", font=("Arial", 15))
        text_box.insert(tk.END, description_text)
        text_box.config(state=tk.DISABLED)
        text_box.pack(pady=10)


        return welcome_frame

    def create_signup_page(self):
        signup_frame = tk.Frame(self.frame, bg="black")
        self.pages["Signup"] = signup_frame  # Update the 'Signup' page reference
        try:
            image = tk.PhotoImage(file="img_2.png" )
        except tk.TclError as e:
            print("Error loading image:", e)
            return signup_frame

            # Add the image to the welcome page
        image_label = tk.Label(signup_frame, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack(pady=10)
        # Welcome message

        try:
            image = tk.PhotoImage(file="hackey.png")
            image_label = tk.Label(signup_frame, image=image, bg="black")
            image_label.image = image  # Keep a reference to the image to prevent garbage collection
            image_label.pack(side=tk.RIGHT, padx=20, pady=10)  # Adjust the padding as needed
        except tk.TclError as e:
            print("Error loading image:", e)
        # Package selection
        tk.Label(signup_frame, text="Select Package:", fg="yellow", bg="black", font=("Arial", 14)).pack(pady=5)
        self.package_var = tk.StringVar()  # Store the package variable as an instance attribute
        packages = [("Hat trick package: $1000", "HATTRICK"), ("Bardown package: $800", "BD"),
                    ("Ovi package: $600", "Ovi")]
        for package, value in packages:
            tk.Radiobutton(signup_frame, text=package, variable=self.package_var, value=value, bg="black", fg="white",
                           selectcolor="blue", font=("Arial", 12)).pack(pady=5)

        # User information entry fields
        fields = [("Name:", 30), ("Phone Number:", 15), ("Email:", 30), ("Date of Birth:", 15), ("Address:", 30)]
        self.entry_vars = []  # Store the entry variables as instance attributes
        for field, width in fields:
            label = tk.Label(signup_frame, text=field, fg="yellow", bg="black", font=("Arial", 12))
            label.pack(pady=5)
            entry_var = tk.StringVar()
            entry = tk.Entry(signup_frame, textvariable=entry_var, font=("Arial", 12), width=width)
            entry.pack(pady=5)
            self.entry_vars.append(entry_var)

        # Submit button
        submit_button = tk.Button(
            signup_frame,
            text="Submit",
            bg="yellow",
            fg="black",
            font=("Arial", 12),
            command=self.submit_signup_form  # Call the method to handle form submission
        )
        submit_button.pack(pady=10)


        return signup_frame

    def create_confirmation_page(self):
        confirmation_frame = tk.Frame(self.frame, bg="black")
        self.pages["Confirmation"] = confirmation_frame  # Update the 'Confirmation' page reference
        try:
            image = tk.PhotoImage(file="img_2.png")
        except tk.TclError as e:
            print("Error loading image:", e)
            return confirmation_frame

            # Add the image to the welcome page
        image_label = tk.Label(confirmation_frame, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack(pady=10)
        # Thank you message
        tk.Label(confirmation_frame, text="Thank you for signing up!", fg="Yellow", bg="black",  font=("Arial", 20)).pack(pady=10)

        # User information confirmation
        self.confirmation_label = tk.Label(confirmation_frame, fg="yellow", bg="black", font=("Arial", 24))
        self.confirmation_label.pack(pady=10)


        # Back to Welcome button
        back_button = tk.Button(confirmation_frame, text="New Submission", bg="yellow", fg="black",
                                font=("Arial", 12), command=self.show_welcome_page)
        back_button.pack(pady=5)

        # Close Window button
        close_button = tk.Button(confirmation_frame, text="Done", bg="red", fg="white",
                                 font=("Arial", 12), command=self.root.destroy)
        close_button.pack(pady=5)

        return confirmation_frame

    def show_welcome_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.pages["Welcome"]
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def show_signup_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.pages["Signup"]
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def show_confirmation_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.pages["Confirmation"]
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def submit_signup_form(self):
        package = self.package_var.get()
        entry_vars = [entry_var.get() for entry_var in self.entry_vars]

        name, phone, email, dob, address = entry_vars

        if not name or not phone or not email or not dob or not address:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        if not package:
            messagebox.showerror("Error", "Please select a package.")
            return

        # Confirmation text
        confirmation_text = (
            "Your information: \n"
            f"Name: {name}\n"
            f"Package: {package}\n"
            f"Phone Number: {phone}\n"
            f"Email: {email}\n"
            f"Date of Birth: {dob}\n"
            f"Address: {address}"
        )
        self.confirmation_label.config(text=confirmation_text)
        self.show_confirmation_page()





if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="black")
    grind_hockey_app = GrindHockeyDevelopmentGUI(root)
    root.mainloop()
