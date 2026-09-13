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

        ctk.CTkLabel(gen_frame, text="Length").grid(row=0, column=0, padx=16, pady=16, sticky="w")
        self.length_slider = ctk.CTkSlider(gen_frame, from_=8, to=32, number_of_steps=24)
        self.length_slider.set(16)
        self.length_slider.grid(row=0, column=1, padx=16, sticky="ew")
        gen_frame.grid_columnconfigure(1, weight=1)

        self.use_upper = ctk.BooleanVar(value=True)
        self.use_digits = ctk.BooleanVar(value=True)
        self.use_symbols = ctk.BooleanVar(value=True)
        opts = ctk.CTkFrame(gen_frame, fg_color=PANEL)
        opts.grid(row=1, column=0, columnspan=2, padx=16, pady=(0, 10), sticky="w")
        ctk.CTkCheckBox(opts, text="Uppercase", variable=self.use_upper).pack(side="left", padx=(0, 10))
        ctk.CTkCheckBox(opts, text="Digits", variable=self.use_digits).pack(side="left", padx=(0, 10))
        ctk.CTkCheckBox(opts, text="Symbols", variable=self.use_symbols).pack(side="left")

        ctk.CTkButton(gen_frame, text="Generate", fg_color="#2a2a30",
                      command=self._generate).grid(row=2, column=0, padx=16, pady=16)

        self.generated_var = ctk.StringVar(value="")
        result_entry = ctk.CTkEntry(gen_frame, textvariable=self.generated_var, width=300)
        result_entry.grid(row=2, column=1, padx=16, sticky="w")
        ctk.CTkButton(gen_frame, text="Copy", width=70, fg_color="#2a2a30",
                      command=self._copy_generated).grid(row=2, column=2, padx=(0, 16))

    def _analyze(self):
        pw = self.password_var.get()
        if not pw:
            self.analysis_var.set("")
            return
        entropy, crack_time = logic.analyze(pw)
        self.analysis_var.set(f"Entropy: {entropy} bits\nEstimated crack time (offline attack): {crack_time}")