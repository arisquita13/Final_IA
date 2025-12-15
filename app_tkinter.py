"""
app_tkinter.py - Interfaz con Tkinter (Diseño profesional)

Generador de Preguntas desde PDF usando:
- Tkinter para la interfaz
- PyPDF2 para extraer PDFs
- Google Gemini AI para generar preguntas
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
from pathlib import Path
import os
from dotenv import load_dotenv

from pdf_extractor import PDFExtractor
from question_generator import create_generator


class AppTkinter:
    """Aplicación Tkinter para generar preguntas desde PDFs"""
    
    # Paleta de colores
    COLOR_AZUL_OSCURO = "#1b2a4e"
    COLOR_AZUL_CLARO = "#27407f"
    COLOR_DORADO = "#d4af37"
    COLOR_BLANCO = "#ffffff"
    COLOR_GRIS_SUAVE = "#f2f2f2"
    COLOR_TEXTO_OSCURO = "#1a1a1a"
    
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Generador de Preguntas desde PDF")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Configurar colores de la ventana
        self.root.configure(bg=self.COLOR_BLANCO)
        
        # Cargar variables de entorno
        load_dotenv()
        
        # Atributos
        self.pdf_ruta = None
        self.contenido_pdf = None
        
        # Crear interfaz
        self._crear_interfaz()
    
    def _crear_interfaz(self):
        """Crea la interfaz gráfica profesional"""
        
        # ========== ENCABEZADO ==========
        header_frame = tk.Frame(
            self.root,
            bg=self.COLOR_AZUL_OSCURO,
            height=80
        )
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        titulo = tk.Label(
            header_frame,
            text="📚 GENERADOR DE PREGUNTAS DESDE PDF",
            font=("Segoe UI", 20, "bold"),
            fg=self.COLOR_DORADO,
            bg=self.COLOR_AZUL_OSCURO,
            pady=15
        )
        titulo.pack()
        
        # ========== CONTENEDOR PRINCIPAL ==========
        main_frame = tk.Frame(self.root, bg=self.COLOR_BLANCO)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # ========== SECCIÓN 1: CARGAR PDF ==========
        pdf_section = tk.LabelFrame(
            main_frame,
            text="📁 CARGAR ARCHIVO PDF",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_AZUL_OSCURO,
            bg=self.COLOR_BLANCO,
            padx=15,
            pady=12,
            relief="solid",
            borderwidth=1
        )
        pdf_section.pack(fill="x", pady=(0, 15))
        
        # Frame para botón y estado
        pdf_content = tk.Frame(pdf_section, bg=self.COLOR_BLANCO)
        pdf_content.pack(fill="x")
        
        self.btn_cargar = tk.Button(
            pdf_content,
            text="📁 Cargar PDF",
            command=self.cargar_pdf,
            font=("Segoe UI", 11, "bold"),
            bg=self.COLOR_AZUL_CLARO,
            fg=self.COLOR_BLANCO,
            padx=25,
            pady=10,
            relief="flat",
            cursor="hand2",
            activebackground="#1a3466"
        )
        self.btn_cargar.pack(side="left", padx=5)
        
        self.label_pdf = tk.Label(
            pdf_content,
            text="❌ Ningún PDF cargado",
            font=("Segoe UI", 10),
            fg="#d32f2f",
            bg=self.COLOR_BLANCO
        )
        self.label_pdf.pack(side="left", padx=15)
        
        # ========== SECCIÓN 2: TEMA (OPCIONAL) ==========
        tema_section = tk.LabelFrame(
            main_frame,
            text="📝 TEMA O CONTEXTO (OPCIONAL)",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_AZUL_OSCURO,
            bg=self.COLOR_BLANCO,
            padx=15,
            pady=12,
            relief="solid",
            borderwidth=1
        )
        tema_section.pack(fill="x", pady=(0, 15))
        
        self.input_tema = tk.Entry(
            tema_section,
            font=("Segoe UI", 10),
            bg=self.COLOR_GRIS_SUAVE,
            fg=self.COLOR_TEXTO_OSCURO,
            relief="solid",
            borderwidth=1
        )
        self.input_tema.pack(fill="x", padx=5, pady=5)
        self.input_tema.insert(0, "Ej: Biología celular, Historia medieval, Matemáticas avanzada...")
        
        # Bind para limpiar placeholder
        def on_focus_in(event):
            if self.input_tema.get() == "Ej: Biología celular, Historia medieval, Matemáticas avanzada...":
                self.input_tema.delete(0, "end")
                self.input_tema.config(fg=self.COLOR_TEXTO_OSCURO)
        
        def on_focus_out(event):
            if self.input_tema.get() == "":
                self.input_tema.insert(0, "Ej: Biología celular, Historia medieval, Matemáticas avanzada...")
                self.input_tema.config(fg="#999999")
        
        self.input_tema.bind("<FocusIn>", on_focus_in)
        self.input_tema.bind("<FocusOut>", on_focus_out)
        self.input_tema.config(fg="#999999")
        
        # ========== SECCIÓN 3: BOTÓN GENERAR ==========
        button_frame = tk.Frame(main_frame, bg=self.COLOR_BLANCO)
        button_frame.pack(fill="x", pady=(0, 15))
        
        self.btn_generar = tk.Button(
            button_frame,
            text="🚀 GENERAR PREGUNTAS",
            command=self.generar_preguntas,
            font=("Segoe UI", 12, "bold"),
            bg=self.COLOR_DORADO,
            fg=self.COLOR_AZUL_OSCURO,
            padx=30,
            pady=12,
            relief="flat",
            cursor="hand2",
            activebackground="#c69c26",
            state="disabled"
        )
        self.btn_generar.pack()
        
        # ========== SECCIÓN 4: ÁREA DE SALIDA ==========
        output_section = tk.LabelFrame(
            main_frame,
            text="📖 PREGUNTAS GENERADAS",
            font=("Segoe UI", 11, "bold"),
            fg=self.COLOR_AZUL_OSCURO,
            bg=self.COLOR_BLANCO,
            padx=10,
            pady=10,
            relief="solid",
            borderwidth=1
        )
        output_section.pack(fill="both", expand=True)
        
        self.output = scrolledtext.ScrolledText(
            output_section,
            font=("Courier New", 9),
            height=20,
            width=100,
            bg=self.COLOR_GRIS_SUAVE,
            fg=self.COLOR_TEXTO_OSCURO,
            relief="solid",
            borderwidth=1,
            padx=10,
            pady=10,
            wrap="word"
        )
        self.output.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Mensaje inicial
        self.output.insert("1.0", 
            "📌 INSTRUCCIONES:\n\n"
            "1. Carga un archivo PDF haciendo clic en el botón 'Cargar PDF'\n"
            "2. (Opcional) Especifica un tema o contexto para enfocar las preguntas\n"
            "3. Haz clic en el botón 'Generar Preguntas'\n\n"
            "⏱️  El proceso toma aproximadamente 15-30 segundos...\n\n"
            "✨ La aplicación generará 5 preguntas de opción múltiple con explicaciones.\n"
        )
        self.output.config(state="disabled")
    
    def cargar_pdf(self):
        """Abre diálogo para cargar PDF"""
        ruta = filedialog.askopenfilename(
            title="Selecciona un PDF",
            filetypes=[("PDF", "*.pdf"), ("Todos", "*.*")]
        )
        
        if not ruta:
            return
        
        self.pdf_ruta = ruta
        
        # Mostrar mensaje de carga
        self._actualizar_output("🔄 Extrayendo PDF...", clear=True)
        self.btn_cargar.config(state="disabled")
        
        # Extraer PDF en thread separado
        thread = threading.Thread(target=self._extraer_pdf, args=(ruta,))
        thread.start()
    
    def _extraer_pdf(self, ruta):
        """Extrae contenido del PDF en thread"""
        try:
            extractor = PDFExtractor()
            contenido = extractor.extract_text(ruta)
            
            if not contenido or len(contenido.strip()) < 50:
                self._mostrar_error("❌ El PDF no contiene contenido válido")
                self.btn_cargar.config(state="normal")
                return
            
            # Limitar contenido
            if len(contenido) > 4000:
                contenido = contenido[:4000] + "\n[... truncado ...]"
            
            self.contenido_pdf = contenido
            
            # Actualizar UI
            self.root.after(0, self._pdf_cargado)
        
        except Exception as e:
            self._mostrar_error(f"❌ Error: {str(e)}")
            self.btn_cargar.config(state="normal")
    
    def _pdf_cargado(self):
        """Se ejecuta cuando se cargó el PDF"""
        self.label_pdf.config(
            text=f"✅ {Path(self.pdf_ruta).name}",
            fg="#388e3c"
        )
        self.btn_cargar.config(state="normal")
        self.btn_generar.config(state="normal")
        
        self._actualizar_output(
            f"✅ PDF CARGADO EXITOSAMENTE\n\n"
            f"📄 Archivo: {Path(self.pdf_ruta).name}\n"
            f"📊 Contenido: {len(self.contenido_pdf)} caracteres\n\n"
            f"¡Listo para generar preguntas!",
            clear=True
        )
    
    def generar_preguntas(self):
        """Genera 5 preguntas"""
        if not self.contenido_pdf:
            messagebox.showwarning("Error", "Carga un PDF primero")
            return
        
        tema = self.input_tema.get()
        
        # Deshabilitar botones
        self.btn_cargar.config(state="disabled")
        self.btn_generar.config(state="disabled")
        
        self._actualizar_output("⏳ Generando preguntas con IA...\n\n(Esto toma 15-30 segundos)", clear=True)
        
        # Generar en thread
        thread = threading.Thread(
            target=self._generar_preguntas_thread,
            args=(self.contenido_pdf, tema)
        )
        thread.start()
    
    def _generar_preguntas_thread(self, contenido, tema):
        """Genera preguntas en thread separado"""
        try:
            # Crear generador
            generator = create_generator(provider="google")
            
            # Generar preguntas
            preguntas = generator.generate_questions(
                text=contenido,
                num_questions=5
            )
            
            if not preguntas:
                self._mostrar_error("❌ No se generaron preguntas")
                return
            
            # Formatear preguntas
            texto = self._formatear_preguntas(preguntas)
            self.root.after(0, lambda: self._actualizar_output(texto, clear=True))
            
            # Guardar en logs
            self._guardar_log(preguntas)
        
        except Exception as e:
            self._mostrar_error(f"❌ Error: {str(e)}")
        
        finally:
            # Habilitar botones
            self.root.after(0, lambda: [
                self.btn_cargar.config(state="normal"),
                self.btn_generar.config(state="normal")
            ])
    
    def _formatear_preguntas(self, preguntas):
        """Formatea preguntas para mostrar con estilos elegantes"""
        texto = "📚 EVALUACIÓN GENERADA\n"
        texto += "=" * 80 + "\n\n"
        
        for idx, q in enumerate(preguntas, 1):
            texto += f"❓ PREGUNTA {idx}\n"
            texto += f"{'─' * 80}\n"
            texto += f"{q.get('pregunta', '')}\n\n"
            
            opciones = q.get('opciones', [])
            respuesta_idx = q.get('respuesta_correcta', 0)
            
            for opt_idx, opcion in enumerate(opciones):
                marcador = "✓" if opt_idx == respuesta_idx else "○"
                letra = chr(65 + opt_idx)
                texto += f"  {marcador} {letra}) {opcion}\n"
            
            texto += f"\n✅ Respuesta correcta: {chr(65 + respuesta_idx)}\n"
            texto += f"💡 Explicación: {q.get('explicacion', '')}\n"
            texto += "=" * 80 + "\n\n"
        
        return texto
    
    def _actualizar_output(self, texto, clear=False):
        """Actualiza el área de salida"""
        self.output.config(state="normal")
        if clear:
            self.output.delete("1.0", "end")
        self.output.insert("end", texto)
        self.output.config(state="disabled")
        self.output.see("end")
    
    def _mostrar_error(self, mensaje):
        """Muestra error en output y en messagebox"""
        self._actualizar_output(mensaje, clear=True)
        self.root.after(0, lambda: messagebox.showerror("Error", mensaje))
    
    def _guardar_log(self, preguntas):
        """Guarda resultado en logs/"""
        try:
            from datetime import datetime
            import json
            
            logs_dir = Path("logs")
            logs_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = logs_dir / f"preguntas_{timestamp}.txt"
            
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write(f"PDF: {self.pdf_ruta}\n")
                f.write(f"Fecha: {datetime.now()}\n")
                f.write("="*70 + "\n\n")
                
                for idx, q in enumerate(preguntas, 1):
                    f.write(f"PREGUNTA {idx}\n")
                    f.write(f"{q.get('pregunta', '')}\n\n")
                    
                    opciones = q.get('opciones', [])
                    for opt_idx, opcion in enumerate(opciones):
                        f.write(f"  {chr(65 + opt_idx)}) {opcion}\n")
                    
                    f.write(f"\nRespuesta: {chr(65 + q.get('respuesta_correcta', 0))}\n")
                    f.write(f"{q.get('explicacion', '')}\n\n")
                    f.write("-"*70 + "\n\n")
        
        except Exception as e:
            print(f"⚠️  No se pudo guardar log: {e}")


def main():
    """Punto de entrada"""
    root = tk.Tk()
    app = AppTkinter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
