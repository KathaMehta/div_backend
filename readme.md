
# 🧠 Diversity IQ – Fairness Analysis Tool

Diversity IQ is an AI-powered tool that helps detect bias in your dataset before model training. It analyzes categorical features like gender or ethnicity, flags imbalance, and offers suggestions to improve fairness — helping you build ethical AI from the ground up.

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

---

### 📁 1. Clone the Repository

```bash
git clone https://github.com/your-username/diversity-iq.git
cd diversity-iq
```

---

### ⚙️ 2. Backend Setup (FastAPI)

#### ✅ Step 1: Install Python Dependencies

Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

#### ✅ Step 2: Create `.env` File

In the root directory, create a `.env` file and add your OpenAI API key:

```env
OPEN_AI_API=your_openai_api_key_here
```

#### ✅ Step 3: Run the Backend Server

```bash
uvicorn main:app --reload
```

The backend will start at:  
📍 `http://127.0.0.1:8000`

---

### 🎨 3. Frontend Setup (React)

#### ✅ Step 1: Navigate to Frontend Folder

```bash
cd frontend
```

#### ✅ Step 2: Install Node Modules

```bash
npm install
```

#### ✅ Step 3: Start the Frontend

```bash
npm start
```

The frontend will start at:  
🌐 `http://localhost:3000`

---

## ✨ Features

- 📊 **Category-wise Distribution Stats**
- ⚖️ **Fairness Verdict**
- 💡 **Actionable Suggestions** to improve dataset balance
- 🧠 Uses **OpenAI** for smart analysis
- 📈 Ready for frontend visualization

---

## 🧪 Sample Output

Upload a CSV file with columns like `gender`, `ethnicity`, etc. The tool returns:

```json
{
  "gender": {
    "male": 60,
    "female": 40
  },
  "genderComment": "One category has over 50% representation. Consider balancing.",
  "verdict": "Unfair Distribution"
}
```

---

## 🛠 Tech Stack

- **Frontend**: React.js
- **Backend**: FastAPI
- **AI Integration**: OpenAI API
- **Languages**: Python, JavaScript

---