import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
import os

class SteganoCrypt:
    def __init__(self, master):
        self.master = master
        self.master.title("SteganoCrypt - Image Steganography")
        self.master.geometry("800x600")
        self.master.configure(bg="#1E1E1E")

        self.image_path = None

        # UI Styling
        self.style = ttk.Style()
        self.style.configure('TButton', padding=10, font=('Arial', 11, 'bold'))
        self.create_ui()

    def create_ui(self):
        frame = ttk.Frame(self.master, padding=10)
        frame.pack(expand=True, fill=tk.BOTH)

        title_label = tk.Label(frame, text="SteganoCrypt - Secure Image Steganography", 
                               font=("Arial", 18, "bold"), bg="#1E1E1E", fg="white")
        title_label.pack(pady=10)

        select_btn = ttk.Button(frame, text="Select Image", command=self.load_image)
        select_btn.pack(pady=5)

        self.message_entry = tk.Text(frame, height=4, width=50)
        self.message_entry.pack(pady=5)

        encode_btn = ttk.Button(frame, text="Encode Message", command=self.encode_message)
        encode_btn.pack(pady=5)

        decode_btn = ttk.Button(frame, text="Decode Message", command=self.decode_message)
        decode_btn.pack(pady=5)

        self.output_text = tk.Text(frame, height=4, width=50, state=tk.DISABLED)
        self.output_text.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.bmp")])
        if self.image_path:
            messagebox.showinfo("Success", f"Loaded: {os.path.basename(self.image_path)}")

    def encode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected!")
            return
        
        msg = self.message_entry.get("1.0", tk.END).strip()
        if not msg:
            messagebox.showerror("Error", "Enter a message to encode!")
            return

        img = cv2.imread(self.image_path)
        max_bytes = (img.shape[0] * img.shape[1] * 3) // 8

        if len(msg) > max_bytes - 1:
            messagebox.showerror("Error", "Message too long for this image!")
            return

        msg_length = len(msg)
        img[0, 0, 0] = msg_length

        i, j, k = 1, 0, 0
        for char in msg:
            if i >= img.shape[0] or j >= img.shape[1]:
                messagebox.showerror("Error", "Image is too small!")
                return
            img[i, j, k] = ord(char)
            j += 1
            if j >= img.shape[1]:
                j = 0
                i += 1
            k = (k + 1) % 3

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            cv2.imwrite(save_path, img)
            messagebox.showinfo("Success", "Message encoded successfully!")

    def decode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected!")
            return

        img = cv2.imread(self.image_path)
        msg_length = img[0, 0, 0]

        message = ""
        i, j, k = 1, 0, 0
        for _ in range(msg_length):
            if i >= img.shape[0] or j >= img.shape[1]:
                messagebox.showerror("Error", "Error in decoding!")
                return
            message += chr(img[i, j, k])
            j += 1
            if j >= img.shape[1]:
                j = 0
                i += 1
            k = (k + 1) % 3

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganoCrypt(root)
    root.mainloop()
