import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from model.solarSystemExecute import SolarSystemExecuter
from model.queryExecuter import QueryExecuter
import tkinter.font as tkfont

class SolarSystemGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ask Solar System Info")
        self.root.geometry("1200x600")
        
        self.manager = SolarSystemExecuter()
        self.query_execute = QueryExecuter(self.manager)
        self.execute_GUI()
        self.get_planet_list()
    
    def execute_GUI(self):
        custom_font = tkfont.Font(family="Times New Roman", size=12, weight="bold", slant="italic")
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        title_label = ttk.Label(main_frame, text="Ask Solar System Info", 
                               font=("Times New Roman", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        query_frame = ttk.LabelFrame(main_frame, text="Quick Queries", padding="10")
        query_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        query_frame.columnconfigure(1, weight=1)
        
        # Planet selection
        ttk.Label(query_frame, text="Select Planet:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.planet_var = tk.StringVar()
        self.planet_all_check = ttk.Combobox(query_frame, textvariable=self.planet_var, 
                                        values=self.manager.get_all_planet_names())
        self.planet_all_check.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.planet_all_check.bind('<<ComboboxSelected>>', self.on_planet_select)
        button_frame = ttk.Frame(query_frame)
        button_frame.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        
        ttk.Button(button_frame, text="Everything", 
                  command=self.execute_show_everything).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(button_frame, text="Moon Count", 
                  command=self.execute_show_moon_count).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Moons", 
                  command=self.execute_show_moons).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Mass", 
                  command=self.execute_show_mass).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Distance", 
                  command=self.execute_show_distance).pack(side=tk.LEFT, padx=5)

       
        query_pre_frame = ttk.LabelFrame(main_frame, text="Feel free to ask a Question about planets", padding="10")
        query_pre_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        query_pre_frame.columnconfigure(0, weight=1)
        
        ttk.Label(query_pre_frame, text="pleaese dont forget to type below your question:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.query_var = tk.StringVar()
        query_entry = ttk.Entry(query_pre_frame, textvariable=self.query_var, width=80)
        query_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        query_entry.bind('<Return>', lambda e: self.process_each_query())
        
        ttk.Button(query_pre_frame, text="Ask", 
                  command=self.process_each_query).grid(row=1, column=1)
        
        init_example_frame = ttk.Frame(query_pre_frame)
        init_example_frame.grid(row=2, column=0, columnspan=15, sticky=tk.W, pady=(15, 0))
        
        ttk.Label(init_example_frame, text="check here for some samples:", font=custom_font).pack(side=tk.LEFT)
        
        examples = [
            "How many moons does Earth have?",
            "Is venus in the list of planets?",
            "Tell me everything about venus",
            "How massive is pluto?"
        ]
        
        for example in examples:
            example_btn = ttk.Button(init_example_frame, text=example, width=40,
                                   command=lambda e=example: self.load_example_query(e))
            example_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(row=4, column=0, columnspan=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        self.results_text = scrolledtext.ScrolledText(results_frame, height=15, width=80, wrap=tk.WORD)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Planet list section
        list_frame = ttk.LabelFrame(main_frame, text="All Planets", padding="10")
        list_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        list_frame.columnconfigure(0, weight=1)
        self.planet_list_var = tk.StringVar()

    
    def load_example_query(self, example):
        self.query_var.set(example)
        self.process_each_query()
    
    def process_each_query(self):
        query = self.query_var.get().strip()
        if not query:
            messagebox.execute_showwarning("Warning", "Please enter a question.")
            return
        
        # Process the query
        response = self.query_execute.process_query(query)
        
        # Display results
        self.clear_results()
        self.append_result(f"Question: {query}\n")
        self.append_result("=" * 50)
        self.append_result(response)
    
    def get_planet_list(self):
        self.planet_list_var.set(self.manager.get_all_planet_names())
    
    def clear_results(self):
        self.results_text.delete(1.0, tk.END)
    
    def append_result(self, text):
        self.results_text.insert(tk.END, text + "\n")
        self.results_text.see(tk.END)
    
    def get_selected_planet(self):
        return self.planet_var.get().strip()
    
    def validate_planet_selection(self):
        planet_name = self.get_selected_planet()
        if not planet_name:
            messagebox.execute_showwarning("Warning", "Please select a planet first.")
            return None
        return planet_name
    
    def on_planet_select(self, event):
        planet_name = self.get_selected_planet()
        if planet_name:
            self.execute_show_init_info(planet_name)
    
    def on_listbox_select(self, event):
        widget = event.widget
        if widget.curselection():
            index = widget.curselection()[0]
            planet_name = widget.get(index)
            self.planet_var.set(planet_name)
            self.execute_show_init_info(planet_name)
    
    def execute_show_init_info(self, planet_name):
        planet = self.manager.get_planet(planet_name)
        if planet:
            self.clear_results()
            self.append_result(f"Important information for {planet.name}:")
            self.append_result(f"  Mass: {planet.mass_kg:.2e} kg")
            self.append_result(f"  Distance from Sun: {planet.distance_from_sun_km:,.0f} km")
            self.append_result(f"  Number of moons: {len(planet.moons)}")
    
    def execute_show_everything(self):
        planet_name = self.validate_planet_selection()
        if not planet_name:
            return
        
        response = self.query_execute.check_everything_response(planet_name)
        self.clear_results()
        self.append_result(response)
    
    def execute_show_mass(self):
        planet_name = self.validate_planet_selection()
        if not planet_name:
            return
        
        response = self.query_execute.get_mass_response(planet_name)
        self.clear_results()
        self.append_result(response)
    
    def execute_show_distance(self):
        planet_name = self.validate_planet_selection()
        if not planet_name:
            return
        
        response = self.query_execute.get_distance_response(planet_name)
        self.clear_results()
        self.append_result(response)
    
    def execute_show_moons(self):
        planet_name = self.validate_planet_selection()
        if not planet_name:
            return
        
        response = self.query_execute.check_moons_response(planet_name)
        self.clear_results()
        self.append_result(response)
    
    def execute_show_moon_count(self):
        planet_name = self.validate_planet_selection()
        if not planet_name:
            return
        
        response = self.query_execute.get_moon_count_response(planet_name)
        self.clear_results()
        self.append_result(response)
    
    def check_planet_exists(self):
        planet_name = self.custom_planet_var.get().strip()
        if not planet_name:
            messagebox.execute_showwarning("Warning", "you need to Enter please a planet name.")
            return
        
        response = self.query_execute.check_existence_response(planet_name)
        self.clear_results()
        self.append_result(response)
