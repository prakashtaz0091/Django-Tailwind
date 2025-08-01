## A simple base setup for Django and Tailwind

## To start project with this base setup, do the following:

### 1. Clone or download this repository

```
git clone --branch django-tailwind-minimal https://github.com/prakashtaz0091/Django-Tailwind.git your-project-name

```

or if your don't have git installed, [click here to download project](https://github.com/prakashtaz0091/Django-Tailwind/archive/refs/heads/django-tailwind-minimal.zip)

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run migrations

```
python manage.py migrate
```

### 4. Run server

```
python manage.py tailwind dev
```

### 5. Visit http://localhost:8000

### 6. Extend `base.html` in other templates where you want to use Tailwind CSS
