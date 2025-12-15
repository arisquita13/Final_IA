"""
Módulo para generar preguntas usando modelos de IA
Soporta: Google Gemini, OpenAI GPT, Anthropic Claude
"""
import os
from typing import List
from abc import ABC, abstractmethod
import json


class QuestionGenerator(ABC):
    """Clase base abstracta para generadores de preguntas"""
    
    @abstractmethod
    def generate_questions(self, text: str, num_questions: int = 5) -> List[dict]:
        """
        Genera preguntas basadas en el texto proporcionado
        
        Args:
            text: Texto del tema
            num_questions: Número de preguntas a generar
            
        Returns:
            Lista de diccionarios con preguntas y respuestas
        """
        pass


class GoogleQuestionGenerator(QuestionGenerator):
    """Generador de preguntas usando Google Gemini API"""
    
    def __init__(self, api_key: str = None):
        """
        Inicializa el generador con Google Gemini API
        
        Args:
            api_key: Clave de API de Google (o variable de entorno GOOGLE_API_KEY)
        """
        try:
            import google.generativeai as genai
            self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
        except ImportError:
            raise ImportError("Se requiere instalar google-generativeai: pip install google-generativeai")
    
    def generate_questions(self, text: str, num_questions: int = 5) -> List[dict]:
        """Genera preguntas usando Google Gemini"""
        try:
            prompt = f"""Basándote en el siguiente texto, genera exactamente {num_questions} preguntas de opción múltiple con 4 opciones de respuesta cada una.

TEXTO:
{text[:3000]}

Genera las preguntas en formato JSON con la siguiente estructura:
{{
    "questions": [
        {{
            "pregunta": "texto de la pregunta",
            "opciones": ["opción A", "opción B", "opción C", "opción D"],
            "respuesta_correcta": 0,
            "explicacion": "explicación de por qué es correcta"
        }}
    ]
}}

Asegúrate de que:
1. Las preguntas sean claras y específicas sobre el tema
2. Las opciones sean plausibles pero solo una sea correcta
3. La respuesta correcta esté indicada por el índice (0-3)
4. Las explicaciones sean educativas y cortas

Responde SOLO con el JSON, sin explicaciones adicionales."""

            response = self.model.generate_content(prompt)
            content = response.text
            
            # Limpiar el contenido si contiene bloques de código
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            # Remover caracteres de escape
            content = content.strip()
            
            data = json.loads(content)
            return data.get("questions", [])
        
        except Exception as e:
            raise Exception(f"Error al generar preguntas con Google Gemini: {str(e)}")


class OpenAIQuestionGenerator(QuestionGenerator):
    """Generador de preguntas usando OpenAI"""
    
    def __init__(self, api_key: str = None):
        """
        Inicializa el generador con la API de OpenAI
        
        Args:
            api_key: Clave de API de OpenAI (o variable de entorno OPENAI_API_KEY)
        """
        try:
            from openai import OpenAI
            self.api_key = api_key or os.getenv('OPENAI_API_KEY')
            self.client = OpenAI(api_key=self.api_key)
        except ImportError:
            raise ImportError("Se requiere instalar openai: pip install openai")
    
    def generate_questions(self, text: str, num_questions: int = 5) -> List[dict]:
        """Genera preguntas usando OpenAI GPT"""
        try:
            prompt = f"""Basándote en el siguiente texto, genera exactamente {num_questions} preguntas de opción múltiple con 4 opciones de respuesta cada una.

TEXTO:
{text[:3000]}

Genera las preguntas en formato JSON con la siguiente estructura:
{{
    "questions": [
        {{
            "pregunta": "texto de la pregunta",
            "opciones": ["opción A", "opción B", "opción C", "opción D"],
            "respuesta_correcta": 0,
            "explicacion": "explicación de por qué es correcta"
        }}
    ]
}}

Asegúrate de que:
1. Las preguntas sean claras y específicas sobre el tema
2. Las opciones sean plausibles pero solo una sea correcta
3. La respuesta correcta esté indicada por el índice (0-3)
4. Las explicaciones sean educativas"""

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un experto en educación que crea preguntas de evaluación de calidad."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            # Extraer el contenido JSON de la respuesta
            content = response.choices[0].message.content
            
            # Limpiar el contenido si contiene bloques de código
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            data = json.loads(content)
            return data.get("questions", [])
        
        except Exception as e:
            raise Exception(f"Error al generar preguntas con OpenAI: {str(e)}")


class AnthropicQuestionGenerator(QuestionGenerator):
    """Generador de preguntas usando Anthropic Claude"""
    
    def __init__(self, api_key: str = None):
        """
        Inicializa el generador con la API de Anthropic
        
        Args:
            api_key: Clave de API de Anthropic (o variable de entorno ANTHROPIC_API_KEY)
        """
        try:
            from anthropic import Anthropic
            self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
            self.client = Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError("Se requiere instalar anthropic: pip install anthropic")
    
    def generate_questions(self, text: str, num_questions: int = 5) -> List[dict]:
        """Genera preguntas usando Anthropic Claude"""
        try:
            prompt = f"""Basándote en el siguiente texto, genera exactamente {num_questions} preguntas de opción múltiple con 4 opciones de respuesta cada una.

TEXTO:
{text[:3000]}

Genera las preguntas en formato JSON con la siguiente estructura:
{{
    "questions": [
        {{
            "pregunta": "texto de la pregunta",
            "opciones": ["opción A", "opción B", "opción C", "opción D"],
            "respuesta_correcta": 0,
            "explicacion": "explicación de por qué es correcta"
        }}
    ]
}}

Asegúrate de que:
1. Las preguntas sean claras y específicas sobre el tema
2. Las opciones sean plausibles pero solo una sea correcta
3. La respuesta correcta esté indicada por el índice (0-3)
4. Las explicaciones sean educativas"""

            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                system="Eres un experto en educación que crea preguntas de evaluación de calidad.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            content = response.content[0].text
            
            # Limpiar el contenido si contiene bloques de código
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            data = json.loads(content)
            return data.get("questions", [])
        
        except Exception as e:
            raise Exception(f"Error al generar preguntas con Claude: {str(e)}")


def create_generator(provider: str = "google", api_key: str = None) -> QuestionGenerator:
    """
    Crea un generador de preguntas según el proveedor especificado
    
    Args:
        provider: "google", "openai" o "anthropic"
        api_key: Clave de API (opcional, se lee del entorno si no se proporciona)
        
    Returns:
        Instancia del generador de preguntas
    """
    provider = provider.lower()
    
    if provider == "google":
        return GoogleQuestionGenerator(api_key)
    elif provider == "openai":
        return OpenAIQuestionGenerator(api_key)
    elif provider == "anthropic":
        return AnthropicQuestionGenerator(api_key)
    else:
        raise ValueError(f"Proveedor no soportado: {provider}. Usa 'google', 'openai' o 'anthropic'")
