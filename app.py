# ==============================================================================
# 🚀 FaceAuth Pro - API Biométrica com ArcFace
# ==============================================================================
# 📌 Descrição:
# API de autenticação facial usando DeepFace (ArcFace) com FastAPI.
# Permite cadastro de usuário via imagem e verificação biométrica via selfie.
#
# ⚠️ IMPORTANTE:
# - NÃO coloque tokens diretamente no código (use .env)
# - Este projeto usa banco em memória (não persistente)
# - Ideal para estudos e protótipos
# ==============================================================================

# =========================
# 📦 IMPORTAÇÕES
# =========================
import os
import io
import cv2
import requests
import numpy as np
from PIL import Image
from typing import Dict, Any

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.datastructures import UploadFile

from deepface import DeepFace

# =========================
# 🔐 CONFIGURAÇÕES
# =========================
# Token do ngrok (caso vá usar túnel externo)
# Defina via variável de ambiente:
# export NGROK_AUTH_TOKEN=seu_token
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")

# =========================
# 🚀 INICIALIZAÇÃO DA API
# =========================
app = FastAPI(
    title="FaceAuth Pro",
    description="API de autentação facial com ArcFace",
    version="4.0.0"
)

# Libera acesso da API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Em produção, restringir domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# 🧠 "BANCO DE DADOS"
# =========================
# Simulação em memória (reset a cada execução)
fake_user_db: Dict[str, Any] = {}

# =========================
# 🧩 FUNÇÕES AUXILIARES
# =========================

def process_image_bytes(file_data: bytes):
    """
    Converte bytes de imagem para formato OpenCV (BGR)
    """
    try:
        # Abre imagem com PIL
        image = Image.open(io.BytesIO(file_data)).convert("RGB")

        # Converte para array numpy
        img_np = np.array(image)

        # Converte RGB -> BGR (padrão OpenCV)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        return img_bgr

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Imagem inválida ou corrompida"
        )


async def get_image_from_request(request: Request) -> bytes:
    """
    Extrai imagem enviada via:
    - Upload (file)
    - URL (url)
    """
    form = await request.form()

    file_input = form.get("file")
    url_input = form.get("url")

    # 📂 Caso seja upload de arquivo
    if isinstance(file_input, UploadFile):
        return await file_input.read()

    # 🌐 Caso seja URL
    if isinstance(url_input, str) and url_input.startswith("http"):
        try:
            response = requests.get(url_input, timeout=10)

            if response.status_code != 200:
                raise Exception()

            return response.content

        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Erro ao baixar imagem da URL"
            )

    # ❌ Nenhuma imagem enviada
    raise HTTPException(
        status_code=400,
        detail="Nenhuma imagem enviada (file ou url)"
    )

# =========================
# 🌐 ENDPOINTS
# =========================

@app.get("/")
def home():
    """
    Endpoint de status da API
    """
    return {
        "status": "online",
        "model": "ArcFace",
        "message": "FaceAuth Pro rodando 🚀"
    }


@app.post("/register/{user_id}")
async def register_user(user_id: str, request: Request):
    """
    📸 Cadastro biométrico

    Recebe uma imagem (documento ou rosto)
    e salva no "banco"
    """

    # 🔽 Extrai imagem da requisição
    content = await get_image_from_request(request)

    # 🔄 Processa imagem
    image = process_image_bytes(content)

    try:
        # 🔍 Detecta rosto usando RetinaFace
        DeepFace.extract_faces(
            image,
            detector_backend="retinaface",
            enforce_detection=True
        )

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Nenhum rosto detectado na imagem"
        )

    # 💾 Salva no banco (memória)
    fake_user_db[user_id] = image

    return {
        "success": True,
        "message": f"Usuário '{user_id}' cadastrado com sucesso"
    }


@app.post("/verify/{user_id}")
async def verify_user(user_id: str, request: Request):
    """
    🤳 Verificação biométrica

    Compara:
    - imagem cadastrada (documento)
    - selfie enviada
    """

    # 🔎 Verifica se usuário existe
    if user_id not in fake_user_db:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    # 🔽 Pega nova imagem (selfie)
    content = await get_image_from_request(request)
    selfie = process_image_bytes(content)

    # 📸 Imagem salva (documento)
    document = fake_user_db[user_id]

    try:
        # 🧠 Comparação com ArcFace
        result = DeepFace.verify(
            img1_path=document,
            img2_path=selfie,
            model_name="ArcFace",
            detector_backend="retinaface",
            enforce_detection=True
        )

        # 📊 Métricas retornadas pela IA
        distance = result["distance"]
        threshold = result["threshold"]

        # ⚙️ Ajuste de tolerância (barba, cabelo, etc.)
        threshold_adjusted = threshold + 0.15

        # ✅ Verifica se bate
        match = distance <= threshold_adjusted

        # 📈 Calcula confiança
        confidence = max(0, (1 - (distance / threshold_adjusted)) * 100)

        if match:
            return {
                "match": True,
                "user_id": user_id,
                "confidence": f"{confidence:.2f}%",
                "message": "Acesso permitido"
            }

        else:
            return JSONResponse(
                status_code=401,
                content={
                    "match": False,
                    "user_id": user_id,
                    "confidence": f"{confidence:.2f}%",
                    "message": "Rosto não confere"
                }
            )

    except Exception:
        return JSONResponse(
            status_code=400,
            content={
                "match": False,
                "message": "Não foi possível identificar o rosto"
            }
        )

# =========================
# ▶️ EXECUÇÃO LOCAL
# =========================
# Rodar com:
# uvicorn app:app --reload
# =========================

if __name__ == "__main__":
    print("🚀 Iniciando FaceAuth Pro...")
    print("👉 Acesse: http://localhost:8000")
