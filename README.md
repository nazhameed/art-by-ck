# Django project for art-by-ck

This project was created with Django and is configured for PostgreSQL. Connect this project to your GitHub repository named 'art-by-ck' for version control.

## Design Philosophy

The design for this project began with a deep dive into understanding the artist and her vision. We studied the existing site and took notes on the recurring themes in her artwork especially the celebration of femininity. Our goal was to create a digital space that honors these elements while providing a cleaner, more modern look.

Key design choices:

- **Artist Centric:** The layout and color palette are crafted to let the artwork remain the main focus, with minimal distractions.
- **Feminine Motifs:** Subtle design cues and gentle curves echo the femininity present in the artist's work.
- **Modern & Clean:** We introduced more whitespace and a grid-based structure for clarity and ease of navigation.
- **Pop Art Accents:** Slight pop art elements and bold accent colors add vibrancy without overpowering the content.
- **Content-Ready:** The site is structured to accommodate rich content—biography, journal, exhibitions, and available art—while maintaining visual harmony.

Throughout, the intent was to balance a gallery inspired feel with a welcoming, contemporary web experience that puts the artist and her creations at the center.

## Setup

1. Create a virtual environment (already set up if you followed the instructions).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your PostgreSQL database in `config/settings.py`.
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
  git remote add origin https://github.com/nazhameed/art-by-ck.git
  ```
- Commit and push your code:
  ```bash
  git add .
  git commit -m "Initial Django project setup"
  git push -u origin main
  ```

## Local Development

- Setup a `.env` file for environment variables (see `.env.example`)

## Deployment

- Update `ALLOWED_HOSTS` and database settings for production.
- Use environment variables for sensitive data.
- When deploying to heroku, only the production database url is needed.
- Add config vars to heroku:
  ![image](/docs/readme/images/heroku-config.png)

## Dashboard Panel

To empower the artist with full control over her website content, we developed a custom dashboard panel. This admin interface is designed to be intuitive and accessible, allowing the artist to easily manage all key aspects of the site without technical barriers.

**Access:**
- The dashboard is available at [`/ck-admin-panel/`](http://localhost:8000/ck-admin-panel/) (or your deployed domain).

**Key features:**
- **Unified Access:** All major content types gallery images, available art, exhibitions, and journal entries can be created, edited, or removed from a single dashboard.
- **User-Friendly Forms:** Clean, simple forms make it easy to update artwork details, upload images, and manage exhibition or journal information.
- **Live Updates:** Changes made in the dashboard are reflected immediately on the public site, ensuring the artist’s portfolio is always up to date.
- **Secure:** Only authorized users can access the dashboard, protecting the integrity of the site’s content.
- **Modern Layout:** The dashboard uses a clear, card-based layout for quick navigation and a visually organized experience.

This approach ensures the artist has as much control as possible over her online presence, with minimal friction and maximum flexibility.

## Features

- Unified, art gallery inspired background and modern CSS throughout
- Responsive navbar with logo and custom favicon
- Gallery, About, Available Art, Exhibitions, and Journal pages with consistent design
- Hover effects for gallery and available art images
- Quotes and cursive typography for artistic flair
- Custom dashboard panel for easy content management at `/ck-admin-panel/`
- Secure, user friendly admin interface
- Mobile friendly, responsive layout
- Static files managed for production (Django staticfiles)
- PostgreSQL database support


