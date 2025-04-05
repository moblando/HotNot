import tkinter as tk
from tkinter import ttk
import webbrowser

class AppScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1080x980")
        self.root.title("QuizFlix - Interactive Learning App")
        
        # Create canvas for background
        self.bg_canvas = tk.Canvas(self.root, width=1080, height=980, bg="#f0f2f5", highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        
        # Create a main frame for content
        self.main_frame = tk.Frame(self.bg_canvas, bg="#f0f2f5")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=1000, height=900)
        
        # Custom font styles
        self.title_font = ("Segoe UI", 32, "bold")
        self.subtitle_font = ("Segoe UI", 16)
        self.button_font = ("Segoe UI", 14, "bold")
        
        # Header with logo and title
        self.header_frame = tk.Frame(self.main_frame, bg="#f0f2f5")
        self.header_frame.pack(pady=(0, 20))
        
        # App logo
        self.logo_label = tk.Label(
            self.header_frame,
            text="🎯",
            font=("Segoe UI", 48),
            bg="#f0f2f5"
        )
        self.logo_label.pack(side="left", padx=10)
        
        # Title and subtitle
        self.title_frame = tk.Frame(self.header_frame, bg="#f0f2f5")
        self.title_frame.pack(side="left")
        
        self.header_label = tk.Label(
            self.title_frame,
            text="QuizFlix",
            font=self.title_font,
            bg="#f0f2f5",
            fg="#2c3e50"
        )
        self.header_label.pack(anchor="w")
        
        self.subtitle_label = tk.Label(
            self.title_frame,
            text="Your Interactive Learning Platform",
            font=self.subtitle_font,
            bg="#f0f2f5",
            fg="#7f8c8d"
        )
        self.subtitle_label.pack(anchor="w")
        
        # Feature cards container - using uniform column weights
        self.features_frame = tk.Frame(self.main_frame, bg="#f0f2f5")
        self.features_frame.pack(pady=30)
        
        # Configure equal column weights
        for i in range(3):
            self.features_frame.grid_columnconfigure(i, weight=1, uniform="cols")
        
        # Create feature cards
        features = [
            {
                "icon": "📚",
                "title": "Multiple Genres",
                "desc": "Explore questions across various topics from science to pop culture"
            },
            {
                "icon": "🏆",
                "title": "Leaderboards",
                "desc": "Compete with friends and track your progress"
            },
            {
                "icon": "🔍",
                "title": "Detailed Explanations",
                "desc": "Learn from comprehensive answer explanations"
            }
        ]
        
        for i, feature in enumerate(features):
            card = tk.Frame(
                self.features_frame,
                bg="white",
                padx=15,
                pady=15,
                relief="groove",
                bd=0,
                highlightbackground="#dfe6e9",
                highlightthickness=1
            )
            card.grid(row=0, column=i, padx=10, sticky="nsew")
            
            # Feature icon
            icon = tk.Label(
                card,
                text=feature["icon"],
                font=("Segoe UI", 24),
                bg="white"
            )
            icon.pack(pady=(0, 10))
            
            # Feature title
            title = tk.Label(
                card,
                text=feature["title"],
                font=("Segoe UI", 16, "bold"),
                bg="white",
                fg="#2c3e50"
            )
            title.pack()
            
            # Feature description
            desc = tk.Label(
                card,
                text=feature["desc"],
                font=("Segoe UI", 12),
                bg="white",
                fg="#7f8c8d",
                wraplength=180
            )
            desc.pack(pady=(10, 0))
        
        # Description text
        self.desc_frame = tk.Frame(self.main_frame, bg="#f0f2f5")
        self.desc_frame.pack(fill="x", pady=30)
        
        self.description_label = tk.Label(
            self.desc_frame,
            text="QuizFlix transforms learning into an engaging experience with interactive quizzes,\n"
                 "personalized recommendations, and a vibrant community of learners.",
            font=("Segoe UI", 14),
            bg="#f0f2f5",
            fg="#34495e",
            justify="center"
        )
        self.description_label.pack()
        
        # Button frame
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f2f5")  # Changed back to match background
        self.button_frame.pack(pady=30)
        
        # GitHub button
        self.github_button = tk.Button(
            self.button_frame,
            text="Explore on GitHub",
            font=self.button_font,
            bg="#000000",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=30,
            pady=15,
            command=self.open_github
        )
        self.github_button.pack()
        
        # Hover effects
        self.github_button.bind("<Enter>", lambda e: self.github_button.config(bg="#757575", fg="#000000"))
        self.github_button.bind("<Leave>", lambda e: self.github_button.config(bg="#000000", fg="white"))
        
        # Create a black footer frame that spans the full width
        self.footer_frame = tk.Frame(self.bg_canvas, bg="#000000", height=60)
        self.footer_frame.pack(side="bottom", fill="x")
        
        # Footer content
        self.footer_label = tk.Label(
            self.footer_frame,
            text="© 2025 QuizFlix | All Rights Reserved",
            font=("Segoe UI", 10),
            bg="#000000",
            fg="#ffffff"  # White text for better contrast
        )
        self.footer_label.pack(pady=20)  # Centered vertically in the footer
        
        self.root.mainloop()

    def open_github(self):
        webbrowser.open("https://github.com/moblando/HotNot.git")

if __name__ == "__main__":
    AppScreen()
