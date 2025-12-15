# 📚 Generador de Preguntas desde PDF

Una aplicación Python profesional que genera automáticamente **5 preguntas de opción múltiple** a partir de cualquier documento PDF, utilizando **Inteligencia Artificial (Google Gemini)**.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Functional-brightgreen)

## ✨ Características

- 📄 **Extracción de PDF**: Carga cualquier archivo PDF y extrae su contenido automáticamente
- 🤖 **Generación de IA**: Utiliza Google Gemini (API gratuita) para generar preguntas educativas
- 🎨 **Interfaz Profesional**: Diseño moderno con Tkinter, paleta azul + dorado
- ⚡ **Sin bloqueos**: Operaciones en segundo plano con threading
- 💾 **Registro automático**: Guarda las preguntas generadas en archivos de log
- 🎯 **Contexto temático**: Opción de especificar un tema para enfocar las preguntas
- ✅ **Explicaciones**: Cada pregunta incluye la respuesta correcta y explicación educativa

## 🚀 Inicio Rápido

### Requisitos
- Python 3.11+
- pip (gestor de paquetes)

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/generador-preguntas-pdf.git
cd generador-preguntas-pdf
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar API Key de Google**

Crea un archivo `.env` en la raíz del proyecto:
```env
GOOGLE_API_KEY=tu_clave_api_aqui
```

Obtén tu API key gratuita en: [Google AI Studio](https://makersuite.google.com/app/apikey)

4. **Ejecutar la aplicación**
```bash
python app_tkinter.py
```

## 📖 Cómo Usar

1. **Cargar PDF**: Haz clic en "Cargar PDF" y selecciona un archivo
2. **Especificar tema (opcional)**: Ingresa un contexto para enfocar las preguntas
3. **Generar preguntas**: Haz clic en "Generar Preguntas"
4. **Espera 15-30 segundos**: La IA generará las 5 preguntas
5. **Revisa los resultados**: Las preguntas aparecerán en el área de salida

## 📁 Estructura del Proyecto

```
.
├── app_tkinter.py              # Aplicación principal (Tkinter UI)
├── pdf_extractor.py            # Módulo para extraer texto de PDFs
├── question_generator.py       # Módulo para generar preguntas con IA
├── generar_informe.py          # Genera informe PDF de desarrollo
├── requirements.txt            # Dependencias Python
├── README.md                   # Documentación
├── .gitignore                  # Archivos a ignorar en Git
└── .env                        # Variables de entorno (NO subir a Git)
```

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|-----------|---------|----------|
| Python | 3.11+ | Lenguaje principal |
| Tkinter | Nativa | Interfaz gráfica |
| PyPDF2 | ≥3.0 | Extracción de PDFs |
| google-generativeai | Latest | IA (Google Gemini) |
| python-dotenv | 1.0+ | Gestión de variables de entorno |
| reportlab | Latest | Generación de PDFs |

## 📦 Dependencias

Todas las dependencias están listadas en `requirements.txt`:

```txt
PyPDF2>=3.0.0
python-dotenv>=1.0.0
google-generativeai>=0.3.0
reportlab>=4.0.0
openai>=1.0.0
anthropic>=0.7.0
requests>=2.31.0
```

## 🔐 Seguridad

- ⚠️ **NO comitear `.env`**: Este archivo contiene tu API key
- ✅ Las variables de entorno se cargan automáticamente
- ✅ El `.gitignore` ya está configurado para excluir archivos sensibles

## 📊 Ejemplo de Salida

```
📚 EVALUACIÓN GENERADA
================================================================================

❓ PREGUNTA 1
────────────────────────────────────────────────────────────────────────────
¿Cuál es la estructura principal de la célula eucariota?

  ○ A) Solo contiene mitocondrias
  ✓ B) Núcleo, citoplasma y membrana plasmática
  ○ C) No tiene membrana plasmática
  ○ D) Solo existe en bacterias

✅ Respuesta correcta: B
💡 Explicación: La célula eucariota se caracteriza por tener un núcleo definido...
================================================================================
```

## 🎨 Diseño Visual

La aplicación utiliza una paleta de colores profesional:

- **Azul Oscuro** (#1b2a4e) - Encabezado
- **Azul Claro** (#27407f) - Botones principales  
- **Dorado** (#d4af37) - Botón de generación
- **Blanco** (#ffffff) - Fondo principal
- **Gris Suave** (#f2f2f2) - Áreas de contenido

## 📝 Informe de Desarrollo

Se incluye un script que genera un informe PDF sobre el proceso de desarrollo:

```bash
python generar_informe.py
```

Esto crea `Informe_Desarrollo_Proyecto.pdf` con detalles sobre:
- Objetivos del proyecto
- Problemas iniciales y soluciones
- Tecnologías utilizadas
- Proceso de desarrollo en 6 fases
- Desafíos superados
- Lecciones aprendidas

## 🐛 Solución de Problemas

### Error: "No module named 'PyPDF2'"
```bash
pip install PyPDF2
```

### Error: "GOOGLE_API_KEY not configured"
- Verifica que el archivo `.env` exista en la carpeta principal
- Verifica que contenga: `GOOGLE_API_KEY=tu_clave`
- La clave debe ser válida desde [Google AI Studio](https://makersuite.google.com/app/apikey)

### La aplicación se congela
- Espera 15-30 segundos, la IA está procesando en segundo plano
- Asegúrate de tener conexión a Internet activa

### Error: "ModuleNotFoundError"
```bash
# Reinstalar todas las dependencias
pip install -r requirements.txt --upgrade
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios mayores:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 👤 Autor

Desarrollado como proyecto académico para demostrar:
- Integración de APIs de IA
- Desarrollo de interfaces gráficas con Python
- Procesamiento de documentos
- Mejores prácticas de programación Python

## 🎓 Aprendizajes Clave

Este proyecto demuestra:

✅ Integración con APIs externas (Google Gemini)  
✅ Procesamiento de archivos (PDFs)  
✅ Desarrollo de GUIs con Tkinter  
✅ Threading para operaciones no-bloqueantes  
✅ Gestión de variables de entorno  
✅ Manejo de errores robusto  
✅ Generación de reportes PDF  
✅ Buenas prácticas de Python  

## 📧 Contacto

Para preguntas o sugerencias sobre el proyecto, siéntete libre de abrir un [issue](../../issues).

---

**Hecho con ❤️ usando Python, Tkinter y Google Gemini API**

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)
