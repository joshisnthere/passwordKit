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