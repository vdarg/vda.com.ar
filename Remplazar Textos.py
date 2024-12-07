import os
import tkinter as tk
from tkinter import messagebox

def replace_text_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = content.replace(old_text, new_text)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"Processed {file_path}")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"No se pudo encontrar el archivo {file_path}. Detalles: {e}")
    except PermissionError as e:
        messagebox.showerror("Error", f"Permiso denegado al abrir el archivo {file_path}. Detalles: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al procesar {file_path}: {e}")

def replace_text_in_folder(folder_path, old_text, new_text, file_extension='.html'):
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    replace_text_in_file(file_path, old_text, new_text)
    except Exception as e:
        messagebox.showerror("Error", f"Error al buscar archivos en {folder_path}: {e}")

def process_files():
    old_text = old_text_entry.get()
    new_text = new_text_entry.get()
    replace_text_in_folder(script_dir, old_text, new_text)

# Obtener la ruta de la carpeta en la que está el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Crear ventana tkinter
root = tk.Tk()
root.title("Reemplazar Texto en Archivos HTML")

# Etiquetas y entradas para old_text y new_text
tk.Label(root, text="Texto Antiguo:").pack()
old_text_entry = tk.Entry(root, width=50)
old_text_entry.pack()

tk.Label(root, text="Texto Nuevo:").pack()
new_text_entry = tk.Entry(root, width=50)
new_text_entry.pack()

# Botón para iniciar el proceso
tk.Button(root, text="Procesar Archivos", command=process_files).pack()

# Función principal de la ventana tkinter
root.mainloop()
