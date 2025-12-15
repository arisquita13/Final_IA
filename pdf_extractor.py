"""
Módulo para extraer texto de archivos PDF
"""

from PyPDF2 import PdfReader


class PDFExtractor:
    """Clase para extraer texto de archivos PDF"""
    
    def extract_text(self, pdf_path):
        """
        Extrae todo el texto de un archivo PDF
        
        Args:
            pdf_path: Ruta del archivo PDF
            
        Returns:
            String con todo el texto extraído
        """
        try:
            reader = PdfReader(pdf_path)
            text = ""
            
            for page in reader.pages:
                text += page.extract_text()
            
            return text
        
        except Exception as e:
            raise Exception(f"Error al extraer PDF: {str(e)}")
