import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm
import os

file_name = ""
autosave_enabled = False

def update_status(event=None):
    """Updates the bottom status bar with word and character count"""
    text_content = content.get(1.0, "end-1c")
    char_count = len(text_content)
    word_count = len(text_content.split())
    
    current_file = os.path.basename(file_name) if file_name else "New Unsaved File"
    status_label.config(text=f" 📂 File: {current_file}  |  📝 Words: {word_count}  |  🔤 Chars: {char_count}")

def auto_save_loop():
    """Background loop that automatically saves the file every 5 seconds if enabled"""
    global file_name, autosave_enabled
    if autosave_enabled and file_name:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content.get(1.0, "end-1c"))
        # Temporarily flash the status bar to show it saved
        status_label.config(text=f" 💾 Auto-saved successfully! | {status_label.cget('text')}")
        window.after(1000, update_status) # return to normal status after 1 sec
        
    window.after(5000, auto_save_loop) # repeat every 5000ms (5 seconds)

def open_file():
    global file_name
    chosen_file = tfd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if chosen_file:
        file_name = chosen_file
        content.delete(1.0, "end")
        with open(file_name, "r", encoding="utf-8") as file:
            content.insert(1.0, file.read())
        update_status()

def save_as():
    global file_name
    chosen_file = tfd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if chosen_file:
        file_name = chosen_file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content.get(1.0, "end-1c"))
        update_status()
        tkm.showinfo("Saved", f"File successfully saved to:\n{file_name}")
    return file_name

def new_file():
    global file_name
    if content.get(1.0, "end-1c").strip(): # Check if there is text to lose
        answer = tkm.askyesnocancel("New File", "Do you want to save changes to your current text first?")
        if answer is True: # Yes, save it
            save()
        elif answer is False: # No, discard changes
            pass
        else: # Cancel
            return
            
    file_name = ""
    content.delete(1.0, "end")
    update_status()

def save():
    global file_name
    if not file_name:
        save_as()
    else:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content.get(1.0, "end-1c"))
        # Beautiful notification instead of a crashing window
        tkm.showinfo("File Saved", f"Changes saved instantly to:\n{file_name}")
        update_status()

def toggle_autosave():
    global autosave_enabled
    autosave_enabled = not autosave_enabled
    if autosave_enabled:
        tkm.showinfo("Auto-Save", "Auto-save is now ENABLED. It will back up your code every 5 seconds.")
    else:
        tkm.showinfo("Auto-Save", "Auto-save is now DISABLED.")

def help_win():
    # Using simple messagebox for help window to keep the app lightweight and stable
    tkm.showinfo("Help & Credits", "davinciXVII Notepad v2.0\n\nFeatures:\n- Cyberpunk Dark Theme\n- Live Word Counter\n- Auto-Save Engine\n\nThere is no further help, you are a master coder now!")

# Window Initialization
window = tk.Tk()
window.title("davinciXVII - CyberNote")
window.geometry("700x600")

# High-tech Dark Theme Colors
BG_COLOR = "#1e1e1e"     # Deep dark grey
TEXT_COLOR = "#f0f0f0"   # Clean off-white
CURSOR_COLOR = "#00ff66" # Neon hacker green
STATUS_BG = "#2d2d2d"    # Lighter grey for bars

# Load Images safely (uncomment and fix paths if you want to use your gifs)
try:
    new_file_pic = tk.PhotoImage(file="pics/new file.gif")
    open_pic = tk.PhotoImage(file="pics/open file.gif")
    save_pic = tk.PhotoImage(file="pics/save file.gif")
    has_images = True
except Exception:
    has_images = False

# Main Text Area (Packed to occupy maximum space, leaving room for status bar)
content = tk.Text(window, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=CURSOR_COLOR, font=("Consolas", 12), undo=True)
content.pack(fill="both", expand=True)

# Bind key releases to update word/char count live
content.bind("<KeyRelease>", update_status)

# Status Bar Creation
status_label = tk.Label(window, text=" 📂 File: New Unsaved File  |  📝 Words: 0  |  🔤 Chars: 0", 
                        bg=STATUS_BG, fg=TEXT_COLOR, anchor="w", font=("Segoe UI", 10))
status_label.pack(fill="x", side="bottom")

# Menu Interface Architecture
main_menu = tk.Menu(window)
file_menu = tk.Menu(main_menu, tearoff=0)
options_menu = tk.Menu(main_menu, tearoff=0)
help_menu = tk.Menu(main_menu, tearoff=0)

# Populating File Menu
if has_images:
    file_menu.add_command(label="New File", image=new_file_pic, compound="left", command=new_file)
    file_menu.add_command(label="Open File", image=open_pic, compound="left", command=open_file)
    file_menu.add_command(label="Save", image=save_pic, compound="left", command=save)
    file_menu.add_command(label="Save As...", image=save_pic, compound="left", command=save_as)
else:
    file_menu.add_command(label="New File", command=new_file)
    file_menu.add_command(label="Open File", command=open_file)
    file_menu.add_command(label="Save", command=save)
    file_menu.add_command(label="Save As...", command=save_as)

# Populating Options Menu (For the cool Auto-Save engine)
options_menu.add_checkbutton(label="Enable 5s Auto-Save", command=toggle_autosave)

# Populating Help Menu
help_menu.add_command(label="About & Help", command=help_win)

# Cascading Menus to the Main Window
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Options", menu=options_menu)
main_menu.add_cascade(label="Help", menu=help_menu)

window.configure(menu=main_menu)

# Start background processes
window.after(5000, auto_save_loop)

window.mainloop()
