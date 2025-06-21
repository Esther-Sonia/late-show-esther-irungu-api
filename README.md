# 🎙️ Late Show Guest API
A Flask-based RESTful API to manage episodes, guests, and their appearances on a talk show.

## 📖 Description
- The Late Show API allows you to:

- View all episodes with show dates and numbers

- View individual episode details

- List all guests

- Record and track guest appearances, including ratings

---

## 🧱 Technologies Used

- Python 3
- Flask (Backend framework)
- Flask-SQLAlchemy (Database ORM)
- Postman (API testing)

---

## 📁 Project Structure

````
lateshow-esther-irungu/
│
├── app/
│   ├── __init__.py      # Initializes the Flask app and extensions
│   ├── models.py        # Defines database models and relationships
│   ├── routes.py        # Contains API route definitions
│   ├── seed.py          # Script to seed the database with data
│
├── migrations/          # Database migration files (auto-generated)
├── run.py               # Main file to run the Flask app
├── config.py            # App configuration settings
├── .gitignore           # Lists files/folders to exclude from git
└── README.md            # Project overview and setup instructions

````
---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/lateshow-esther-irungu.git
   cd lateshow-esther-irungu

2. **Create and activate virtual environment**

```bash

python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash

pip install -r requirements.txt

```
4. **Setup Environment variables**

```bash

FLASK_APP=app
PYTHONPATH=.
```
5. **Run migrations**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
6. **seed the database** 
```bash
python seed.py
```
7. **Start the Flask server**
```bash
python run.py
The server will run on: http://localhost:5555
```


## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/episodes` | Get all episodes |
| GET | `/episodes/<int:id>` | Get specific episode with guests |
| GET | `/guests` | Get all guests |
| POST | `/appearances` | Create new appearance |


## ✨ Key Features
- RESTful Routes – Built using standard REST principles

- Relational Models – Episodes ↔ Guests via Appearances

- Seed from CSV – Auto-import guest & episode data

- Validation & Error Handling – For clean request handling

- Modular Codebase – All logic separated cleanly into files



## 👩🏽‍💻 Project Owner
Esther Muthoni Irungu
📧 Email: esthersonia21@gmail.com

## ❓ Support
If you encounter any issues or have questions, feel free to reach out via email.



## 🪪 License
This project is licensed for educational use under the MIT License.
Feel free to fork it, play with it, and give credit when due! 😊

