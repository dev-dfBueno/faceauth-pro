# 🚀 FaceAuth Pro

API de autentação biométrica facial utilizando **DeepFace + ArcFace**, com foco em precisão e tolerância a variações como barba, cabelo e iluminação.

---

## 🔥 Sobre o projeto

O **FaceAuth Pro** é uma API desenvolvida em Python com FastAPI que permite:

* 📸 Cadastro facial a partir de documento (CNH/RG)
* 🤳 Verificação de identidade via selfie
* 🧠 Comparação com modelo ArcFace
* ⚙️ Ajuste de tolerância para mudanças faciais

Ideal para **testes, estudos e prototipagem de sistemas biométricos**.

---

## 🧠 Tecnologias utilizadas

* Python
* FastAPI
* DeepFace (ArcFace)
* OpenCV
* RetinaFace
* Ngrok

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/faceauth-pro.git
cd faceauth-pro
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
NGROK_AUTH_TOKEN=seu_token_aqui
```

> ⚠️ Nunca compartilhe seu token publicamente

---

## ▶️ Executando localmente

```bash
uvicorn app:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

---

## ☁️ Rodando no Google Colab (modo teste)

Este projeto também pode ser executado no **Google Colab**, ideal para testes rápidos sem precisar instalar nada localmente.

### Passos básicos:

1. Abra o Google Colab
2. Cole o código do `app.py` em uma célula
3. Instale as dependências:

```python
!pip install deepface opencv-python fastapi uvicorn pyngrok nest_asyncio python-multipart
```

4. Configure seu token do ngrok:

```python
import os
os.environ["NGROK_AUTH_TOKEN"] = "seu_token_aqui"
```

5. Execute a API e use o link público gerado pelo ngrok

---

## 🌐 Endpoints

### 🔹 Status

```
GET /
```

---

### 🔹 Cadastro de usuário

```
POST /register/{user_id}
```

**Envio:**

* arquivo de imagem (`file`)
  ou
* URL da imagem (`url`)

---

### 🔹 Verificação facial

```
POST /verify/{user_id}
```

**Resposta:**

```json
{
  "match": true,
  "confidence": "91.32%"
}
```

---

## ⚠️ Limitações

* Banco de dados em memória (não persistente)
* Não recomendado para produção sem melhorias
* Depende da qualidade da imagem

---

## 🛣️ Roadmap

* [ ] Integração com banco de dados real
* [ ] Autenticação JWT
* [ ] Interface web
* [ ] Deploy em cloud
* [ ] Logs e monitoramento

---

## 🛡️ Segurança

* Utilize `.env` para dados sensíveis
* Nunca suba tokens no GitHub
* Adicione `.env` ao `.gitignore`

---

## 📌 Possíveis usos

* Login biométrico
* Validação de identidade
* Sistemas antifraude
* Aplicações de segurança

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo, aprendizado e prototipagem com inteligência artificial.

---

## ⭐ Contribuição

Sinta-se livre para contribuir com melhorias, ideias ou correções!
