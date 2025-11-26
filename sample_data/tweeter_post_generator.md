# 🚀 AI-Powered Tweet Generation Agent

This project is an automated AI agent that generates and posts tweets based on any article link you provide. It combines the power of **LangChain**, **Gemini**, **BeautifulSoup4**, and **Tweepy** to create high‑quality, context‑aware tweet content and publish it directly to your Twitter (X) account.

---

## ✨ Features

* **🔍 Article Scraping:** Extracts clean and relevant text from the article URL using `BeautifulSoup4`.
* **🧠 AI Text Generation:** Uses **Google Gemini** via **LangChain** to summarize and generate engaging tweet text.
* **🐦 Auto Tweet Posting:** Uses **Tweepy** to directly publish the tweet to your X (Twitter) account.
* **⚙️ Modular Architecture:** Each component (scraping, generation, tweeting) is separate, easy to modify and extend.
* **📦 Environment Variables:** Secure authentication handled through `.env` file.

---

## 🛠️ Tech Stack

* **Python**
* **LangChain** – LLM pipeline
* **Gemini API** – text generation
* **BeautifulSoup4** – article content extraction
* **Tweepy** – posting the tweet

---

## 📁 Project Structure

```
project/
│
├── main.py                # Main agent logic
├── web_crawler.py         # Fetch + parse article content
├── tweet_client.py        # Tweepy client initializer
├── tweeter_utils.py       # Tweet posting logic
├── .env                   # API keys and secrets
├── requirements.txt       # Dependencies
├── model.py               # Model and it's configs
├── post_generator.py      # LLM prompt + generation
└── README.md              # Documentation
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AMalfez/tweeter_post_generator.git
cd tweeter_post_generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your environment variables

Create a `.env` file:

```
X_API_KEY="your_tweeter_api_key"
X_API_KEY_SECRET="your_tweeter_api_key_secret"
X_ACCESS_TOKEN="your_tweeter_access_token"
X_ACCESS_TOKEN_SECRET="your_tweeter_access_token_secret"
X_CLIENT_ID="your_tweeter_client_id"
X_CLIENT_SECRET="your_tweeter_client_secret"

GOOGLE_API_KEY="your_gemini_api_key"
```

### 4. Run the agent
Test if article is generating properly:
```bash
python post_generator.py
```
If generating properly, run:
```bash
python main.py 
```

---

## 🧠 How It Works

1. **URL** → You pass an article link to main() in main.py.
2. **Scraper Module** fetches and extracts clean text.
3. **LangChain + Gemini** turns the article into a concise tweet.
4. **Tweepy Module** posts the tweet to your Twitter account.

---

## 🧩 Customization

* Modify the tweet style (casual, formal, thread mode, hashtags).
* Add support for auto‑thread creation.
* Include link-shortening features.
* Integrate sentiment style or topic‑based formatting.
* Save the generated post to DB, it will act as draft post, fetch again and tweet.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---


## 🙌 Acknowledgements

* Google Gemini API
* LangChain Framework
* BeautifulSoup4
* Tweepy

---

If you like this project, consider giving it a ⭐ on GitHub!
