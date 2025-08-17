# 🔍 File Searcher: Search Files by Extension or Name

This is a simple command-line Python project that allows users to search for files in a given directory based on:

- File **extension(s)** (e.g., `.txt`, `.py`, etc.)
- File **name** (case-insensitive)

Ideal for beginners learning how to build modular, testable Python projects.

---

## 📌 Features

- Search files by one or more extensions
- Search files by name (case-insensitive)
- Recursive search in subdirectories
- Friendly error messages
- Supports automated testing with `unittest`

---

## ⚙️ Requirements

- Python 3.10 or higher  
  (No external libraries are required.)

---

## 🚀 How to Use

Open your terminal and run the project like this:

### ✅ Search by Extension(s)

```bash
python main.py /path/to/search --extension txt py md
```

You can enter multiple extensions (without the dot).

### ✅ Search by Name

```bash
python main.py /path/to/search --name report

```

### Example Output

```
Found files:
- /home/user/docs/report1.txt
- /home/user/docs/Report2.TXT

```

### 🧪 Running Tests

To run the automated tests:

```bash
python -m unittest discover -s tests

```

## 📁 Project Structurej

```
file_searcher_project/
├── file_searcher/
│   └── search.py
├── tests/
│   └── test_search.py
├── main.py
└── README.md

```
