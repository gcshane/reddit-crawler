# 🚀 Reddit Crawler Web App

A full-stack web application that crawls the top 20 posts from [r/memes](https://reddit.com/r/memes) from the past 24 hours, generates a PDF report, and sends it to a specified Telegram user via a bot.

---

## 📦 Features

- 🔍 Crawls top Reddit posts using PRAW
- 📄 Generates a PDF report
- 🤖 Sends report to users via a Telegram bot
- 🌐 Full web UI built with React
- 🔁 Daily meme summaries straight to Telegram

---

## 🛠️ Tech Stack

- **Frontend**: React + CSS
- **Backend**: Flask + PRAW (Reddit API) + FPDF + Telegram Bot API
- **Database**: MongoDB

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/gcshane/reddit-crawler.git
cd reddit-crawler
```

---

### 2. Backend Setup (Flask)

#### 🔹 Create Virtual Environment

```bash
cd flaskr
python3 -m venv .venv
source .venv/bin/activate
```

#### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 🔹 Environment Variables

Create a `.env` file inside the `flaskr/` directory:

```env
client_id = <your_reddit_client_id>
client_secret = <your_reddit_client_secret>
user_agent = <your_reddit_user_agent>
mongo_uri = <your_mongodb_uri>
telegram_token = <your_telegram_bot_api_token>
FLASK_APP = server

```

#### 🔹 Run the Flask Server

```bash
cd ..
python -m flask run
```

---

### 3. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

Frontend will be available at [http://localhost:3000](http://localhost:3000)

---

## 🧪 Usage

1. Visit the frontend UI
2. Click the "bot" URL and be redirected to the Telegram bot
3. Started the bot on Telegram with `/start`
4. Enter your Telegram username (without `@`)
5. Click **"Generate Report"**

---

## 📄 License

MIT License
