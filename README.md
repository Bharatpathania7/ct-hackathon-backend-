# 🚨 Smart Life Monitoring (SLM) - Backend

A **real-time emergency detection and response system** built using **FastAPI**.
This backend powers features like **voice-based distress detection, safety timer SOS, and multi-contact alert system**.

---

## 🔥 Features

* 🎤 **Voice-based Emergency Detection**
* ⏱ **Safety Timer with Auto SOS Trigger**
* 📩 **SMS Alerts via Twilio**
* 📞 **Auto Call Triggering**
* 📍 **Location-based Emergency Alerts**
* 👥 **Multi-contact Notification System**
* ⚡ **FastAPI High-performance backend**

---

## 🏗 Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python 3.10+
* **SMS & Calls:** Twilio API
* **Async Tasks:** asyncio
* **Server:** Uvicorn

---

## 📁 Project Structure

```
backend-fastapi/
│
├── app/
│   ├── main.py                # Entry point
│   ├── routes/
│   │   ├── detect.py         # Voice emergency detection API
│   │   └── timer.py          # Timer APIs
│   ├── services/
│   │   ├── timer_service.py  # Timer logic
│   │   └── twilio_service.py # SMS & call logic
│   └── models/
│       └── schemas.py        # Request/Response models
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (Run on Any Computer)

### ✅ 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd backend-fastapi
```

---

### ✅ 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Setup Environment Variables

Create a `.env` file:

```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

---

### ✅ 5. Run the Server

```bash
uvicorn app.main:app --reload
```

---

### 🌐 API Docs

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 API Endpoints

### 🔹 1. Start Timer

```http
POST /timer/start
```

**Body:**

```json
{
  "user_id": "bharat",
  "duration": 10,
  "contacts": ["+91XXXXXXXXXX"]
}
```

---

### 🔹 2. Cancel Timer

```http
POST /timer/cancel
```

```json
{
  "user_id": "bharat"
}
```

---

### 🔹 3. Emergency Detection

```http
POST /detect-emergency
```

```json
{
  "user_id": "bharat",
  "text": "help help",
  "volume": 0.9,
  "repeat_count": 3,
  "latitude": 30.7,
  "longitude": 76.7,
  "contacts": ["+91XXXXXXXXXX"],
  "force_emergency": true
}
```

---

## 🔥 How It Works

1. 🎤 Voice input analyzed for distress keywords
2. ⏱ Timer triggers SOS if not cancelled
3. 📍 Location is captured
4. 📩 SMS + 📞 Call sent to contacts
5. 🚨 Emergency flow executed

---

## 🧪 Testing

Use Swagger UI:

```
http://127.0.0.1:8000/docs
```

Or Postman with JSON requests.

---

## ⚠️ Notes

* Twilio trial accounts require **verified numbers**
* Ensure phone numbers are in **+91XXXXXXXXXX format**
* Backend uses **in-memory timers** (no DB)

---

## 🚀 Future Improvements

* 🔄 Database integration (MongoDB)
* 📱 Push notifications
* 🤖 ML-based voice classification
* 🌍 Live tracking dashboard

---

## 👨‍💻 Author

**Bharat Pathania**
Backend Developer | Startup Builder

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
