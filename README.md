# 🕷️ Python Web Scraper (Playwright + Retry + Logging)

## 📌 Overview

This project is a **production-ready web scraping template** built using Python and Playwright.
It includes robust features like retry logic, structured logging, and clean architecture for scalability.

---

## 🚀 Features

* 🔁 Retry mechanism for handling transient failures (e.g., timeouts)
* 📊 Structured logging (debug, info, warning, error)
* ⏱️ Execution time tracking
* 🧩 Modular and reusable code design
* 🌐 Configurable target URL (no hardcoding)
* 📁 Clean JSON output
* ⚙️ Ready for scaling and real-world projects

---

## 🛠️ Tech Stack

* Python 3.x
* Playwright
* Logging module
* Flake8 (for linting)

---

## 📂 Project Structure

```
project/
│
├── scraper/
│   └── scraper.py        # Core scraping logic
│
├── utils/                # (Planned reusable utilities)
│   ├── retry.py
│   ├── logger.py
│   └── timeit.py
│
├── main.py               # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd project
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
python -m playwright install
```

---

## ▶️ Usage

Run the scraper:

```bash
python main.py
```

---

## 🌐 Configure Target URL

Edit in `main.py`:

```python
url = "https://quotes.toscrape.com"
scraper = QuoteScraper(base_url=url)
```

---

## 🔁 Retry Logic

* Retries only on `TimeoutError`
* Configurable retry count and delay
* Exponential backoff supported

---

## 📊 Logging

* DEBUG → function entry/exit
* INFO → successful operations
* WARNING → retry attempts
* ERROR → failures
* EXCEPTION → full traceback

---

## 📁 Output

Scraped data is saved as:

```
quotes.json
```

---

## 🧪 Linting

Run flake8:

```bash
flake8 .
```

---

## 📌 Future Improvements

* CLI arguments for dynamic input
* Database support (PostgreSQL)
* Parallel scraping
* Docker support
* Config file support (YAML/JSON)

---

## 🤝 Contributing

Feel free to fork and improve. Suggestions are welcome!

---

## 📄 License

MIT License

---

## 💡 Author Note

This project is designed as a **scalable template for freelance and production scraping tasks**, focusing on clean architecture, reliability, and maintainability.
