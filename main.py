
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 09:12:22 2026
@author: arthur.vantricht
"""

# Importing packages
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip
from mail_library import TEMPLATES
import json
with open("HNI_database.json", "r", encoding="utf-8") as f:
    HNI_data = json.load(f)["data"]
    

################### 
### MAIN WINDOW ###
###################

root = tk.Tk()
root.title("DIGI Support Tool")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
win_w = int(screen_w * 0.7)
win_h = int(screen_h * 0.75)
x = (screen_w - win_w) // 2
y = (screen_h - win_h) // 2
root.geometry(f"{win_w}x{win_h}+{x}+{y}")
root.minsize(int(screen_w * 0.4), int(screen_h * 0.4))

bg_color = "#f7f7f7"
input_bg = "#ffffff"
btn_color = "#4CAF50"
btn_clear = "#E53935"
btn_mail = "#1E88E5"
root.configure(bg=bg_color)

SEPARATOR = "=" * 44


########################
### HELPER FUNCTIONS ###
########################


def attach_editor_bindings(widget):

    
    ### ENTRY HISTORY (for ttk.Entry) ###

    if isinstance(widget, (tk.Entry, ttk.Entry)):
        undo_stack = []
        redo_stack = []

        def save_state(event=None):
            current = widget.get()

            if not undo_stack or undo_stack[-1] != current:
                undo_stack.append(current)

            # typing clears redo history
            redo_stack.clear()

        widget.bind("<KeyRelease>", save_state)


    ### ZOOM ###

    def zoom(event):
        current_font = widget.cget("font")

        try:
            font_name, font_size = current_font.rsplit(" ", 1)
            font_size = int(font_size)
        except Exception:
            font_name = "Arial"
            font_size = 10

        if event.delta > 0 or event.num == 4:
            font_size = min(font_size + 1, 30)
        else:
            font_size = max(font_size - 1, 6)

        widget.config(font=(font_name, font_size))
        return "break"

    widget.bind("<Control-MouseWheel>", zoom)
    widget.bind("<Control-Button-4>", zoom)
    widget.bind("<Control-Button-5>", zoom)


    ### CTRL + BACKSPACE ###

    def ctrl_backspace(event):

        if isinstance(widget, tk.Text):

            widget.delete("insert -1c wordstart", "insert")

        elif isinstance(widget, (tk.Entry, ttk.Entry)):

            cursor_pos = widget.index(tk.INSERT)
            text = widget.get()

            if cursor_pos == 0:
                return "break"

            left_text = text[:cursor_pos].rstrip()

            new_pos = left_text.rfind(" ") + 1

            widget.delete(new_pos, cursor_pos)
            widget.icursor(new_pos)

        return "break"

    widget.bind("<Control-BackSpace>", ctrl_backspace)

    
    ### CTRL + Z ###

    def ctrl_z(event):

        if isinstance(widget, tk.Text):

            try:
                widget.edit_undo()
            except Exception:
                pass

        elif isinstance(widget, (tk.Entry, ttk.Entry)):

            if len(undo_stack) > 1:

                current = undo_stack.pop()
                redo_stack.append(current)

                previous = undo_stack[-1]

                widget.delete(0, tk.END)
                widget.insert(0, previous)

        return "break"


    ### CTRL + Y ###

    def ctrl_y(event):

        if isinstance(widget, tk.Text):

            try:
                widget.edit_redo()
            except Exception:
                pass

        elif isinstance(widget, (tk.Entry, ttk.Entry)):

            if redo_stack:

                next_state = redo_stack.pop()

                undo_stack.append(next_state)

                widget.delete(0, tk.END)
                widget.insert(0, next_state)

        return "break"

    widget.bind("<Control-z>", ctrl_z)
    widget.bind("<Control-y>", ctrl_y)


def fill_placeholders(text):
    phone = affected_phone_no_entry.get().strip()
    if phone:
        text = text.replace("{phone_no}", phone)
    return text


def normalize_separators(text):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and all(c == "=" for c in stripped):
            new_lines.append(SEPARATOR)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def get_template(section, category, subcategory, language):
    key = f"{section}.{category}.{subcategory}.{language}"

    try:
        return TEMPLATES[key]
    except KeyError:
        raise KeyError(f"Template not found: {key}")
        


############
### TABS ###
############

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=(10, 0))

tab_main = tk.Frame(notebook, bg=bg_color)
tab_failed = tk.Frame(notebook, bg=bg_color)

notebook.add(tab_main, text="MAIN OBSERVATION")
notebook.add(tab_failed, text="FAILED CALL OBSERVATION")


### TAB 1 — Main Observation Generator ###

obs_left = tk.Frame(tab_main, bg=bg_color, padx=10, pady=10)
obs_left.pack(fill="both", expand=True)

fields = [
    ("Affected phone number:", "affected_phone_no_entry"),
    ("Port Done Date:", "port_done_date_entry"),
    ("ICCID:", "ICCID_entry"),
    ("Phone Model:", "phone_model_entry"),
    ("Connected To:", "conn_to_entry"),
    ("Parameters:", "params_entry"),
    ("VoLTE:", "VoLTE_entry")
]

entries = {}
entry_widgets_tab1 = []
for i, (label_text, var_name) in enumerate(fields):
    tk.Label(obs_left, text=label_text, bg=bg_color, font=("Arial", 10)).grid(
        row=i, column=0, sticky="e", padx=5, pady=3)
    entry = ttk.Entry(obs_left, font=("Arial", 10), width=35)
    entry.grid(row=i, column=1, sticky="ew", padx=5, pady=3)
    attach_editor_bindings(entry)
    obs_left.grid_columnconfigure(1, weight=1)
    entries[var_name] = entry
    entry_widgets_tab1.append(entry)

# Bind Enter to move to next field
for i, widget in enumerate(entry_widgets_tab1[:-1]):
    next_w = entry_widgets_tab1[i + 1]
    widget.bind("<Return>", lambda event, nw=next_w: nw.focus_set())
entry_widgets_tab1[-1].bind("<Return>", lambda event: additional_info_text.focus_set())
    


affected_phone_no_entry = entries["affected_phone_no_entry"]
port_done_date_entry = entries["port_done_date_entry"]
ICCID_entry = entries["ICCID_entry"]
phone_model_entry = entries["phone_model_entry"]
conn_to_entry = entries["conn_to_entry"]
params_entry = entries["params_entry"]
VoLTE_entry = entries["VoLTE_entry"]

tk.Label(obs_left, text="Additional Info:", bg=bg_color, font=("Arial", 10)).grid(
    row=len(fields), column=0, sticky="ne", padx=5, pady=3)
additional_info_text = tk.Text(obs_left, height=max(3, int(win_h * 0.008)), font=("Arial", 10), bg=input_bg, undo=True)
additional_info_text.grid(row=len(fields), column=0, columnspan=2, sticky="nsew", padx=5, pady=3)
obs_left.grid_rowconfigure(len(fields), weight=1)
obs_left.grid_rowconfigure(len(fields)+1, weight=0)
attach_editor_bindings(additional_info_text)

obs_button_frame = tk.Frame(obs_left, bg=bg_color)
obs_button_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=8)


def get_sim_version():
    iccid = ICCID_entry.get().strip()
    if len(iccid) >= 9:
        eighth = iccid[7]
        ninth = iccid[8]
        if eighth == "5":
            return "Idemia"
        elif eighth == "4" and ninth == "0":
            return "Idemia"
        elif eighth == "4" and ninth == "1":
            return "Valid"
    return None


def assemble_stk_template(base_key, language):
    sim_version = get_sim_version()
    header = TEMPLATES.get(f"{base_key}.header.{language}", "")
    idemia_instr = TEMPLATES.get(f"{base_key}.Idemia.{language}", "")
    valid_instr = TEMPLATES.get(f"{base_key}.Valid.{language}", "")

    if sim_version == "Idemia":
        parts = [header, idemia_instr]
    elif sim_version == "Valid":
        parts = [header, valid_instr]
    else:
        # Unknown or empty ICCID — include both
        parts = [header, idemia_instr, valid_instr]

    return "\n".join(part for part in parts if part)

    

def generate_observation(affected_phone_no, port_done_date, ICCID, phone_model, conn_to, params, additional_info, VoLTE_state):
    lines = ["Client info", ""]
    if affected_phone_no:
        if port_done_date:
            if affected_phone_no.startswith("0451" or "451"):
                port_part = f", joined: {port_done_date}"
            else:
                port_part = f", port done date: {port_done_date}"            
        else:
            port_part = ""
            
        
        if affected_phone_no.startswith("0"):
            lines.append(f"- Affected phone number: {affected_phone_no}{port_part}")
        else:
            lines.append(f"- Affected phone number: 0{affected_phone_no}{port_part}")
            
    
    if ICCID:
        lines.append(f"- ICCID: {ICCID}")
    if phone_model:
        lines.append(f"- Phone model: {phone_model}")
    if conn_to:
        def parse_plmn(value):
            first_part = value[:2]          
            second_part = value[3:]        
            reversed_first = first_part[::-1]   
            mcc = reversed_first + second_part[0]   
            mnc = second_part[1:][::-1]             
            return mcc, mnc
        def HNI_lookup(mcc, mnc, HNI_data):
            for entry in HNI_data:
                if entry["mcc"] == mcc and entry["mnc"] == mnc:
                    operator = (
                        entry.get("operator")
                        or entry.get("brand")
                        or entry.get("network")
                        or "Unknown operator"
                    )
        
                    country = entry.get("country", "Unknown country")
                    return operator, country
            return f" {conn_to} -> Unknown operator", "Unknown country"
    
        try:
            mcc, mnc = parse_plmn(conn_to)
            operator_name, country = HNI_lookup(mcc, mnc, HNI_data)
            lines.append(
                f"- Connected to: {operator_name} ({country})")
        except Exception:
            lines.append(f"- Connected to: {conn_to}")
    else: 
        pass
                   
    if params:
        lines.append(f"- Main params {params}")
    if VoLTE_state:
        lines.append(f"- VoLTE: {VoLTE_state}")
    if additional_info:
        lines.append("")
        lines.append(SEPARATOR)
        lines.append("")
        lines.append(additional_info)
    return "\n".join(lines)

def on_generate():
    affected_phone_no = affected_phone_no_entry.get().strip()
    port_done_date = port_done_date_entry.get().strip()
    ICCID = ICCID_entry.get().strip()
    phone_model = phone_model_entry.get().strip()
    conn_to = conn_to_entry.get().strip()
    params = params_entry.get().strip()
    additional_info = additional_info_text.get("1.0", tk.END).strip()
    additional_info = normalize_separators(additional_info)
    VoLTE_state = VoLTE_entry.get().strip()
    observation = generate_observation(
        affected_phone_no, port_done_date, ICCID,
        phone_model, conn_to, params, additional_info, VoLTE_state
    )
    pyperclip.copy(observation)
    messagebox.showinfo("Copied", "Observation copied to clipboard!")

def on_clear():
    for entry in entries.values():
        entry.delete(0, tk.END)
    additional_info_text.delete("1.0", tk.END)

tk.Button(obs_button_frame, text="Generate Observation", command=on_generate,
          bg=btn_color, fg="white", font=("Arial", 10, "bold"), padx=8, pady=3).grid(row=0, column=0, padx=8)
tk.Button(obs_button_frame, text="Clear Fields", command=on_clear,
          bg=btn_clear, fg="white", font=("Arial", 10, "bold"), padx=8, pady=3).grid(row=0, column=1, padx=8)

def on_ctrl_enter(event):
    current_tab = notebook.index(notebook.select())
    if current_tab == 0:
        on_generate()
    elif current_tab == 1:
        on_generate_failed()

root.bind('<Control-Return>', on_ctrl_enter)


def format_belgian_number(number):
    number = number.strip().replace(" ", "").replace("-", "")
    if number.startswith("00"):
        number = "+" + number[2:]
    elif number.startswith("0") and not number.startswith("00"):
        number = "+32" + number[1:]
    elif number.startswith("32") and not number.startswith("+"):
        number = "+" + number
    elif not number.startswith("+"):
        number = "+32" + number
    return number



### TAB 2 — Failed Call Observation Generator ###

failed_frame = tk.Frame(tab_failed, bg=bg_color, padx=10, pady=10)
failed_frame.pack(fill="both", expand=True)

failed_fields = [
    ("Call ID:", "call_id_entry"),
    ("A Number:", "a_number_entry"),
    ("B Number:", "b_number_entry"),
    ("Date:", "date_entry"),
    ("Status:", "status_entry")]



failed_entries = {}
entry_widgets_tab2 = []
for i, (label_text, var_name) in enumerate(failed_fields):
    tk.Label(failed_frame, text=label_text, bg=bg_color, font=("Arial", 10)).grid(
        row=i, column=0, sticky="e", padx=5, pady=3)
    entry = ttk.Entry(failed_frame, font=("Arial", 10), width=35)
    entry.grid(row=i, column=1, sticky="ew", padx=5, pady=3)
    attach_editor_bindings(entry)
    failed_frame.grid_columnconfigure(1, weight=1)
    failed_entries[var_name] = entry
    entry_widgets_tab2.append(entry)

# Bind Enter to move to next field
for i, widget in enumerate(entry_widgets_tab2[:-1]):
    next_w = entry_widgets_tab2[i + 1]
    widget.bind("<Return>", lambda event, nw=next_w: nw.focus_set())
entry_widgets_tab2[-1].bind("<Return>", lambda event: failed_additional_info_text.focus_set())



call_id_entry = failed_entries["call_id_entry"]
a_number_entry = failed_entries["a_number_entry"]
b_number_entry = failed_entries["b_number_entry"]
date_entry = failed_entries["date_entry"]
status_entry = failed_entries["status_entry"]




# Additional info for failed call
tk.Label(failed_frame, text="Additional Info:", bg=bg_color, font=("Arial", 10)).grid(
    row=len(failed_fields), column=0, sticky="ne", padx=5, pady=3)
failed_additional_info_text = tk.Text(failed_frame, height=max(3, int(win_h * 0.008)), font=("Arial", 10), bg=input_bg, undo=True)
failed_additional_info_text.grid(row=len(failed_fields), column=0, columnspan=2, sticky="nsew", padx=5, pady=3)
failed_frame.grid_rowconfigure(len(failed_fields), weight=1)
failed_frame.grid_rowconfigure(len(failed_fields)+1, weight=0)
attach_editor_bindings(failed_additional_info_text)

failed_button_frame = tk.Frame(failed_frame, bg=bg_color)
failed_button_frame.grid(row=len(failed_fields)+1, column=0, columnspan=2, pady=8)

def generate_failed_call_observation(call_id, a_number, b_number, date, status, additional_info_failed):
    lines = [f"Call ID: {call_id}"]
    if a_number:
        lines.append(f"- Ano: {format_belgian_number(a_number)}")
    if b_number:
        lines.append(f"- Bno: {format_belgian_number(b_number)}")
    if date:
        lines.append(f"- Date: {date}")
    if status:
        lines.append(f"- {status}")
    if additional_info_failed:
        lines.append("")
        lines.append(additional_info_failed)
    return "\n".join(lines)

def on_generate_failed():
    call_id = call_id_entry.get().strip()
    a_number = a_number_entry.get().strip()
    b_number = b_number_entry.get().strip()
    date = date_entry.get().strip()
    status = status_entry.get().strip()
    additional_info = failed_additional_info_text.get("1.0", tk.END).strip()
    additional_info = normalize_separators(additional_info)
    observation = generate_failed_call_observation(
        call_id, a_number, b_number, date, status, additional_info
    )
    pyperclip.copy(observation)
    messagebox.showinfo("Copied", "Failed call observation copied to clipboard!")

def on_clear_failed():
    for entry in failed_entries.values():
        entry.delete(0, tk.END)
    failed_additional_info_text.delete("1.0", tk.END)

tk.Button(failed_button_frame, text="Generate Observation", command=on_generate_failed,
          bg=btn_color, fg="white", font=("Arial", 10, "bold"), padx=8, pady=3).grid(row=0, column=0, padx=8)
tk.Button(failed_button_frame, text="Clear Fields", command=on_clear_failed,
          bg=btn_clear, fg="white", font=("Arial", 10, "bold"), padx=8, pady=3).grid(row=0, column=1, padx=8)


############################
### MAIL TEMPLATE BUTTON ###
############################

def open_mail_window():
    mail_win = tk.Toplevel(root)
    mail_win.title("Mail Template Selector")
    mw = int(screen_w * 0.75)
    mh = int(screen_h * 0.6)
    mx = (screen_w - mw) // 2
    my = (screen_h - mh) // 2
    mail_win.geometry(f"{mw}x{mh}+{mx}+{my}")
    mail_win.minsize(int(screen_w * 0.4), int(screen_h * 0.35))
    mail_win.configure(bg=bg_color)

    mail_paned = tk.PanedWindow(mail_win, orient="horizontal", sashrelief="flat", bg="#CCCCCC", sashwidth=2)
    mail_paned.pack(fill="both", expand=True, padx=10, pady=10)

    left_frame = tk.Frame(mail_paned, bg=bg_color)
    right_frame = tk.Frame(mail_paned, bg=bg_color)
    mail_paned.add(left_frame, stretch="always", minsize=int(screen_w * 0.2), width=int(mw * 0.63))
    mail_paned.add(right_frame, stretch="always", minsize=int(screen_w * 0.12), width=int(mw * 0.3))

    type_var = tk.StringVar()
    device_var = tk.StringVar()
    issue_var = tk.StringVar()
    language_var = tk.StringVar()

    type_combo = ttk.Combobox(left_frame, textvariable=type_var, state="readonly")
    type_combo.pack(pady=5)
    type_combo["values"] = ["Mobile", "Fix", "OnlineServices"]

    combo2 = ttk.Combobox(left_frame, textvariable=device_var, state="readonly")
    combo2.pack(pady=5)

    combo3 = ttk.Combobox(left_frame, textvariable=issue_var, state="readonly")
    combo3.pack(pady=5)

    combo4 = ttk.Combobox(left_frame, textvariable=language_var, state="readonly")
    combo4.pack(pady=5)

    left_button_frame = tk.Frame(left_frame, bg=bg_color)
    left_button_frame.pack(side="bottom", pady=(0, 5))

    output_box = tk.Text(left_frame, wrap="word", font=("Consolas", 10), undo=True)
    output_box.pack(expand=True, fill="both", pady=5)
    attach_editor_bindings(output_box)

    issue_options = {
        "Mobile": ["STK", "APN", "STK + APN", "Roaming"],
        "Fix": ["SlowSpeedsChangesMade", "PoorCoverageChangesMade", "TempOutageOngoing", "TempOutageSolved", "IssueSolved"],
        "OnlineServices": ["MailInSpam", "WeSentActivationMail", "ResetPassword", "WeSentChangeMailRequest"]
    }

    def update_type(event=None):
        type_val = type_var.get()
        device_var.set("")
        issue_var.set("")
        language_var.set("")
        combo2["values"] = []
        combo3["values"] = []
        combo4["values"] = []
        if type_val == "Mobile":
            combo2["values"] = ["Android", "iPhone", "IssueSolved"]
            combo2.config(state="readonly")
            combo3.config(state="disabled")
            combo4.config(state="disabled")
        elif type_val in ("Fix", "OnlineServices"):
            combo2["values"] = issue_options[type_val]
            combo2.config(state="readonly")
            combo3.config(state="disabled")
            combo4.config(state="disabled")

    type_combo.bind("<<ComboboxSelected>>", update_type)

    def update_combo2(event=None):
        type_val = type_var.get()
        issue_var.set("")
        language_var.set("")
        combo3["values"] = []
        combo4["values"] = []
    
        if type_val == "Mobile":
            selected = device_var.get()
            if selected == "IssueSolved":
                # Skip device selection — go straight to language in combo3
                combo3["values"] = ["English", "Dutch", "French"]
                combo3.config(state="readonly")
                combo4.config(state="disabled")
            else:
                combo3["values"] = issue_options["Mobile"]
                combo3.config(state="readonly")
                combo4.config(state="disabled")
    
        elif type_val in ("Fix", "OnlineServices"):
            combo3["values"] = ["English", "Dutch", "French"]
            combo3.config(state="readonly")
            combo4.config(state="disabled")

    combo2.bind("<<ComboboxSelected>>", update_combo2)


    def update_combo3(event=None):
        type_val = type_var.get()
        language_var.set("")
        combo4["values"] = []
    
        if type_val == "Mobile":
            device = device_var.get()
    
            if device == "IssueSolved":
                # combo3 holds language — trigger display directly
                display_template()
            else:
                issue = issue_var.get()
                if device and issue:
                    combo4["values"] = ["English", "Dutch", "French"]
                    combo4.config(state="readonly")
    
        elif type_val in ("Fix", "OnlineServices"):
            display_template()

    combo3.bind("<<ComboboxSelected>>", update_combo3)


    def update_combo4(event=None):
        display_template()

    combo4.bind("<<ComboboxSelected>>", update_combo4)

    def auto_select():
        phone = affected_phone_no_entry.get().strip()
        phone_model = phone_model_entry.get().strip().lower()
        if phone:
            type_var.set("Mobile")
            update_type()
            if "iphone" in phone_model or "apple" in phone_model:
                device_var.set("iPhone")
            else:
                device_var.set("Android")
            update_combo2()

    auto_select()

    tk.Label(right_frame, text="Notification Message", font=("Arial", 12, "bold"), bg=bg_color).pack(pady=(0, 5))

    notif_language_var = tk.StringVar()
    notif_language_combo = ttk.Combobox(right_frame, textvariable=notif_language_var, state="readonly", width=20)
    notif_language_combo["values"] = ["English", "Dutch", "French"]
    notif_language_combo.pack(pady=5)

    notif_button_frame = tk.Frame(right_frame, bg=bg_color)
    notif_button_frame.pack(side="bottom", pady=5)

    notif_output_box = tk.Text(right_frame, wrap="word", font=("Consolas", 10), undo=True)
    notif_output_box.pack(expand=True, fill="both", pady=5)
    attach_editor_bindings(notif_output_box)

    def sync_notif_language():
        type_val = type_var.get()
        device = device_var.get()
    
        if type_val == "Mobile" and device == "IssueSolved":
            language = issue_var.get()
        elif type_val == "Mobile":
            language = language_var.get()
        elif type_val in ("Fix", "OnlineServices"):
            language = issue_var.get()
        else:
            return
    
        if language in ["English", "Dutch", "French"]:
            notif_language_var.set(language)
            notif_output_box.delete("1.0", tk.END)
            notif_output_box.insert(tk.END, TEMPLATES.get(f"notification.{language}", ""))

    def display_template(event=None):
        type_val = type_var.get()
        device = device_var.get()
        issue = issue_var.get()
        language = language_var.get()
    
        # ── MOBILE — IssueSolved ──
        if type_val == "Mobile" and device == "IssueSolved":
            language = issue_var.get()  # combo3 holds language here
            if not language:
                return
            intro = TEMPLATES.get(f"intro.Mobile.General.{language}", "")
            middle = TEMPLATES.get(f"middle.Mobile.IssueSolved.{language}", "")
            outro = TEMPLATES.get(f"outro.General.{language}", "")
            full = "\n\n".join(part.strip() for part in [intro, middle, outro] if part.strip())
            full = fill_placeholders(full)
    
        # ── MOBILE — normal issues ──
        elif type_val == "Mobile":
            if not (device and issue and language):
                return
            general_intro = TEMPLATES.get(f"intro.Mobile.General.{language}", "")
            specific_intro = TEMPLATES.get(f"intro.Mobile.STK.{language}", "") if issue == "STK + APN" else TEMPLATES.get(f"intro.Mobile.{issue}.{language}", "")
        
            if issue in ("STK", "Roaming"):
                middle = assemble_stk_template(f"middle.Mobile.{device}.{issue}", language)
            elif issue == "STK + APN":
                stk_part = assemble_stk_template(f"middle.Mobile.{device}.STK", language)
                apn_part = TEMPLATES.get(f"middle.Mobile.{device}.APN.{language}", "")
                middle = "\n\n".join(part for part in [stk_part, apn_part] if part)
            else:
                middle = TEMPLATES.get(f"middle.Mobile.{device}.{issue}.{language}", "")
        
            outro = TEMPLATES.get(f"outro.General.{language}", "")
            full = "\n\n".join(part.strip() for part in [general_intro, specific_intro, middle, outro] if part.strip())
            full = fill_placeholders(full)
    
        # ── FIX + ONLINE SERVICES ──
        elif type_val in ("Fix", "OnlineServices"):
            issue = device_var.get()
            language = issue_var.get()
            if not (issue and language):
                return
            intro = TEMPLATES.get(f"intro.{type_val}.{language}", "")
            middle = TEMPLATES.get(f"middle.{type_val}.{issue}.{language}", "")
            outro = TEMPLATES.get(f"outro.General.{language}", "")
            full = "\n\n".join(part.strip() for part in [intro, middle, outro] if part.strip())
            full = fill_placeholders(full)
    
        else:
            return
    
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, full)
        sync_notif_language()


    def display_notification(event=None):
        language = notif_language_var.get()
        if language:
            notif_output_box.delete("1.0", tk.END)
            notif_output_box.insert(tk.END, TEMPLATES[f"notification.{language}"])

    notif_language_combo.bind("<<ComboboxSelected>>", display_notification)

    def copy_to_clipboard():
        template_text = output_box.get("1.0", tk.END).strip()
        if template_text:
            pyperclip.copy(template_text)
            copy_button.config(text="Copied!", bg="#90EE90")
            mail_win.after(2000, lambda: copy_button.config(text="Copy Template", bg=btn_color))
        else:
            messagebox.showwarning("Nothing to copy", "Please select all options first.")

    copy_button = tk.Button(left_button_frame, text="Copy Template", command=copy_to_clipboard,
                             bg=btn_color, fg="white", font=("Arial", 11, "bold"),
                             padx=10, pady=5, relief="flat", cursor="hand2")
    copy_button.pack(side="left", padx=10)

    def clear_all():
        type_var.set("")
        device_var.set("")
        issue_var.set("")
        language_var.set("")
        combo2["values"] = []
        combo3["values"] = []
        combo4["values"] = []
        combo2.config(state="readonly")
        combo3.config(state="disabled")
        combo4.config(state="disabled")
        output_box.delete("1.0", tk.END)

    clear_button = tk.Button(left_button_frame, text="Clear All", command=clear_all,
                              bg=btn_clear, fg="white", font=("Arial", 11, "bold"),
                              padx=10, pady=5, relief="flat", cursor="hand2")
    clear_button.pack(side="left", padx=10)

    def copy_notification():
        notif_text = notif_output_box.get("1.0", tk.END).strip()
        if notif_text:
            pyperclip.copy(notif_text)
            mail_win.destroy()
        else:
            messagebox.showwarning("Nothing to copy", "Please select a language first.")

    copy_notif_button = tk.Button(notif_button_frame, text="Copy Notification", command=copy_notification,
                                   bg=btn_color, fg="white", font=("Arial", 10, "bold"),
                                   padx=8, pady=3, relief="flat", cursor="hand2")
    copy_notif_button.pack(side="left", padx=5)

    def clear_notification():
        notif_language_var.set("")
        notif_output_box.delete("1.0", tk.END)

    clear_notif_button = tk.Button(notif_button_frame, text="Clear", command=clear_notification,
                                    bg=btn_clear, fg="white", font=("Arial", 10, "bold"),
                                    padx=8, pady=3, relief="flat", cursor="hand2")
    clear_notif_button.pack(side="left", padx=5)


# Mail Template button
mail_button = tk.Button(root, text="Open Mail Template Selector", command=open_mail_window,
                         bg=btn_mail, fg="white", font=("Arial", 11, "bold"),
                         padx=10, pady=6, relief="flat", cursor="hand2")
mail_button.pack(pady=(5, 10))

root.mainloop()







