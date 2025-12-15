"""
Generador de Informe PDF sobre el Desarrollo del Proyecto
Generador de Preguntas desde PDF con IA
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from datetime import datetime

# Configuración
PDF_FILENAME = "Informe_Desarrollo_Proyecto.pdf"
AZUL_OSCURO = colors.HexColor("#1b2a4e")
AZUL_CLARO = colors.HexColor("#27407f")
DORADO = colors.HexColor("#d4af37")

def crear_informe():
    """Crea el informe PDF sobre el desarrollo del proyecto"""
    
    # Crear documento
    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=letter,
        rightMargin=0.8*inch,
        leftMargin=0.8*inch,
        topMargin=1*inch,
        bottomMargin=0.8*inch
    )
    
    # Estilos personalizados
    styles = getSampleStyleSheet()
    
    titulo_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=AZUL_OSCURO,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    encabezado_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=DORADO,
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    subtitulo_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=AZUL_CLARO,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    cuerpo_style = ParagraphStyle(
        'BodyText',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=16
    )
    
    # Contenido del documento
    elementos = []
    
    # ========== PORTADA ==========
    elementos.append(Spacer(1, 1.5*inch))
    
    elementos.append(Paragraph(
        "📚 GENERADOR DE PREGUNTAS DESDE PDF",
        titulo_style
    ))
    
    elementos.append(Paragraph(
        "Con Inteligencia Artificial",
        encabezado_style
    ))
    
    elementos.append(Spacer(1, 0.3*inch))
    
    elementos.append(Paragraph(
        "INFORME DE DESARROLLO Y PROCESO",
        subtitulo_style
    ))
    
    elementos.append(Spacer(1, 0.5*inch))
    
    elementos.append(Paragraph(
        f"Fecha: {datetime.now().strftime('%d de %B de %Y')}",
        cuerpo_style
    ))
    
    elementos.append(PageBreak())
    
    # ========== ÍNDICE ==========
    elementos.append(Paragraph("ÍNDICE DE CONTENIDOS", encabezado_style))
    elementos.append(Spacer(1, 0.2*inch))
    
    indice_items = [
        "1. Introducción y Objetivo",
        "2. Problema Inicial",
        "3. Soluciones Implementadas",
        "4. Tecnologías Utilizadas",
        "5. Características Principales",
        "6. Proceso de Desarrollo",
        "7. Desafíos y Superación",
        "8. Conclusión"
    ]
    
    for item in indice_items:
        elementos.append(Paragraph(item, cuerpo_style))
        elementos.append(Spacer(1, 0.1*inch))
    
    elementos.append(PageBreak())
    
    # ========== INTRODUCCIÓN ==========
    elementos.append(Paragraph("1. INTRODUCCIÓN Y OBJETIVO", encabezado_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    texto_intro = """Este proyecto consiste en desarrollar una aplicación desktop que permite a los usuarios cargar archivos PDF y generar automáticamente un conjunto de 5 preguntas de opción múltiple basadas en el contenido del documento. La herramienta utiliza inteligencia artificial (Google Gemini API) para analizar y generar preguntas educativas con sus respectivas explicaciones."""
    
    elementos.append(Paragraph(texto_intro, cuerpo_style))
    elementos.append(Spacer(1, 0.15*inch))
    
    # ========== PROBLEMA INICIAL ==========
    elementos.append(Paragraph("2. PROBLEMA INICIAL", encabezado_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    texto_problema = """La aplicación inicial fue desarrollada con PyQt5 en Python, sin embargo, se encontraron varios obstáculos:<br/>
    <br/>
    <b>• Error de importación PyQt5.QtUiTools:</b> Windows no proporciona el módulo QUiLoader, lo que impedía cargar archivos .ui (diseño de interfaz).<br/>
    <br/>
    <b>• Limitaciones de costo:</b> Las APIs de OpenAI y Anthropic requieren pago (mínimo $5), lo cual no era viable para el proyecto.<br/>
    <br/>
    <b>• Complejidad innecesaria:</b> PyQt5 es robusto pero complejo para una aplicación simple, aumentando la curva de aprendizaje."""
    
    elementos.append(Paragraph(texto_problema, cuerpo_style))
    elementos.append(Spacer(1, 0.15*inch))
    
    # ========== SOLUCIONES ==========
    elementos.append(Paragraph("3. SOLUCIONES IMPLEMENTADAS", encabezado_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    texto_solucion = """<b>Solución 1: UI Programática en PyQt5</b><br/>
    En lugar de usar archivos .ui, se construyó la interfaz completamente en Python, evitando la dependencia de QUiLoader.<br/>
    <br/>
    <b>Solución 2: Integración con Google Gemini</b><br/>
    Se integró la API de Google Generative AI (Gemini), que ofrece un plan gratuito con cuota suficiente para desarrollo. Esto eliminó la barrera de costo.<br/>
    <br/>
    <b>Solución 3: Migración a Tkinter</b><br/>
    Se rediseñó completamente la aplicación usando Tkinter (nativa de Python, sin dependencias adicionales), simplificando significativamente el código y mejorando la mantenibilidad."""
    
    elementos.append(Paragraph(texto_solucion, cuerpo_style))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(PageBreak())
    
    # ========== TECNOLOGÍAS ==========
    elementos.append(Paragraph("4. TECNOLOGÍAS UTILIZADAS", encabezado_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    # Tabla de tecnologías
    tech_data = [
        ["Tecnología", "Versión", "Propósito"],
        ["Python", "3.11+", "Lenguaje de programación principal"],
        ["Tkinter", "Incluido", "Framework GUI nativo"],
        ["PyPDF2", "≥3.0", "Extracción de texto de PDFs"],
        ["Google Gemini API", "Latest", "IA para generar preguntas"],
        ["python-dotenv", "1.0+", "Gestión de variables de entorno"],
        ["reportlab", "Latest", "Generación de reportes PDF"]
    ]
    
    tech_table = Table(tech_data, colWidths=[2*inch, 1.5*inch, 2.5*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), AZUL_OSCURO),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
    ]))
    
    elementos.append(tech_table)
    elementos.append(Spacer(1, 0.15*inch))
    
    # ========== CARACTERÍSTICAS ==========
    elementos.append(Paragraph("5. CARACTERÍSTICAS PRINCIPALES", encabezado_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    features_text = """
    <b>✓ Carga de PDFs:</b> Interfaz intuitiva para seleccionar y cargar archivos PDF desde el sistema de archivos.<br/>
    <br/>
    <b>✓ Extracción de Contenido:</b> Extrae automáticamente todo el texto del PDF usando PyPDF2.<br/>
    <br/>
    <b>✓ Generación de Preguntas:</b> Utiliza Google Gemini para generar 5 preguntas de opción múltiple (A, B, C, D) con contenido educativo.<br/>
    <br/>
    <b>✓ Contexto Temático (Opcional):</b> El usuario puede especificar un tema para enfocar las preguntas generadas.<br/>
    <br/>
    <b>✓ Explicaciones Detalladas:</b> Cada pregunta incluye la respuesta correcta y una explicación educativa.<br/>
    <br/>
    <b>✓ Interfaz Profesional:</b> Diseño moderno con paleta de colores azul + dorado, responsive y fácil de usar.<br/>
    <br/>
    <b>✓ Operación No-Bloqueante:</b> Utiliza threading para que la UI no se congele durante la extracción y generación.<br/>
    <br/>
    <b>✓ Registro de Resultados:</b> Guarda automáticamente las preguntas generadas en archivos de log.
    """
    
    elementos.append(Paragraph(features_text, cuerpo_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    elementos.append(PageBreak())
    
    # ========== CONCLUSIÓN ==========
    elementos.append(Paragraph("6. CONCLUSIÓN", encabezado_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    conclusion_text = """Este proyecto demuestra la importancia de la adaptabilidad en el desarrollo de software. Lo que comenzó como una aplicación con PyQt5 y APIs pagas, evolucionó a una solución más elegante, simple y accesible usando Tkinter y la API gratuita de Google Gemini.<br/>
    <br/>
    <b>Lecciones aprendidas:</b><br/>
    • Evaluación de dependencias y limitaciones antes de comprometerse<br/>
    • Exploración de alternativas gratuitas y eficientes<br/>
    • Simplicidad en el diseño produce mejores resultados<br/>
    • Diseño profesional no requiere frameworks pesados<br/>
    • Threading es esencial para buena experiencia de usuario<br/>
    <br/>
    El producto final es una aplicación funcional, profesional, mantenible y completamente gratuita.
    """
    
    elementos.append(Paragraph(conclusion_text, cuerpo_style))
    
    elementos.append(Spacer(1, 0.3*inch))
    elementos.append(Paragraph("─" * 80, cuerpo_style))
    elementos.append(Spacer(1, 0.1*inch))
    
    firma_text = f"""Desarrollado en: Python 3.11+<br/>
    Fecha: {datetime.now().strftime('%d de %B de %Y')}<br/>
    Arquitectura: Tkinter + PyPDF2 + Google Gemini API<br/>
    Estado: Completado y Funcional ✓"""
    
    elementos.append(Paragraph(firma_text, cuerpo_style))
    
    # Construir el PDF
    doc.build(elementos)
    
    print(f"✅ PDF generado: {PDF_FILENAME}")


if __name__ == "__main__":
    crear_informe()
