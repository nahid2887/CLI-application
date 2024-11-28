# **CLI-application** 👩‍💻👨‍💼  

Welcome to the **Employee Management System** — your one-stop solution to managing employee data with style! 🚀 Powered by **Python Flask** for the brains 🧠 and **Tailwind CSS** for the beauty 💅, this app does it all:  

- **Add Employees** (because everyone deserves a place 🌟)  
- **View All Employees** (because transparency is key 🔍)  
- **Search for Employees** (find them faster than HR 🕵️‍♀️)  
- **Update/Delete Employees** (give them a makeover or let them go 🧹)  
- **Save Data to File** (for the old-school backup fans 📝)  

---

## **🛠️ System Design**  

- **Backend:** Flask is our chef 🍳, cooking up those HTTP requests and managing data.  
- **Frontend:** Tailwind CSS brings the flavor 🌈 with responsive and clean designs.  
- **Storage:** Data lives in `employees.json` 📂 but gets immortalized in `employees.txt` 🗃️.  

---

## **🏗️ Routes Overview**  

- `/` — Your comfy home page. Add employees, search for them, or see the latest additions. 🏠  
- `/add` — Add employees with style. Collects ID, name, designation, number, and salary. 📝  
- `/view_all` — See everyone in one place! Edit or delete as needed. 🗂️  
- `/search` — Type a name or designation; we’ll find them for you. 🕵️‍♂️  
- `/update/<emp_id>` — Give employees a fresh new look with updated details. ✏️  
- `/delete/<emp_id>` — Goodbye, employee! You’ll live forever in our hearts. 🗑️  
- `/save_all` — Save all data to `employees.txt`. Perfect for backups or bragging. 💾  

---

## **💡 Features**  

1. **Add Employee**  
   No one left behind! Add employees with all the details they deserve.  
2. **View All Employees**  
   One screen, all employees. Who’s in charge of that raise? 😉  
3. **Search Employees**  
   Find employees by name or designation. Results pop up like magic! ✨  
4. **Update Employee**  
   Job change? New number? Higher salary? We’ve got you. 🚀  
5. **Delete Employee**  
   Say farewell with one click. 😢  
6. **Save Employees to TXT**  
   Your data deserves a backup. Save it beautifully. 💼  

---

## **⚡ How to Run This Masterpiece**  

1. Clone the project like a pro:  
   ```bash  
   git clone https://github.com/<your-username>/CLI-application.git

  Additional install the required dependencies 
 
pip install flask

Run the application:

python app.py

Open a web browser and navigate to: http://127.0.0.1:5000/

Conclusion

This solution provides a basic yet functional CLI application with features such as adding, viewing, searching, updating, deleting, and saving employees. The system leverages Flask for backend handling and Tailwind CSS for an attractive, responsive frontend.
