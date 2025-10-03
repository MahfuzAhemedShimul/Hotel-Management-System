import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Mahfuz Ahmed Shimul Paradise")

        # ---------------- MySQL Connection ----------------
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",       # default XAMPP user
            password="23303255",       # put your MySQL password if set
            database="hotel"   # our database
        )
        self.cursor = self.conn.cursor()

        # ---------------- Background ----------------
        self.bg_image = Image.open("hotel.jpg")
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ---------------- Variables ----------------
        self.name = tk.StringVar()
        self.address = tk.StringVar()
        self.cin = tk.StringVar()
        self.cout = tk.StringVar()
        self.rno = 101

        self.room_rent = 0
        self.food_bill = 0
        self.laundry_bill = 0
        self.game_bill = 0
        self.total = 0
        self.service_charge = 1800

        # ---------------- Center Frame ----------------
        frame = tk.Frame(self.root, bg="white", bd=3, relief="ridge")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=400)

        tk.Label(frame, text="🏨 Mahfuz Ahmed Shimul Paradise", font=("Arial", 14, "bold"), bg="white").pack(pady=20)

        tk.Button(frame, text="Enter Customer Data", width=25, bg="#FF9999", fg="black", command=self.customer_data).pack(pady=5)
        tk.Button(frame, text="Calculate Room Rent", width=25, bg="#99FF99", fg="black", command=self.room_rent_window).pack(pady=5)
        tk.Button(frame, text="Restaurant Bill", width=25, bg="#9999FF", fg="black", command=self.restaurant_window).pack(pady=5)
        tk.Button(frame, text="Laundry Bill", width=25, bg="#FFCC99", fg="black", command=self.laundry_window).pack(pady=5)
        tk.Button(frame, text="Game Bill", width=25, bg="#FF99FF", fg="black", command=self.game_window).pack(pady=5)
        tk.Button(frame, text="Show Total Bill", width=25, bg="#66CCCC", fg="black", command=self.display_bill).pack(pady=5)
        tk.Button(frame, text="Exit", width=25, bg="#CCCCCC", fg="black", command=root.quit).pack(pady=5)

    # ---------------- Customer Data ----------------
    def customer_data(self):
        top = tk.Toplevel(self.root)
        top.title("Customer Data")
        top.geometry("400x300")

        tk.Label(top, text="Name:").pack()
        tk.Entry(top, textvariable=self.name).pack()

        tk.Label(top, text="Address:").pack()
        tk.Entry(top, textvariable=self.address).pack()

        tk.Label(top, text="Check-in Date:").pack()
        tk.Entry(top, textvariable=self.cin).pack()

        tk.Label(top, text="Check-out Date:").pack()
        tk.Entry(top, textvariable=self.cout).pack()

        tk.Button(top, text="Save", command=lambda: [messagebox.showinfo("Saved", f"Customer {self.name.get()} added!"), top.destroy()]).pack(pady=10)

    # ---------------- Room Rent ----------------
    def room_rent_window(self):
        top = tk.Toplevel(self.root)
        top.title("Room Rent")
        top.geometry("400x300")

        tk.Label(top, text="Select Room Type", font=("Arial", 14)).pack(pady=10)

        tk.Button(top, text="SUITE - BDT 6000", command=lambda: self.calculate_rent(6000)).pack(pady=5)
        tk.Button(top, text="DELUX - BDT 5000", command=lambda: self.calculate_rent(5000)).pack(pady=5)
        tk.Button(top, text="DOUBLE - BDT 4000", command=lambda: self.calculate_rent(4000)).pack(pady=5)
        tk.Button(top, text="SINGLE - BDT 3000", command=lambda: self.calculate_rent(3000)).pack(pady=5)

    def calculate_rent(self, rate):
        nights_window = tk.Toplevel(self.root)
        nights_window.title("Number of Nights")
        nights_window.geometry("300x150")

        tk.Label(nights_window, text="Enter number of nights:").pack(pady=5)
        nights_entry = tk.Entry(nights_window)
        nights_entry.pack(pady=5)

        def calculate():
            try:
                nights = int(nights_entry.get())
                self.room_rent = rate * nights
                messagebox.showinfo("Room Rent", f"Room Rent: BDT {self.room_rent}")
                nights_window.destroy()
            except:
                messagebox.showerror("Error", "Enter valid number of nights!")

        tk.Button(nights_window, text="Calculate", command=calculate).pack(pady=10)

    # ---------------- Restaurant ----------------
    def restaurant_window(self):
        top = tk.Toplevel(self.root)
        top.title("Restaurant Menu")
        top.geometry("400x400")

        def add_food(price, item):
            self.food_bill += price
            messagebox.showinfo("Added", f"{item} added! Total = BDT {self.food_bill}")

        tk.Button(top, text="Water - BDT 20", command=lambda: add_food(20, "Water")).pack(pady=5)
        tk.Button(top, text="Tea - BDT 10", command=lambda: add_food(10, "Tea")).pack(pady=5)
        tk.Button(top, text="Breakfast - BDT 90", command=lambda: add_food(90, "Breakfast")).pack(pady=5)
        tk.Button(top, text="Lunch - BDT 110", command=lambda: add_food(110, "Lunch")).pack(pady=5)
        tk.Button(top, text="Dinner - BDT 150", command=lambda: add_food(150, "Dinner")).pack(pady=5)
        tk.Button(top, text="Snacks - BDT 100", command=lambda: add_food(100, "Snacks")).pack(pady=5)

    # ---------------- Laundry ----------------
    def laundry_window(self):
        top = tk.Toplevel(self.root)
        top.title("Laundry Menu")
        top.geometry("400x400")

        def add_laundry(price, item):
            self.laundry_bill += price
            messagebox.showinfo("Added", f"{item} added! Total = BDT {self.laundry_bill}")

        tk.Button(top, text="Shorts - BDT 30", command=lambda: add_laundry(30, "Shorts")).pack(pady=5)
        tk.Button(top, text="Trousers - BDT 40", command=lambda: add_laundry(40, "Trousers")).pack(pady=5)
        tk.Button(top, text="Shirt - BDT 50", command=lambda: add_laundry(50, "Shirt")).pack(pady=5)
        tk.Button(top, text="Jeans - BDT 60", command=lambda: add_laundry(60, "Jeans")).pack(pady=5)
        tk.Button(top, text="Girlsuit - BDT 80", command=lambda: add_laundry(80, "Girlsuit")).pack(pady=5)

    # ---------------- Games ----------------
    def game_window(self):
        top = tk.Toplevel(self.root)
        top.title("Game Menu")
        top.geometry("400x400")

        def add_game(price, item):
            self.game_bill += price
            messagebox.showinfo("Added", f"{item} added! Total = BDT {self.game_bill}")

        tk.Button(top, text="Table Tennis - BDT 60", command=lambda: add_game(60, "Table Tennis")).pack(pady=5)
        tk.Button(top, text="Bowling - BDT 80", command=lambda: add_game(80, "Bowling")).pack(pady=5)
        tk.Button(top, text="Snooker - BDT 70", command=lambda: add_game(70, "Snooker")).pack(pady=5)
        tk.Button(top, text="Video Games - BDT 90", command=lambda: add_game(90, "Video Games")).pack(pady=5)
        tk.Button(top, text="Pool - BDT 50", command=lambda: add_game(50, "Pool")).pack(pady=5)

    # ---------------- Display Final Bill ----------------
    def display_bill(self):
        self.total = self.room_rent + self.food_bill + self.laundry_bill + self.game_bill + self.service_charge

        # Save to MySQL
        sql = '''INSERT INTO customers
            (name, address, check_in, check_out, room_rent, food_bill, laundry_bill, game_bill, service_charge, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        values = (
            self.name.get(), self.address.get(), self.cin.get(), self.cout.get(),
            self.room_rent, self.food_bill, self.laundry_bill, self.game_bill,
            self.service_charge, self.total
        )
        self.cursor.execute(sql, values)
        self.conn.commit()

        # Show bill
        bill_text = f"""
***** HOTEL BILL *****
Name: {self.name.get()}
Address: {self.address.get()}
Check-in: {self.cin.get()}
Check-out: {self.cout.get()}
Room No: {self.rno}

Room Rent: BDT {self.room_rent}
Food Bill: BDT {self.food_bill}
Laundry Bill: BDT {self.laundry_bill}
Game Bill: BDT {self.game_bill}
Service Charges: BDT {self.service_charge}

-------------------------
Total: BDT {self.total}
"""
        messagebox.showinfo("Final Bill", bill_text)


# ---------------- Main ----------------
root = tk.Tk()
root.geometry("800x600")
app = HotelManagement(root)
root.mainloop()
