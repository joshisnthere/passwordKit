"""
Password Toolkit

Two halves of one problem: analyze how strong a password actually is
(entropy bits and a rough crack-time estimate), and generate a genuinely
strong one with a length slider and charset controls.
"""

import customtkinter as ctk

import password_logic as logic

ctk.set_appearance_mode("dark")

BG = "#0d0c10"
PANEL = "#19181e"
ACCENT = "#e06c9f"


class PasswordToolkitApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Toolkit")
        self.geometry("640x620")
        self.configure(fg_color=BG)

        ctk.CTkLabel(self, text="Analyze", font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=ACCENT).pack(anchor="w", padx=24, pady=(24, 6))

        analyze_frame = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=12)
        analyze_frame.pack(fill="x", padx=24)
        self.password_var = ctk.StringVar()
        entry = ctk.CTkEntry(analyze_frame, textvariable=self.password_var, width=400, show="*")
        entry.pack(side="left", padx=16, pady=16)
        entry.bind("<KeyRelease>", lambda e: self._analyze())
        self.show_var = ctk.BooleanVar(value=False)
        ctk.CTkSwitch(analyze_frame, text="Show", variable=self.show_var,
                     command=lambda: entry.configure(show="" if self.show_var.get() else "*")).pack(side="left")

        self.analysis_var = ctk.StringVar(value="")
        ctk.CTkLabel(self, textvariable=self.analysis_var, text_color="#e6e6e6", justify="left",
                     wraplength=560).pack(anchor="w", padx=24, pady=(10, 30))

        ctk.CTkLabel(self, text="Generate", font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=ACCENT).pack(anchor="w", padx=24, pady=(0, 6))

        gen_frame = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=12)
        gen_frame.pack(fill="x", padx=24)