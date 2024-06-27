import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from rembg import remove
import io
import threading

class BackgroundRemoveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Remover Plano de Fundo")
        bg_color = "#2b2b2b"
        fg_color = "#ffffff"
        active_bg_color = "#808080"

        self.root.configure(bg=bg_color)

        main_frame = tk.Frame(root, bg=bg_color)
        main_frame.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(main_frame, width=300, height=300, bg=bg_color)
        self.canvas.pack()

        self.loading_label = tk.Label(
            main_frame, text="Selecione uma imagem", bg=bg_color, fg=fg_color)
        self.loading_label.pack()
        self.loading = False

        button_frame = tk.Frame(main_frame, bg=bg_color)
        button_frame.pack(pady=(10, 0))

        self.load_button = tk.Button(button_frame, text="Selecionar Imagem", command=self.load_image,
                                     bg=bg_color, fg=fg_color, activebackground=active_bg_color)
        self.load_button.pack(side=tk.LEFT, padx=(0, 10))

        self.process_button = tk.Button(button_frame, text="Remover Plano de Fundo",
                                        command=self.remove_background, bg=bg_color, fg=fg_color, activebackground=active_bg_color)
        self.process_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(main_frame, text="Salvar Resultado", command=self.save_result,
                                     bg=bg_color, fg=fg_color, activebackground=active_bg_color)
        self.save_button.pack(pady=(10, 0))

        self.image = None
        self.result = None

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.jpg *.png *.jpeg")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def remove_background(self):
        if self.image is not None:
            self.process_button.config(state=tk.DISABLED)
            self.start_loading_animation()
            thread = threading.Thread(target=self.process_image)
            thread.start()

    def start_loading_animation(self):
        self.loading = True
        loading_chars = ["|", "/", "-", "\\"]

        def update_label(i):
            if self.loading:
                self.loading_label.config(
                    text=f"Processando {loading_chars[i]}")
                i = (i + 1) % len(loading_chars)
                self.root.after(100, update_label, i)

        update_label(0)

    def stop_loading_animation(self):
        self.loading = False
        self.loading_label.config(text="Processamento concluído!")

    def process_image(self):
        with io.BytesIO() as input_bytes:
            self.image.save(input_bytes, format="PNG")
            input_data = input_bytes.getvalue()

        output_data = remove(input_data)
        output_image = Image.open(io.BytesIO(output_data))

        self.root.after(0, self.update_ui, output_image)

    def update_ui(self, output_image):
        self.result = output_image
        self.display_image(self.result)
        self.stop_loading_animation()
        self.process_button.config(state=tk.NORMAL)

    def save_result(self):
        if self.result is not None:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png", filetypes=[("Imagens PNG", "*.png")])
            if file_path:
                self.result.save(file_path)
                print(f"Resultado salvo em {file_path}")

    def display_image(self, image):
        if image is not None:
            image_width, image_height = image.size
            canvas_width = self.canvas.winfo_reqwidth()
            canvas_height = self.canvas.winfo_reqheight()

            if image_width > image_height:  # Horizontal Images
                new_width = canvas_width
                new_height = int(canvas_width * (image_height / image_width))
            else:  # Vertical or squared images
                new_height = canvas_height
                new_width = int(canvas_height * (image_width / image_height))

            image = image.resize((new_width, new_height))

            self.canvas.config(width=new_width, height=new_height)

            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.image = photo

# App init

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoveApp(root)
    root.mainloop()
