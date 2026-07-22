from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv
import os
from datetime import datetime

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Results Management System")
        self.root.geometry("1400x700+50+50")
        self.root.config(bg="white")
        
        # File paths
        self.courses_file = "courses.csv"
        self.students_file = "students.csv"
        self.results_file = "results.csv"
        
        # Initialize files
        self.init_files()
        
        # Load data from files
        self.courses_data = self.read_courses()
        self.students_data = self.read_students()
        self.results_data = self.read_results()
        
        # Variables
        self.course_var = StringVar()
        self.student_id_var = StringVar()
        self.student_name_var = StringVar()
        self.student_email_var = StringVar()
        self.student_phone_var = StringVar()
        self.student_address_var = StringVar()
        self.search_var = StringVar()
        
        # For selected item IDs
        self.selected_course_id = None
        self.selected_student_id = None
        self.selected_result_id = None
        
        # Title
        self.logo_dash = None
        try:
            self.logo_dash = ImageTk.PhotoImage(Image.open("logo.png").resize((40, 40)))
        except:
            self.logo_dash = None
            
        title_frame = Frame(root, bg="#033054", height=60)
        title_frame.pack(fill="x")
        
        if self.logo_dash:
            lbl_icon = Label(title_frame, image=self.logo_dash, bg="#033054")
            lbl_icon.place(x=10, y=10)
            
        lbl_title = Label(title_frame, text="Student Result Management System", 
                         font=("Times New Roman", 25, "bold"), 
                         bg="#033054", fg="white")
        lbl_title.pack(pady=10)
        
        # Menu Frame
        self.create_menu()
        
        # Main Content Frame
        self.main_content = Frame(root, bg="white")
        self.main_content.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Show Dashboard by default
        self.show_dashboard()
        
    def init_files(self):
        """Initialize CSV files with headers if they don't exist"""
        try:
            # Courses file
            if not os.path.exists(self.courses_file):
                with open(self.courses_file, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['id', 'course_name', 'duration', 'fee'])
            
            # Students file
            if not os.path.exists(self.students_file):
                with open(self.students_file, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['id', 'student_id', 'name', 'email', 'phone', 'address', 'course', 'enrollment_date'])
            
            # Results file
            if not os.path.exists(self.results_file):
                with open(self.results_file, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['id', 'student_id', 'course', 'subject', 'marks', 'grade', 'exam_date'])
                    
        except Exception as e:
            messagebox.showerror("File Error", f"Error initializing files: {str(e)}")
    
    # ==================== FILE OPERATIONS ====================
    
    def read_courses(self):
        """Read courses from CSV file"""
        courses = []
        try:
            with open(self.courses_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    courses.append({
                        'id': int(row['id']) if row['id'] else 0,
                        'course_name': row['course_name'],
                        'duration': row['duration'],
                        'fee': float(row['fee']) if row['fee'] else 0
                    })
        except FileNotFoundError:
            self.init_files()
        except Exception as e:
            messagebox.showerror("File Error", f"Error reading courses: {str(e)}")
        return courses
    
    def write_courses(self):
        """Write courses to CSV file"""
        try:
            with open(self.courses_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'course_name', 'duration', 'fee'])
                for course in self.courses_data:
                    writer.writerow([course['id'], course['course_name'], course['duration'], course['fee']])
        except Exception as e:
            messagebox.showerror("File Error", f"Error writing courses: {str(e)}")
    
    def read_students(self):
        """Read students from CSV file"""
        students = []
        try:
            with open(self.students_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append({
                        'id': int(row['id']) if row['id'] else 0,
                        'student_id': row['student_id'],
                        'name': row['name'],
                        'email': row['email'],
                        'phone': row['phone'],
                        'address': row['address'],
                        'course': row['course'],
                        'enrollment_date': row['enrollment_date']
                    })
        except FileNotFoundError:
            self.init_files()
        except Exception as e:
            messagebox.showerror("File Error", f"Error reading students: {str(e)}")
        return students
    
    def write_students(self):
        """Write students to CSV file"""
        try:
            with open(self.students_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'student_id', 'name', 'email', 'phone', 'address', 'course', 'enrollment_date'])
                for student in self.students_data:
                    writer.writerow([student['id'], student['student_id'], student['name'], 
                                   student['email'], student['phone'], student['address'],
                                   student['course'], student['enrollment_date']])
        except Exception as e:
            messagebox.showerror("File Error", f"Error writing students: {str(e)}")
    
    def read_results(self):
        """Read results from CSV file"""
        results = []
        try:
            with open(self.results_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    results.append({
                        'id': int(row['id']) if row['id'] else 0,
                        'student_id': row['student_id'],
                        'course': row['course'],
                        'subject': row['subject'],
                        'marks': float(row['marks']) if row['marks'] else 0,
                        'grade': row['grade'],
                        'exam_date': row['exam_date']
                    })
        except FileNotFoundError:
            self.init_files()
        except Exception as e:
            messagebox.showerror("File Error", f"Error reading results: {str(e)}")
        return results
    
    def write_results(self):
        """Write results to CSV file"""
        try:
            with open(self.results_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'student_id', 'course', 'subject', 'marks', 'grade', 'exam_date'])
                for result in self.results_data:
                    writer.writerow([result['id'], result['student_id'], result['course'],
                                   result['subject'], result['marks'], result['grade'], result['exam_date']])
        except Exception as e:
            messagebox.showerror("File Error", f"Error writing results: {str(e)}")
    
    def get_next_course_id(self):
        """Get next available course ID"""
        if not self.courses_data:
            return 1
        return max(course['id'] for course in self.courses_data) + 1
    
    def get_next_student_id(self):
        """Get next available student record ID"""
        if not self.students_data:
            return 1
        return max(student['id'] for student in self.students_data) + 1
    
    def get_next_result_id(self):
        """Get next available result ID"""
        if not self.results_data:
            return 1
        return max(result['id'] for result in self.results_data) + 1
    
    def create_menu(self):
        """Create centered menu buttons"""
        menu_frame = Frame(self.root, bg="white", height=70)
        menu_frame.pack(fill="x", pady=10)
        
        inner_frame = Frame(menu_frame, bg="white")
        inner_frame.pack(expand=True)
        
        btn_style = {
            "font": ("Arial", 11, "bold"),
            "bg": "#0b5377",
            "fg": "white",
            "cursor": "hand2",
            "relief": "raised",
            "bd": 2,
            "width": 15,
            "height": 1
        }
        
        buttons = [
            ("🏠 Dashboard", self.show_dashboard),
            ("📚 Courses", self.show_courses),
            ("👥 Students", self.show_students),
            ("📊 Results", self.show_results),
            ("👁️ View Results", self.view_results),
            ("📋 Student List", self.show_student_list_only),  
            ("🚪 Logout", self.logout),
            ("❌ Exit", self.exit_app)
        ]
        
        for text, command in buttons:
            btn = Button(inner_frame, text=text, command=command, **btn_style)
            btn.pack(side="left", padx=8, pady=10)
            
        separator = Frame(self.root, height=2, bg="#033054")
        separator.pack(fill="x", padx=20)
            
    def clear_main_content(self):
        """Clear main content frame"""
        for widget in self.main_content.winfo_children():
            widget.destroy()
            
    # ==================== DASHBOARD ====================
    
    def show_dashboard(self):
        """Show dashboard with statistics"""
        self.clear_main_content()
        
        # Refresh data from files
        self.courses_data = self.read_courses()
        self.students_data = self.read_students()
        self.results_data = self.read_results()
        
        welcome_frame = Frame(self.main_content, bg="white")
        welcome_frame.pack(fill="x", pady=10)
        
        Label(welcome_frame, text="Welcome to Student Results Management System",
              font=("Arial", 18, "bold"), bg="white", fg="#033054").pack()
        
        stats_frame = Frame(self.main_content, bg="white")
        stats_frame.pack(fill="x", pady=20)
        
        student_count = len(self.students_data)
        course_count = len(self.courses_data)
        result_count = len(self.results_data)
        
        # Calculate pass rate
        if self.results_data:
            passed = sum(1 for r in self.results_data if float(r['marks']) >= 35)
            pass_rate = (passed / len(self.results_data)) * 100
            pass_rate_text = f"{pass_rate:.1f}%"
        else:
            pass_rate_text = "N/A"
        
        card_frame = Frame(stats_frame, bg="white")
        card_frame.pack(expand=True)
        
        cards = [
            ("🎓 Total Students", student_count, "#4CAF50"),
            ("📚 Total Courses", course_count, "#2196F3"),
            ("📝 Total Results", result_count, "#FF9800"),
            ("⭐ Pass Rate", pass_rate_text, "#9C27B0")
        ]
        
        for title, value, color in cards:
            card = Frame(card_frame, bg=color, width=200, height=120, relief="raised", bd=2)
            card.pack(side="left", padx=15, pady=10)
            card.pack_propagate(False)
            
            Label(card, text=title, font=("Arial", 11), bg=color, fg="white").pack(pady=10)
            Label(card, text=str(value), font=("Arial", 20, "bold"), bg=color, fg="white").pack()
            
        recent_frame = LabelFrame(self.main_content, text="System Statistics", 
                                  font=("Arial", 14, "bold"), bg="white", fg="#033054")
        recent_frame.pack(fill="both", expand=True, pady=20, padx=20)
        
        # Display summary
        summary_text = f"""
        📊 System Summary:
        
        • Total Courses: {course_count}
        • Total Students: {student_count}
        • Total Results: {result_count}
        • Data Files: courses.csv, students.csv, results.csv
        
        All data is automatically saved to CSV files.
        """
        
        Label(recent_frame, text=summary_text, font=("Arial", 12), 
              bg="white", justify=LEFT).pack(padx=20, pady=20)
    
    # ==================== COURSE MANAGEMENT ====================
    
    def show_courses(self):
        """Show course management interface with update/delete buttons"""
        self.clear_main_content()
        
        # Refresh courses data
        self.courses_data = self.read_courses()
        
        # Header
        header_frame = Frame(self.main_content, bg="white")
        header_frame.pack(fill="x", pady=10)
        Label(header_frame, text="Course Management", font=("Arial", 18, "bold"),
              bg="white", fg="#033054").pack()
        
        # Course Form
        form_frame = LabelFrame(self.main_content, text="Add New Course", 
                                font=("Arial", 12, "bold"), bg="white", fg="#033054")
        form_frame.pack(fill="x", padx=200, pady=10)
        
        Label(form_frame, text="Course Name:", bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.course_name_entry = Entry(form_frame, width=30, font=("Arial", 10))
        self.course_name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        Label(form_frame, text="Duration (months):", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.course_duration_entry = Entry(form_frame, width=30, font=("Arial", 10))
        self.course_duration_entry.grid(row=1, column=1, padx=10, pady=10)
        
        Label(form_frame, text="Fee (Rs):", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.course_fee_entry = Entry(form_frame, width=30, font=("Arial", 10))
        self.course_fee_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Buttons
        btn_frame = Frame(form_frame, bg="white")
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        large_btn_style = {
            "font": ("Arial", 12, "bold"),
            "fg": "white",
            "cursor": "hand2",
            "relief": "raised",
            "bd": 3,
            "width": 15,
            "height": 2,
            "justify": "center"
        }
        
        Button(btn_frame, text="➕ ADD", command=self.add_course,
               bg="#4CAF50", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="✏️ UPDATE", command=self.update_course,
               bg="#FF9800", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="🗑️ DELETE", command=self.delete_course,
               bg="#f44336", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="🔄 CLEAR", command=self.clear_course_form,
               bg="#607D8B", **large_btn_style).pack(side="left", padx=8)
        
        # Course List
        list_frame = LabelFrame(self.main_content, text="Course List (Click to Select)", 
                                font=("Arial", 12, "bold"), bg="white", fg="#033054")
        list_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Treeview for courses
        columns = ("ID", "Course Name", "Duration", "Fee (Rs)")
        self.course_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.course_tree.heading(col, text=col)
            self.course_tree.column(col, width=150)
            
        # Bind select event
        self.course_tree.bind('<<TreeviewSelect>>', self.on_course_select)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.course_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.course_tree.configure(yscrollcommand=scrollbar.set)
        self.course_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Load courses
        self.load_courses()
        
    def on_course_select(self, event):
        """Handle course selection from treeview"""
        selected = self.course_tree.selection()
        if selected:
            item = self.course_tree.item(selected[0])
            values = item['values']
            self.selected_course_id = values[0]
            
            # Fill the form with selected course data
            self.course_name_entry.delete(0, END)
            self.course_name_entry.insert(0, values[1])
            
            self.course_duration_entry.delete(0, END)
            self.course_duration_entry.insert(0, values[2])
            
            self.course_fee_entry.delete(0, END)
            self.course_fee_entry.insert(0, values[3])
    
    def add_course(self):
        """Add new course to CSV file"""
        name = self.course_name_entry.get()
        duration = self.course_duration_entry.get()
        fee = self.course_fee_entry.get()
        
        if not name or not duration or not fee:
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            # Check for duplicate course name
            for course in self.courses_data:
                if course['course_name'].lower() == name.lower():
                    messagebox.showerror("Error", "Course already exists!")
                    return
            
            # Create new course
            new_course = {
                'id': self.get_next_course_id(),
                'course_name': name,
                'duration': duration,
                'fee': float(fee)
            }
            
            self.courses_data.append(new_course)
            self.write_courses()
            
            messagebox.showinfo("Success", "✅ Course added successfully!")
            self.load_courses()
            self.clear_course_form()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid fee value!")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding course: {str(e)}")
    
    def update_course(self):
        """Update selected course"""
        if not self.selected_course_id:
            messagebox.showerror("Error", "Please select a course to update!")
            return
            
        name = self.course_name_entry.get()
        duration = self.course_duration_entry.get()
        fee = self.course_fee_entry.get()
        
        if not name or not duration or not fee:
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            # Find and update course
            for course in self.courses_data:
                if course['id'] == self.selected_course_id:
                    course['course_name'] = name
                    course['duration'] = duration
                    course['fee'] = float(fee)
                    break
            
            self.write_courses()
            
            messagebox.showinfo("Success", "✅ Course updated successfully!")
            self.load_courses()
            self.clear_course_form()
            self.selected_course_id = None
            
        except ValueError:
            messagebox.showerror("Error", "Invalid fee value!")
        except Exception as e:
            messagebox.showerror("Error", f"Error updating course: {str(e)}")
    
    def delete_course(self):
        """Delete selected course"""
        if not self.selected_course_id:
            messagebox.showerror("Error", "Please select a course to delete!")
            return
            
        result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this course?")
        if result:
            try:
                # Remove course
                self.courses_data = [c for c in self.courses_data if c['id'] != self.selected_course_id]
                self.write_courses()
                
                messagebox.showinfo("Success", "✅ Course deleted successfully!")
                self.load_courses()
                self.clear_course_form()
                self.selected_course_id = None
                
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting course: {str(e)}")
    
    def clear_course_form(self):
        """Clear course form fields"""
        self.course_name_entry.delete(0, END)
        self.course_duration_entry.delete(0, END)
        self.course_fee_entry.delete(0, END)
        self.selected_course_id = None
        
    def load_courses(self):
        """Load courses into treeview"""
        for item in self.course_tree.get_children():
            self.course_tree.delete(item)
            
        for course in self.courses_data:
            self.course_tree.insert("", "end", values=(
                course['id'],
                course['course_name'],
                course['duration'],
                f"Rs. {course['fee']:.2f}"
            ))
    
    # ==================== STUDENT MANAGEMENT WITH LIVE SEARCH ====================
    
    def show_students(self):
        """Show student management interface with update/delete buttons and live search"""
        self.clear_main_content()
        
        # Refresh data
        self.courses_data = self.read_courses()
        self.students_data = self.read_students()
        
        header_frame = Frame(self.main_content, bg="white")
        header_frame.pack(fill="x", pady=10)
        Label(header_frame, text="Student Management", font=("Arial", 18, "bold"),
              bg="white", fg="#033054").pack()
        
        # Student Form
        form_frame = LabelFrame(self.main_content, text="Student Registration Form", 
                                font=("Arial", 12, "bold"), bg="white", fg="#033054")
        form_frame.pack(fill="x", padx=200, pady=10)
        
        # Form fields
        labels = ["Student ID:", "Name:", "Email:", "Phone:", "Address:", "Course:"]
        self.student_entries = []
        
        for i, label in enumerate(labels):
            Label(form_frame, text=label, bg="white", font=("Arial", 10)).grid(row=i, column=0, padx=10, pady=8, sticky="w")
            
            if label == "Course:":
                # Course dropdown
                self.student_course_combo = ttk.Combobox(form_frame, font=("Arial", 10), width=27)
                self.student_course_combo.grid(row=i, column=1, padx=10, pady=8)
                
                # Load courses
                courses = [course['course_name'] for course in self.courses_data]
                self.student_course_combo['values'] = courses
                self.student_entries.append(self.student_course_combo)
            else:
                entry = Entry(form_frame, width=30, font=("Arial", 10))
                entry.grid(row=i, column=1, padx=10, pady=8)
                self.student_entries.append(entry)
                
        # Buttons
        btn_frame = Frame(form_frame, bg="white")
        btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
        
        large_btn_style = {
            "font": ("Arial", 12, "bold"),
            "fg": "white",
            "cursor": "hand2",
            "relief": "raised",
            "bd": 3,
            "width": 15,
            "height": 2,
            "justify": "center"
        }
        
        Button(btn_frame, text="➕ ADD", command=self.add_student,
               bg="#4CAF50", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="✏️ UPDATE", command=self.update_student,
               bg="#FF9800", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="🗑️ DELETE", command=self.delete_student,
               bg="#f44336", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="🔄 CLEAR", command=self.clear_student_form,
               bg="#607D8B", **large_btn_style).pack(side="left", padx=8)
        
        # Search Frame - UPDATED for live search
        search_frame = Frame(self.main_content, bg="white")
        search_frame.pack(fill="x", padx=200, pady=10)
        
        Label(search_frame, text="🔍 Search Student:", bg="white", font=("Arial", 10)).pack(side="left", padx=5)
        
        # Create search variable and entry with trace for live search
        self.search_var = StringVar()
        self.search_var.trace('w', lambda *args: self.live_search_students())
        
        self.search_entry = Entry(search_frame, textvariable=self.search_var, width=30, font=("Arial", 10))
        self.search_entry.pack(side="left", padx=5)
        
        # Add search tips
        tips_label = Label(search_frame, text="(Type to search - searches by ID, Name, Course, or Phone)", 
                           bg="white", font=("Arial", 8, "italic"), fg="gray")
        tips_label.pack(side="left", padx=10)
        
        # Clear search button
        Button(search_frame, text="✖ Clear", command=self.clear_search,
               bg="#f44336", fg="white", font=("Arial", 8, "bold"), width=8).pack(side="left", padx=5)
        
        # Student List with counter
        list_header_frame = Frame(self.main_content, bg="white")
        list_header_frame.pack(fill="x", padx=20)
        
        self.student_count_label = Label(list_header_frame, text="", bg="white", font=("Arial", 10, "italic"))
        self.student_count_label.pack(side="left")
        
        # Export button for student list
        export_btn = Button(list_header_frame, text="📥 Export to CSV", command=self.export_student_list,
                           bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), 
                           cursor="hand2", padx=10)
        export_btn.pack(side="right", padx=5)
        
        # Print button
        print_btn = Button(list_header_frame, text="🖨️ Print List", command=self.print_student_list,
                          bg="#FF9800", fg="white", font=("Arial", 9, "bold"),
                          cursor="hand2", padx=10)
        print_btn.pack(side="right", padx=5)
        
        # Refresh button
        refresh_btn = Button(list_header_frame, text="🔄 Refresh", command=self.refresh_student_list,
                            bg="#2196F3", fg="white", font=("Arial", 9, "bold"),
                            cursor="hand2", padx=10)
        refresh_btn.pack(side="right", padx=5)
        
        list_frame = LabelFrame(self.main_content, text="Student List (Click to Select)", 
                                font=("Arial", 12, "bold"), bg="white", fg="#033054")
        list_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        columns = ("ID", "Student ID", "Name", "Email", "Phone", "Course", "Enrollment Date")
        self.student_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=12)
        
        # Configure columns
        column_widths = [50, 100, 150, 180, 100, 120, 100]
        for col, width in zip(columns, column_widths):
            self.student_tree.heading(col, text=col)
            self.student_tree.column(col, width=width)
        
        # Add sorting functionality
        for col in columns:
            self.student_tree.heading(col, command=lambda c=col: self.sort_treeview(self.student_tree, c, False))
        
        # Bind select event
        self.student_tree.bind('<<TreeviewSelect>>', self.on_student_select)
        
        # Add double-click to select
        self.student_tree.bind('<Double-Button-1>', self.on_student_double_click)
        
        # Add scrollbars
        vsb = ttk.Scrollbar(list_frame, orient="vertical", command=self.student_tree.yview)
        hsb = ttk.Scrollbar(list_frame, orient="horizontal", command=self.student_tree.xview)
        self.student_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        self.student_tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Load students
        self.load_students()
        
        # Bind keyboard shortcuts
        self.search_entry.bind('<Return>', lambda event: self.live_search_students())
        self.search_entry.bind('<Escape>', lambda event: self.clear_search())
        
        # Set focus to search entry
        self.search_entry.focus()
    
    def show_student_list_only(self):
        """Show only the student list without the form"""
        self.clear_main_content()
        
        # Refresh data
        self.students_data = self.read_students()
        
        header_frame = Frame(self.main_content, bg="white")
        header_frame.pack(fill="x", pady=10)
        Label(header_frame, text="Student List", font=("Arial", 18, "bold"),
              bg="white", fg="#033054").pack()
        
        # Search Frame
        search_frame = Frame(self.main_content, bg="white")
        search_frame.pack(fill="x", padx=200, pady=10)
        
        Label(search_frame, text="🔍 Search Student:", bg="white", font=("Arial", 10)).pack(side="left", padx=5)
        
        # Create search variable and entry with trace for live search
        self.search_var = StringVar()
        self.search_var.trace('w', lambda *args: self.live_search_students_list_only())
        
        self.search_entry = Entry(search_frame, textvariable=self.search_var, width=30, font=("Arial", 10))
        self.search_entry.pack(side="left", padx=5)
        
        # Add search tips
        tips_label = Label(search_frame, text="(Type to search - searches by ID, Name, Course, or Phone)", 
                           bg="white", font=("Arial", 8, "italic"), fg="gray")
        tips_label.pack(side="left", padx=10)
        
        # Clear search button
        Button(search_frame, text="✖ Clear", command=self.clear_search_list_only,
               bg="#f44336", fg="white", font=("Arial", 8, "bold"), width=8).pack(side="left", padx=5)
        
        # Student List with counter
        list_header_frame = Frame(self.main_content, bg="white")
        list_header_frame.pack(fill="x", padx=20)
        
        self.student_count_label = Label(list_header_frame, text="", bg="white", font=("Arial", 10, "italic"))
        self.student_count_label.pack(side="left")
        
        # Export button for student list
        export_btn = Button(list_header_frame, text="📥 Export to CSV", command=self.export_student_list,
                           bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), 
                           cursor="hand2", padx=10)
        export_btn.pack(side="right", padx=5)
        
        # Print button
        print_btn = Button(list_header_frame, text="🖨️ Print List", command=self.print_student_list,
                          bg="#FF9800", fg="white", font=("Arial", 9, "bold"),
                          cursor="hand2", padx=10)
        print_btn.pack(side="right", padx=5)
        
        # Refresh button
        refresh_btn = Button(list_header_frame, text="🔄 Refresh", command=self.refresh_student_list_only,
                            bg="#2196F3", fg="white", font=("Arial", 9, "bold"),
                            cursor="hand2", padx=10)
        refresh_btn.pack(side="right", padx=5)
        
        # Back button
        back_btn = Button(list_header_frame, text="◀ Back", command=self.show_dashboard,
                         bg="#607D8B", fg="white", font=("Arial", 9, "bold"),
                         cursor="hand2", padx=10)
        back_btn.pack(side="right", padx=5)
        
        list_frame = LabelFrame(self.main_content, text="Complete Student List", 
                                font=("Arial", 12, "bold"), bg="white", fg="#033054")
        list_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        columns = ("Student ID", "Name", "Email", "Phone", "Course", "Enrollment Date")
        self.student_list_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        # Configure columns
        column_widths = [100, 150, 180, 100, 120, 100]
        for col, width in zip(columns, column_widths):
            self.student_list_tree.heading(col, text=col)
            self.student_list_tree.column(col, width=width)
        
        # Add sorting functionality
        for col in columns:
            self.student_list_tree.heading(col, command=lambda c=col: self.sort_treeview(self.student_list_tree, c, False))
        
        # Add scrollbars
        vsb = ttk.Scrollbar(list_frame, orient="vertical", command=self.student_list_tree.yview)
        hsb = ttk.Scrollbar(list_frame, orient="horizontal", command=self.student_list_tree.xview)
        self.student_list_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        self.student_list_tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
       
        
        # Bind keyboard shortcuts
        self.search_entry.bind('<Return>', lambda event: self.live_search_students_list_only())
        self.search_entry.bind('<Escape>', lambda event: self.clear_search_list_only())
        
        # Set focus to search entry
        self.search_entry.focus()
    
    def load_student_list_only(self):
        """Load students into the list-only view"""
        for item in self.student_list_tree.get_children():
            self.student_list_tree.delete(item)
        
        for student in self.students_data:
            self.student_list_tree.insert("", "end", values=(
                student['student_id'],
                student['name'],
                student['email'],
                student['phone'],
                student['course'],
                student['enrollment_date']
            ))
        
        # Update count label
        if hasattr(self, 'student_count_label'):
            self.student_count_label.config(text=f"📊 Total Students: {len(self.students_data)}", fg="green")
    
    def live_search_students_list_only(self):
        """Live search for list-only view"""
        search_term = self.search_var.get().strip().lower()
        
        # Clear treeview
        for item in self.student_list_tree.get_children():
            self.student_list_tree.delete(item)
        
        if not search_term:
            # If search is empty, show all students
            self.load_student_list_only()
            return
        
        # Search in multiple fields
        matched_students = []
        for student in self.students_data:
            # Search in Student ID, Name, Course, Phone, Email
            if (search_term in student['student_id'].lower() or
                search_term in student['name'].lower() or
                search_term in student['course'].lower() or
                search_term in student['phone'].lower() or
                search_term in student['email'].lower()):
                matched_students.append(student)
        
        # Display matched students
        for student in matched_students:
            self.student_list_tree.insert("", "end", values=(
                student['student_id'],
                student['name'],
                student['email'],
                student['phone'],
                student['course'],
                student['enrollment_date']
            ))
        
        # Update count label
        total = len(self.students_data)
        count = len(matched_students)
        if count == total:
            self.student_count_label.config(text=f"📊 Showing all {total} students", fg="green")
        else:
            self.student_count_label.config(text=f"📊 Found {count} of {total} students", fg="blue")
    
    def clear_search_list_only(self):
        """Clear search for list-only view"""
        self.search_var.set("")
        self.search_entry.focus()
    
    def refresh_student_list_only(self):
        """Refresh student list-only view"""
        self.students_data = self.read_students()
        self.load_student_list_only()
        messagebox.showinfo("Success", "Student list refreshed!")
    
    def export_student_list(self):
        """Export student list to a separate CSV file"""
        try:
            filename = f"student_list_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Student ID', 'Name', 'Email', 'Phone', 'Address', 'Course', 'Enrollment Date'])
                for student in self.students_data:
                    writer.writerow([
                        student['student_id'],
                        student['name'],
                        student['email'],
                        student['phone'],
                        student['address'],
                        student['course'],
                        student['enrollment_date']
                    ])
            messagebox.showinfo("Success", f"Student list exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting student list: {str(e)}")
    
    def print_student_list(self):
        """Print student list (creates a text file for printing)"""
        try:
            filename = f"student_list_print_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("="*80 + "\n")
                file.write("STUDENT LIST\n")
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("="*80 + "\n\n")
                
                file.write(f"{'Student ID':<12} {'Name':<20} {'Email':<25} {'Phone':<12} {'Course':<15}\n")
                file.write("-"*80 + "\n")
                
                for student in self.students_data:
                    file.write(f"{student['student_id']:<12} {student['name']:<20} "
                             f"{student['email']:<25} {student['phone']:<12} {student['course']:<15}\n")
                
                file.write("\n" + "="*80 + "\n")
                file.write(f"Total Students: {len(self.students_data)}\n")
            
            messagebox.showinfo("Success", f"Printable student list saved to {filename}")
            
            # Open the file with default text editor
            os.startfile(filename)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error creating print file: {str(e)}")
    
    def refresh_student_list(self):
        """Refresh student list"""
        self.students_data = self.read_students()
        self.load_students()
        messagebox.showinfo("Success", "Student list refreshed!")
    
    def live_search_students(self):
        """Live search students as you type"""
        search_term = self.search_var.get().strip().lower()
        
        # Clear treeview
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)
        
        if not search_term:
            # If search is empty, show all students
            self.load_students()
            return
        
        # Search in multiple fields
        matched_students = []
        for student in self.students_data:
            # Search in Student ID, Name, Course, Phone, Email
            if (search_term in student['student_id'].lower() or
                search_term in student['name'].lower() or
                search_term in student['course'].lower() or
                search_term in student['phone'].lower() or
                search_term in student['email'].lower()):
                matched_students.append(student)
        
        # Display matched students
        for student in matched_students:
            self.student_tree.insert("", "end", values=(
                student['id'],
                student['student_id'],
                student['name'],
                student['email'],
                student['phone'],
                student['course'],
                student['enrollment_date']
            ))
        
        # Update count label
        self.update_student_count(len(matched_students))
        
        # Highlight search term in results
        if matched_students:
            # Select first result
            first_item = self.student_tree.get_children()[0]
            self.student_tree.selection_set(first_item)
            self.student_tree.focus(first_item)
            self.student_tree.see(first_item)
    
    def update_student_count(self, count=None):
        """Update the student count label"""
        if count is None:
            count = len(self.students_data)
        
        total = len(self.students_data)
        if count == total:
            self.student_count_label.config(text=f"📊 Showing all {total} students", fg="green")
        else:
            self.student_count_label.config(text=f"📊 Found {count} of {total} students", fg="blue")
    
    def clear_search(self):
        """Clear search field and show all students"""
        self.search_var.set("")  # This will trigger live_search_students via trace
        self.search_entry.focus()
    
    def sort_treeview(self, tree, col, reverse):
        """Sort treeview column"""
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        
        for index, (val, child) in enumerate(data):
            tree.move(child, '', index)
        
        tree.heading(col, command=lambda: self.sort_treeview(tree, col, not reverse))
    
    def on_student_double_click(self, event):
        """Handle double click on student - select and show details"""
        selected = self.student_tree.selection()
        if selected:
            self.on_student_select(event)
            # Optionally show a message with student details
            item = self.student_tree.item(selected[0])
            values = item['values']
            messagebox.showinfo("Student Details", 
                              f"Student ID: {values[1]}\n"
                              f"Name: {values[2]}\n"
                              f"Email: {values[3]}\n"
                              f"Phone: {values[4]}\n"
                              f"Course: {values[5]}")
    
    def on_student_select(self, event):
        """Handle student selection from treeview"""
        selected = self.student_tree.selection()
        if selected:
            item = self.student_tree.item(selected[0])
            values = item['values']
            self.selected_student_id = values[1]  # student_id
            
            # Fill the form with selected student data
            self.clear_student_form()
            self.student_entries[0].insert(0, values[1])  # student_id
            self.student_entries[1].insert(0, values[2])  # name
            self.student_entries[2].insert(0, values[3])  # email
            self.student_entries[3].insert(0, values[4])  # phone
            self.student_entries[4].insert(0, values[5])  # address
            self.student_entries[5].set(values[5])  # course
    
    def add_student(self):
        """Add new student to CSV file"""
        student_data = [entry.get() for entry in self.student_entries]
        
        if any(not data for data in student_data):
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            # Check for duplicate student ID
            for student in self.students_data:
                if student['student_id'] == student_data[0]:
                    messagebox.showerror("Error", "Student ID already exists!")
                    return
            
            # Create new student
            new_student = {
                'id': self.get_next_student_id(),
                'student_id': student_data[0],
                'name': student_data[1],
                'email': student_data[2],
                'phone': student_data[3],
                'address': student_data[4],
                'course': student_data[5],
                'enrollment_date': datetime.now().strftime("%Y-%m-%d")
            }
            
            self.students_data.append(new_student)
            self.write_students()
            
            messagebox.showinfo("Success", "✅ Student added successfully!")
            self.load_students()
            self.clear_student_form()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error adding student: {str(e)}")
    
    def update_student(self):
        """Update selected student"""
        if not self.selected_student_id:
            messagebox.showerror("Error", "Please select a student to update!")
            return
            
        student_data = [entry.get() for entry in self.student_entries]
        
        if any(not data for data in student_data):
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            # Find and update student
            for student in self.students_data:
                if student['student_id'] == self.selected_student_id:
                    student['name'] = student_data[1]
                    student['email'] = student_data[2]
                    student['phone'] = student_data[3]
                    student['address'] = student_data[4]
                    student['course'] = student_data[5]
                    break
            
            self.write_students()
            
            messagebox.showinfo("Success", "✅ Student updated successfully!")
            self.load_students()
            self.clear_student_form()
            self.selected_student_id = None
            
        except Exception as e:
            messagebox.showerror("Error", f"Error updating student: {str(e)}")
    
    def delete_student(self):
        """Delete selected student"""
        if not self.selected_student_id:
            messagebox.showerror("Error", "Please select a student to delete!")
            return
            
        result = messagebox.askyesno("Confirm Delete", 
                                     "Are you sure you want to delete this student?\nAll results will also be deleted!")
        if result:
            try:
                # Remove student
                self.students_data = [s for s in self.students_data if s['student_id'] != self.selected_student_id]
                
                # Remove associated results
                self.results_data = [r for r in self.results_data if r['student_id'] != self.selected_student_id]
                
                self.write_students()
                self.write_results()
                
                messagebox.showinfo("Success", "✅ Student deleted successfully!")
                self.load_students()
                self.clear_student_form()
                self.selected_student_id = None
                
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting student: {str(e)}")
    
    def clear_student_form(self):
        """Clear student form fields"""
        for entry in self.student_entries:
            if isinstance(entry, ttk.Combobox):
                entry.set('')
            else:
                entry.delete(0, END)
        self.selected_student_id = None
            
    def load_students(self):
        """Load students into treeview"""
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)
        
        for student in self.students_data:
            self.student_tree.insert("", "end", values=(
                student['id'],
                student['student_id'],
                student['name'],
                student['email'],
                student['phone'],
                student['course'],
                student['enrollment_date']
            ))
        
        # Update count label
        if hasattr(self, 'student_count_label'):
            self.update_student_count()
    
    def search_students(self):
        """Legacy search method - calls live search"""
        self.live_search_students()
    
    # ==================== RESULT MANAGEMENT ====================
    
    def show_results(self):
        """Show result management interface with update/delete buttons"""
        self.clear_main_content()
        
        # Refresh data
        self.courses_data = self.read_courses()
        self.students_data = self.read_students()
        self.results_data = self.read_results()
        
        header_frame = Frame(self.main_content, bg="white")
        header_frame.pack(fill="x", pady=10)
        Label(header_frame, text="Result Management", font=("Arial", 18, "bold"),
              bg="white", fg="#033054").pack()
        
        # Result Form
        form_frame = LabelFrame(self.main_content, text="Add New Result", 
                                font=("Arial", 12, "bold"), bg="white", fg="#033054")
        form_frame.pack(fill="x", padx=200, pady=10)
        
        # Form fields
        Label(form_frame, text="Student ID:", bg="white", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.result_student_combo = ttk.Combobox(form_frame, font=("Arial", 10), width=27)
        self.result_student_combo.grid(row=0, column=1, padx=10, pady=8)
        
        Label(form_frame, text="Course:", bg="white", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.result_course_combo = ttk.Combobox(form_frame, font=("Arial", 10), width=27)
        self.result_course_combo.grid(row=1, column=1, padx=10, pady=8)
        
        Label(form_frame, text="Subject:", bg="white", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=8, sticky="w")
        self.result_subject_entry = Entry(form_frame, width=30, font=("Arial", 10))
        self.result_subject_entry.grid(row=2, column=1, padx=10, pady=8)
        
        Label(form_frame, text="Marks:", bg="white", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=8, sticky="w")
        self.result_marks_entry = Entry(form_frame, width=30, font=("Arial", 10))
        self.result_marks_entry.grid(row=3, column=1, padx=10, pady=8)
        
        # Load student IDs
        student_ids = [student['student_id'] for student in self.students_data]
        self.result_student_combo['values'] = student_ids
        
        # Load courses
        courses = [course['course_name'] for course in self.courses_data]
        self.result_course_combo['values'] = courses
        
        # Buttons
        btn_frame = Frame(form_frame, bg="white")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        large_btn_style = {
            "font": ("Arial", 12, "bold"),
            "fg": "white",
            "cursor": "hand2",
            "relief": "raised",
            "bd": 3,
            "width": 15,
            "height": 2,
            "justify": "center"
        }
        
        Button(btn_frame, text="➕ ADD", command=self.add_result,
               bg="#4CAF50", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="✏️ UPDATE", command=self.update_result,
               bg="#FF9800", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="🗑️ DELETE", command=self.delete_result,
               bg="#f44336", **large_btn_style).pack(side="left", padx=8)
        
        Button(btn_frame, text="🔄 CLEAR", command=self.clear_result_form,
               bg="#607D8B", **large_btn_style).pack(side="left", padx=8)
        
        # Results List
        list_frame = LabelFrame(self.main_content, text="Results List (Click to Select)", 
                                font=("Arial", 12, "bold"), bg="white", fg="#033054")
        list_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        columns = ("ID", "Student ID", "Course", "Subject", "Marks", "Grade", "Exam Date")
        self.result_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.result_tree.heading(col, text=col)
            self.result_tree.column(col, width=120)
            
        # Bind select event
        self.result_tree.bind('<<TreeviewSelect>>', self.on_result_select)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.result_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_tree.configure(yscrollcommand=scrollbar.set)
        self.result_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Load results
        self.load_results()
    
    def on_result_select(self, event):
        """Handle result selection from treeview"""
        selected = self.result_tree.selection()
        if selected:
            item = self.result_tree.item(selected[0])
            values = item['values']
            self.selected_result_id = values[0]
            
            # Fill the form with selected result data
            self.result_student_combo.set(values[1])
            self.result_course_combo.set(values[2])
            self.result_subject_entry.delete(0, END)
            self.result_subject_entry.insert(0, values[3])
            self.result_marks_entry.delete(0, END)
            self.result_marks_entry.insert(0, values[4])
    
    def add_result(self):
        """Add new result to CSV file"""
        student_id = self.result_student_combo.get()
        course = self.result_course_combo.get()
        subject = self.result_subject_entry.get()
        marks = self.result_marks_entry.get()
        
        if not student_id or not course or not subject or not marks:
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            marks = float(marks)
            if marks < 0 or marks > 100:
                messagebox.showerror("Error", "Marks must be between 0 and 100!")
                return
                
            # Calculate grade
            if marks >= 75:
                grade = "A"
            elif marks >= 65:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            elif marks >= 35:
                grade = "S"
            else:
                grade = "F"
                
            # Create new result
            new_result = {
                'id': self.get_next_result_id(),
                'student_id': student_id,
                'course': course,
                'subject': subject,
                'marks': marks,
                'grade': grade,
                'exam_date': datetime.now().strftime("%Y-%m-%d")
            }
            
            self.results_data.append(new_result)
            self.write_results()
            
            messagebox.showinfo("Success", f"✅ Result added successfully!\nGrade: {grade}")
            self.load_results()
            self.clear_result_form()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid marks value!")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding result: {str(e)}")
    
    def update_result(self):
        """Update selected result"""
        if not self.selected_result_id:
            messagebox.showerror("Error", "Please select a result to update!")
            return
            
        student_id = self.result_student_combo.get()
        course = self.result_course_combo.get()
        subject = self.result_subject_entry.get()
        marks = self.result_marks_entry.get()
        
        if not student_id or not course or not subject or not marks:
            messagebox.showerror("Error", "All fields are required!")
            return
            
        try:
            marks = float(marks)
            if marks < 0 or marks > 100:
                messagebox.showerror("Error", "Marks must be between 0 and 100!")
                return
                
            # Calculate grade
            if marks >= 75:
                grade = "A"
            elif marks >= 65:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            elif marks >= 35:
                grade = "S"
            else:
                grade = "F"
                
            # Find and update result
            for result in self.results_data:
                if result['id'] == self.selected_result_id:
                    result['student_id'] = student_id
                    result['course'] = course
                    result['subject'] = subject
                    result['marks'] = marks
                    result['grade'] = grade
                    break
            
            self.write_results()
            
            messagebox.showinfo("Success", f"✅ Result updated successfully!\nNew Grade: {grade}")
            self.load_results()
            self.clear_result_form()
            self.selected_result_id = None
            
        except ValueError:
            messagebox.showerror("Error", "Invalid marks value!")
        except Exception as e:
            messagebox.showerror("Error", f"Error updating result: {str(e)}")
    
    def delete_result(self):
        """Delete selected result"""
        if not self.selected_result_id:
            messagebox.showerror("Error", "Please select a result to delete!")
            return
            
        result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this result?")
        if result:
            try:
                # Remove result
                self.results_data = [r for r in self.results_data if r['id'] != self.selected_result_id]
                self.write_results()
                
                messagebox.showinfo("Success", "✅ Result deleted successfully!")
                self.load_results()
                self.clear_result_form()
                self.selected_result_id = None
                
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting result: {str(e)}")
    
    def clear_result_form(self):
        """Clear result form fields"""
        self.result_student_combo.set('')
        self.result_course_combo.set('')
        self.result_subject_entry.delete(0, END)
        self.result_marks_entry.delete(0, END)
        self.selected_result_id = None
        
    def load_results(self):
        """Load results into treeview"""
        for item in self.result_tree.get_children():
            self.result_tree.delete(item)
            
        for result in self.results_data:
            self.result_tree.insert("", "end", values=(
                result['id'],
                result['student_id'],
                result['course'],
                result['subject'],
                result['marks'],
                result['grade'],
                result['exam_date']
            ))
    
    # ==================== VIEW RESULTS ====================
    
    def view_results(self):
        """View student results interface"""
        self.clear_main_content()
        
        header_frame = Frame(self.main_content, bg="white")
        header_frame.pack(fill="x", pady=10)
        Label(header_frame, text="View Student Results", font=("Arial", 18, "bold"),
              bg="white", fg="#033054").pack()
        
        search_frame = Frame(self.main_content, bg="white")
        search_frame.pack(fill="x", padx=400, pady=30)
        
        Label(search_frame, text="🔍 Enter Student ID:", bg="white", 
              font=("Arial", 12)).pack(side="left", padx=5)
        
        self.view_student_id = Entry(search_frame, font=("Arial", 12), width=20)
        self.view_student_id.pack(side="left", padx=5)
        
        Button(search_frame, text="View Results", 
               command=self.display_student_results,
               bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15).pack(side="left", padx=5)
        
        self.display_frame = Frame(self.main_content, bg="white")
        self.display_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
    def display_student_results(self):
        """Display results for a specific student"""
        for widget in self.display_frame.winfo_children():
            widget.destroy()
            
        student_id = self.view_student_id.get()
        
        if not student_id:
            messagebox.showerror("Error", "Please enter Student ID!")
            return
            
        try:
            # Refresh data
            self.students_data = self.read_students()
            self.results_data = self.read_results()
            
            # Find student
            student = None
            for s in self.students_data:
                if s['student_id'] == student_id:
                    student = s
                    break
            
            if not student:
                messagebox.showerror("Error", "Student not found!")
                return
                
            # Student Info Card
            info_frame = Frame(self.display_frame, bg="#e3f2fd", relief="solid", bd=2)
            info_frame.pack(fill="x", padx=100, pady=10)
            
            info_text = f"📋 Student ID: {student['student_id']} | Name: {student['name']} | Course: {student['course']}"
            Label(info_frame, text=info_text, bg="#e3f2fd", 
                  font=("Arial", 12, "bold")).pack(pady=10)
            
            # Get student's results
            student_results = [r for r in self.results_data if r['student_id'] == student_id]
            
            if not student_results:
                Label(self.display_frame, text="No results found for this student!",
                      font=("Arial", 14), bg="white", fg="red").pack(pady=20)
                return
                
            # Results Table
            table_frame = Frame(self.display_frame, bg="white")
            table_frame.pack(fill="both", expand=True, padx=100, pady=10)
            
            headers = ["Subject", "Marks", "Grade", "Exam Date"]
            for i, header in enumerate(headers):
                Label(table_frame, text=header, bg="#0b5377", fg="white",
                      font=("Arial", 11, "bold"), width=20).grid(row=0, column=i, padx=1, pady=1)
                
            total_marks = 0
            for row, result in enumerate(student_results, start=1):
                values = [result['subject'], result['marks'], result['grade'], result['exam_date']]
                for col, value in enumerate(values):
                    Label(table_frame, text=value, bg="white", 
                          font=("Arial", 10), width=20).grid(row=row, column=col, padx=1, pady=1)
                total_marks += result['marks']
                
            avg_marks = total_marks / len(student_results)
            status = "✅ PASS" if avg_marks >= 35 else "❌ FAIL"
            status_color = "#4CAF50" if avg_marks >= 35 else "#f44336"
            
            summary_frame = Frame(self.display_frame, bg="#fff3e0", relief="solid", bd=2)
            summary_frame.pack(fill="x", padx=100, pady=10)
            
            summary_text = f"📊 Total Subjects: {len(student_results)} | Average: {avg_marks:.2f}% | Status: {status}"
            Label(summary_frame, text=summary_text, bg="#fff3e0",
                  font=("Arial", 12, "bold"), fg=status_color).pack(pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying results: {str(e)}")
    
    def logout(self):
        """Logout function"""
        result = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if result:
            messagebox.showinfo("Logout", "👋 Logged out successfully!")
            
    def exit_app(self):
        """Exit application"""
        result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if result:
            self.root.quit()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()