"""
Módulo para extraer texto de archivos PDF
"""
from PyPDF2 import PdfReader
from typing import Optional


class PDFExtractor:
    """Extrae texto de archivos PDF"""
    
    @staticmethod
    def extract_text(pdf_path: str, max_pages: Optional[int] = None) -> str:
        """
        Extrae texto de un archivo PDF
        
        Args:
            pdf_path: Ruta del archivo PDF
            max_pages: Número máximo de páginas a procesar (None = todas)
            
        Returns:
            Texto extraído del PDF
        """
        try:
            text = ""
            with open(pdf_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                num_pages = len(pdf_reader.pages)
                
                pages_to_read = min(num_pages, max_pages) if max_pages else num_pages
                
                for page_num in range(pages_to_read):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                    text += "\n"
            
            return text.strip()
        except Exception as e:
            raise Exception(f"Error al extraer texto del PDF: {str(e)}")
    
    @staticmethod
    def validate_pdf(pdf_path: str) -> bool:
        """
        Valida que el archivo sea un PDF válido
        
        Args:
            pdf_path: Ruta del archivo PDF
            
        Returns:
            True si es un PDF válido, False en caso contrario
        """
        try:
            with open(pdf_path, 'rb') as file:
                PdfReader(file)
            return True
        except:
            return False
