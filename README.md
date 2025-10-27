# 📚 AI-Youtube-plus-Web-Summarizer
A LangChain + Groq powered Streamlit application that automatically summarizes YouTube videos and web articles into concise 300-word summaries using state-of-the-art LLMs.

---

## 🖼️ Application Preview

#### Home Screen
![Home UI](images/main.png) 

#### Summary Output
![Summary Output](images/output.png) 

---


## 🚀 Features

- 🔗 Accepts **YouTube video links** or **website URLs**
- 🤖 Uses **Groq LLM (llama-3.3-70b-versatile)** for natural language summarization  
- ⚡ Built with **LangChain Summarization Chains**
- 🎨 Interactive and modern Streamlit UI
- 🧠 Automatically extracts YouTube transcripts or web content
- 🔒 Secure API key input through sidebar

---

## 🧩 Tech Stack

| Component | Technology |
|:--|:--|
| Frontend | Streamlit |
| LLM Model | Groq – LLaMA 3.3 (70B) |
| Framework | LangChain (PromptTemplate + Summarize Chain) |
| Data Loaders | YouTubeLoader, UnstructuredURLLoader |
| Language | Python 3.10+ |

---

## 🏗️ Project Structure
```bash
├── images # Screenshot folder
├── .gitignore
├── README.md
├── apjspeech.pdf # pdf for practicing text summarizer
├── app.py # main application
├── requirements.txt # Dependencies list
└── text_summarizer.ipynb # practice file
```

---


## ⚙️ Setup & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/pahul1712/SmartSummarizer-AI-(YT-and-Web).git
   cd SmartSummarizer-AI-(YT-and-Web)
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app
   ``` bash
   streamlit run app.py
   ```
4. Add your Groq API key in the sidebar and paste a YouTube or Website URL.


---

## 🧠 How It Works

- Extracts text from YouTube video transcripts or web articles.
- Passes the text to LangChain’s summarization chain with a custom prompt.
- Groq’s LLM (LLaMA 3.3 70B) generates a concise 300-word summary.
- Displays the summary beautifully in the app UI.


## 🧑‍💻 Author

Pahuldeep Singh Dhingra
Graduate Teaching Assistant | M.S. Data Science & Analytics @ FAU


