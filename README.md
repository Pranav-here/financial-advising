
# 🧠 Financial Advising Agents with Phidata

This project showcases two specialized AI agents: a **Financial Analyst** and a **Web Researcher**, built using the [Phidata](https://docs.phidata.com/) framework. These agents are designed to answer financial questions (stock prices, fundamentals, analyst recommendations) and perform real-time web searches with citations.

🔗 [📽️ Watch Demo Video](https://iit0-my.sharepoint.com/:v:/r/personal/pkuchibhotla_hawk_iit_edu/Documents/Phidata%20-%20Chat%20-%20Google%20Chrome%202025-06-07%2018-01-21.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=sPQy3y)

---

## 🚀 Features

- 📈 **Financial Analyst Agent**
  - Pulls real-time **stock prices**, **analyst recommendations**, and **fundamentals**
  - Uses `YFinanceTools` for accurate and updated data
  - Auto-formats responses in clean **Markdown tables**

- 🌐 **Web Researcher Agent**
  - Uses `DuckDuckGo` to perform live web searches
  - Responds with sources and citations
  - Good for news, current events, or company info

- 🧠 **Team Agent**
  - Smartly routes queries to the relevant agent
  - Supports debug logs and reasoning traces
  - Modular – easily extendable to more agents or domains

- 🧪 **Interactive Playground**
  - Launch the app locally with a Streamlit-like interface
  - Ask finance or web questions in a chat UI

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Pranav-here/financial-advising.git
cd financial-advising
```

### 2. Install Dependencies

Use Pipenv:

```bash
pipenv install
pipenv shell
```

Or just use `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

Create a `.env` file and add your keys:

```env
OPENAI_API_KEY=your-openai-key
GROQ_API_KEY=your-groq-key
```

### 4. Run the Playground App

```bash
phi euth
python playground.py
```

---

## 🧪 How to Use

- Run `playground.py` to launch the local UI
- Ask questions like:
  - `"Compare analyst recommendations for Tesla and Apple"`
  - `"What's the latest news about Nvidia?"`
- Agents will auto-select and return clean, contextual answers

> ✅ [Watch the video walkthrough here](https://iit0-my.sharepoint.com/:v:/r/personal/pkuchibhotla_hawk_iit_edu/Documents/Phidata%20-%20Chat%20-%20Google%20Chrome%202025-06-07%2018-01-21.mp4)

> *See the `/Working App/` folder for example outputs.*

---

## 🧠 Code Structure

| File                | Purpose                                              |
|---------------------|------------------------------------------------------|
| `financial_advisors.py` | Financial agent logic setup with YFinance tools    |
| `playground.py`        | Launches web UI using Phidata's Playground         |
| `testing.py`           | Simple script to test agents via CLI               |
| `Pipfile` / `requirements.txt` | Package dependencies                       |

---

## 📌 Future Ideas

- Add a News Summary Agent using `NewsAPI`
- Integrate earnings calendar + price prediction models
- Deploy the UI using FastAPI + Vercel

---

## 👨‍💻 Author

**Pranav Kuchibhotla**  
💻 [Portfolio](https://pranavkuchibhotla.com) | 🔗 [LinkedIn](https://www.linkedin.com/in/pranavkuchibhotla/)

---

## 📄 License

MIT – feel free to fork and build on it!
