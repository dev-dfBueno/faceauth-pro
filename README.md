# 🚀 FaceAuth Pro

API de autenticação biométrica facial usando **DeepFace + ArcFace**, com foco em precisão e tolerância a variações como barba, cabelo e iluminação.

---

## 🔥 Sobre o projeto

O FaceAuth Pro é uma API desenvolvida em Python com FastAPI que permite:

* 📸 Cadastro facial a partir de documento (CNH/RG)
* 🤳 Verificação de identidade via selfie
* 🧠 Comparação usando modelo ArcFace
* ⚙️ Ajuste de tolerância para mudanças faciais

Ideal para **testes, estudos e protótipos de sistemas biométricos**.

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

## ▶️ Executando o projeto

```bash
uvicorn app:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

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
* Depende de qualidade da imagem

---

## 🛣️ Roadmap

* [ ] Integração com banco de dados real
* [ ] Autenticação JWT
* [ ] Interface web
* [ ] Deploy em cloud
* [ ] Logs e monitoramento

---

## 🛡️ Segurança

* Utilize `.env` para variáveis sensíveis
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

Projeto desenvolvido para fins de estudo, aprendizado e prototipagem de soluções com inteligência artificial.

---

## ⭐ Contribuição

Sinta-se livre para contribuir com melhorias, ideias ou correções!

---
