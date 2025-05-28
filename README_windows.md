# Sistema RAG para ONGs - Instrucciones para Windows

Este documento detalla los pasos completos para instalar, configurar y ejecutar el sistema RAG (Retrieval-Augmented Generation) en un entorno Windows. Además, incluye soluciones a problemas reales encontrados durante el proceso.

---

## 🧱 Requisitos previos

- Python 3.12 (instalado desde https://www.python.org/)
- Git instalado
- PowerShell habilitado
- Visual Studio Code (opcional)
- Conexión a Internet estable

---

## 📁 1. Crear el proyecto

```powershell
cd C:\Users\TU_USUARIO\Desktop\Projects
mkdir RAG_ONGs
cd RAG_ONGs
```

---

## 🧪 2. Crear y activar entorno virtual

```powershell
python -m venv clean_env
.\clean_env\Scripts\Activate.ps1
```

---

## 📦 3. Instalar dependencias

Crea un archivo `requirements.txt` con lo siguiente (o usa el que viene en el repositorio si lo tienes):

```txt
langchain
langchain-community
langchain-core
sentence-transformers
faiss-cpu
transformers
huggingface-hub
pillow
pyyaml
langchain-huggingface
```

Instala las dependencias:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ⚠️ 4. Problemas resueltos

### 🔧 a. `langchain_huggingface` no encontrado
- Solución: Verifica que esté instalado y disponible en `sys.path`. Si no:
```powershell
pip install --force-reinstall langchain-huggingface
```

### 🔧 b. Error de codificación al leer `config.yml`
- Solución: abrir con `encoding='utf-8'`:
```python
with open("config.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)
```

### 🔧 c. `faiss` no encontrado
- Solución:
```powershell
pip install faiss-cpu
```

### 🔧 d. Problemas con entornos y rutas
- Solución: Verifica el entorno activo con `where python`
- Usa entornos virtuales con nombres únicos para evitar confusión

---

## ⚙️ 5. Ejecutar el sistema RAG

Una vez esté todo configurado:

```powershell
cd C:\Users\TU_USUARIO\Desktop\Projects\RAG_ONGs
.\clean_env\Scriptsctivate
python main.py
```

---

## ❓ Preguntas frecuentes

### ¿Cómo hago una pregunta al sistema?
Edita la entrada `"query"` en el archivo `config.yml` con tu pregunta antes de ejecutar `main.py`.

```yaml
query: "¿Qué ONG trabaja en sostenibilidad en América Latina?"
```

---

## 🪟 Consideraciones especiales para Windows

- Usa `encoding="utf-8"` al leer archivos.
- Algunos paquetes pueden fallar al desinstalar si están en uso. Reinicia PowerShell o la máquina si no puedes eliminarlos.
- Si los errores persisten, considera usar **WSL (Windows Subsystem for Linux)** para evitar problemas específicos de Windows.

---

## ✅ Verificación final

```powershell
python -c "from langchain_huggingface import HuggingFaceEmbeddings; print('✅ Funciona')"
```

---

¡Listo! Ya tienes el sistema RAG funcionando en Windows.