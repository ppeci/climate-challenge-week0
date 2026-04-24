# Climate Challenge Project

## Setup Instructions

Follow these steps to reproduce the environment:

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd climate-challenge-week0
```

### 2. Create virtual environment

```bash
python -m venv nenv
```

### 3. Activate environment

**Windows:**

```bash
nenv\Scripts\activate
```

**Mac/Linux:**

```bash
source nenv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Continuous Integration (CI)

This project uses GitHub Actions to:

* check Python version
* install dependencies automatically on push

---

## Project Structure

```
climate-challenge-week0/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── nenv/              # virtual environment (ignored)
├── data/              # datasets (ignored)
├── requirements.txt
├── .gitignore
└── README.md
```

