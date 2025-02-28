import tkinter as tk
from tkinter import filedialog, messagebox
from caesar_ciper import encrypt, decrypt
from file_operations import process_file
from logger import log_operation
from visualization import plot_frequency

# ---------- Utility Functions ---------- #
def validate_shift(shift_value):
    """Validate shift input and ensure it's an integer."""
    if not shift_value.isdigit():
        messagebox.showerror("Invalid Input", "Shift must be a positive integer.")
        return None
    return int(shift_value) % 26

def load_text():
    """Load text from a file into the input text area."""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        text = process_file(file_path)
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, text)

def save_output():
    """Save the output text to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(output_text.get("1.0", tk.END).strip())
        messagebox.showinfo("Saved", "Output saved successfully!")

# ---------- Button Handlers ---------- #
def handle_encrypt():
    shift = validate_shift(shift_entry.get())
    if shift is None:
        return
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Enter text to encrypt.")
        return
    result = encrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    log_operation("encrypt", shift, text, result)

def handle_decrypt():
    shift = validate_shift(shift_entry.get())
    if shift is None:
        return
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Enter text to decrypt.")
        return
    result = decrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    log_operation("decrypt", shift, text, result)

def handle_visualize():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Enter text to visualize.")
        return
    plot_frequency(text)

# ---------- GUI Setup ---------- #
def run_gui():
    global shift_entry, input_text, output_text

    window = tk.Tk()
    window.title("🔒 Caesar Cipher Tool")
    window.geometry("700x600")
    window.configure(bg="#f0f4f8")

    # ---------- Menu Bar ---------- #
    menubar = tk.Menu(window)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Load Text", command=load_text)
    file_menu.add_command(label="Save Output", command=save_output)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    window.config(menu=menubar)

    # ---------- Title ---------- #
    tk.Label(window, text="Caesar Cipher Encryption & Decryption", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#333")\
        .pack(pady=15)

    # ---------- Shift Input ---------- #
    shift_frame = tk.Frame(window, bg="#f0f4f8")
    shift_frame.pack(pady=10)
    tk.Label(shift_frame, text="🔑 Shift (0-25):", font=("Arial", 12), bg="#f0f4f8").grid(row=0, column=0, padx=5)
    shift_entry = tk.Entry(shift_frame, width=10, font=("Arial", 12))
    shift_entry.grid(row=0, column=1, padx=5)

    # ---------- Input Text ---------- #
    tk.Label(window, text="📝 Input Text:", font=("Arial", 12, "bold"), bg="#f0f4f8").pack(pady=5)
    input_text = tk.Text(window, height=10, width=70, font=("Arial", 11), wrap=tk.WORD, bd=2, relief="groove")
    input_text.pack(pady=5)

    # ---------- Action Buttons ---------- #
    button_frame = tk.Frame(window, bg="#f0f4f8")
    button_frame.pack(pady=15)
    tk.Button(button_frame, text="🔐 Encrypt", font=("Arial", 11, "bold"), bg="#4caf50", fg="white", width=15, command=handle_encrypt)\
        .grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="🔓 Decrypt", font=("Arial", 11, "bold"), bg="#2196f3", fg="white", width=15, command=handle_decrypt)\
        .grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="📊 Visualize Frequency", font=("Arial", 11, "bold"), bg="#ff9800", fg="white", width=20, command=handle_visualize)\
        .grid(row=0, column=2, padx=10)

    # ---------- Output Text ---------- #
    tk.Label(window, text="📄 Output Text:", font=("Arial", 12, "bold"), bg="#f0f4f8").pack(pady=5)
    output_text = tk.Text(window, height=10, width=70, font=("Arial", 11), wrap=tk.WORD, bd=2, relief="groove")
    output_text.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    run_gui()
