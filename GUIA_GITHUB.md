# 📚 Guía para Subir a GitHub

Sigue estos pasos para subir tu proyecto a GitHub.

## Paso 1: Crear un repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Inicia sesión con tu cuenta (o crea una si no tienes)
3. Haz clic en **"+"** arriba a la derecha
4. Selecciona **"New repository"**
5. Nombre: `generador-preguntas-pdf`
6. Descripción: `Generador de preguntas desde PDF con IA (Google Gemini)`
7. Selecciona **Public** (para que otros puedan verlo)
8. NO selecciones "Initialize with README" (ya tenemos uno)
9. Haz clic en **"Create repository"**

GitHub te mostrará instrucciones. Usa las que aparecen en "...or push an existing repository from the command line"

## Paso 2: Inicializar Git en tu proyecto

```powershell
cd 'c:\Users\HP\Documents\INTELIGENCIA ARTIFICIAL 2\IA trabajo final'

# Inicializar repositorio git
git init

# Configurar tu nombre y email
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@example.com"

# Agregar todos los archivos
git add .

# Verificar qué se va a subir
git status
```

## Paso 3: Hacer el primer commit

```powershell
git commit -m "Initial commit: Generador de preguntas desde PDF con Tkinter e IA"
```

## Paso 4: Conectar con GitHub

Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub:

```powershell
# Agregegar la URL del repositorio remoto
git branch -M main
git remote add origin https://github.com/TU_USUARIO/generador-preguntas-pdf.git

# Subir los archivos
git push -u origin main
```

Si te pide autenticación:
- Usa tu **email de GitHub** como usuario
- Usa un **Personal Access Token** como contraseña (no tu contraseña de GitHub)

### Generar Personal Access Token

1. Ve a GitHub → Settings → Developer settings → Personal access tokens
2. Haz clic en "Generate new token"
3. Dale un nombre descriptivo
4. Selecciona permisos: `repo`
5. Copia el token y úsalo como contraseña

## Paso 5: Verificar que está en GitHub

1. Ve a `https://github.com/TU_USUARIO/generador-preguntas-pdf`
2. Deberías ver todos tus archivos

## ✅ Archivos que se subieron

Con el `.gitignore` que creamos, **SI se suben:**

```
✅ app_tkinter.py
✅ pdf_extractor.py
✅ question_generator.py
✅ generar_informe.py
✅ requirements.txt
✅ README.md
✅ README_GITHUB.md
✅ INICIO_RAPIDO.md
✅ .gitignore
✅ interfaces/
```

**NO se suben (correctamente ignorados):**

```
❌ .env (contiene tu API key)
❌ __pycache__/
❌ logs/ (archivos generados)
❌ *.pyc
❌ Informe_Desarrollo_Proyecto.pdf
❌ venv/
❌ .vscode/
```

## Actualizaciones Futuras

Cuando hagas cambios en tu código:

```powershell
# Ver qué cambió
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Descripción de cambios"

# Subir a GitHub
git push
```

## Ejemplo de Commits Buenos

```
✅ git commit -m "Add threaded PDF extraction"
✅ git commit -m "Update UI color scheme to blue and gold"
✅ git commit -m "Fix Google Gemini model deprecation"
❌ git commit -m "update" (muy vago)
❌ git commit -m "..." (no describible)
```

## Agregar una Licencia

Para agregar una licencia MIT (recomendado):

1. En GitHub, ve a tu repositorio
2. Haz clic en "Add file" → "Create new file"
3. Nombre: `LICENSE`
4. GitHub te sugiere seleccionar una licencia
5. Selecciona **MIT License**
6. Commit

## Agregar Badges (opcional)

En tu README, puedes agregar badges bonitos:

```markdown
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Functional-brightgreen)
```

## 🎉 ¡Listo!

Tu proyecto ya está en GitHub. Comparte el link: `https://github.com/TU_USUARIO/generador-preguntas-pdf`

---

**Tips extras:**

- 📌 Haz commits frecuentes con mensajes descriptivos
- 🔒 NUNCA comitees tu `.env` (GitHub te avisará)
- 📖 Mantén el README actualizado
- 🐛 Usa Issues para reportar bugs
- 🎯 Usa Releases para versiones importantes

