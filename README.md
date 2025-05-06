# 🌍 Country Info Portal (Django)

This project is a Django-based application that fetches and stores country data from a public API and provides RESTful API access, a styled web interface, and user authentication.

---

## 📌 Features

### ✅ Phase 1: Data Fetching and Storage
- Fetches country data from [`https://restcountries.com/v3.1/all`](https://restcountries.com/v3.1/all).
- Stores country details including name, region, code, population, timezone, languages, and flag.
- Script to fetch and load data into the database.

### ✅ Phase 2: RESTful API Endpoints
- `GET /api/countries/`: List all countries.
- `GET /api/countries/<pk>/`: Retrieve a specific country.
- `POST /api/countries/`: Create a new country.
- `PUT /api/countries/<pk>/`: Update country info.
- `DELETE /api/countries/<pk>/`: Delete a country.
- `GET /api/countries/<pk>/same_region/`: Countries in the same region.
- `GET /api/countries/by-language/<lang_code>/`: Countries that speak a given language.
- `GET /api/countries/?search=<name>`: Search countries by partial name.

### ✅ Phase 3: Web Interface (Bootstrap)
- User-friendly HTML interface to view countries.
- Table listing with: Name, CCA2, Capital, Population, Timezone, and Flag.
- Search field for country names.
- “Details” button shows:
  - Countries in the same region.
  - Spoken languages of the country.
- Styled using **Bootstrap 5**.

### ✅ Phase 4: Authentication and Security
- Login page for registered users.
- All REST API endpoints are restricted to **authenticated users**.
- Uses Django’s default authentication system (`django.contrib.auth`).

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, Bootstrap
- **Auth:** Django built-in authentication system
- **Data Source:** [restcountries.com](https://restcountries.com/v3.1/all)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
1. git clone https://github.com/yourusername/country-info.git
cd country-info


2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py migrate

5. Create Superuser
python manage.py createsuperuser

6. Fetch Country Data
python manage.py fetch_countries

7. Run Development Server
python manage.py runserver

