# Django project for art-by-ck

This project was created with Django and is configured for PostgreSQL. Connect this project to your GitHub repository named 'art-by-ck' for version control.

## Setup

1. Create a virtual environment (already set up if you followed the instructions).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your PostgreSQL database in `art_by_ck/settings.py`.
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## GitHub Integration

- Initialize git and add your remote:
  ```bash
  git init
  git remote add origin https://github.com/<your-username>/art-by-ck.git
  ```
- Commit and push your code:
  ```bash
  git add .
  git commit -m "Initial Django project setup"
  git push -u origin main
  ```

## Deployment

- Update `ALLOWED_HOSTS` and database settings for production.
- Use environment variables for sensitive data.

---

Replace this README with project-specific details as you develop.
