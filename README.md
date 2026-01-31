# Mini MDM API

This project is a small **Device Management API** built with **Django Rest Framework**.
It demonstrates secure multi-user data isolation and business rule enforcement for managing **Fleets** and **Devices**.

The application is fully containerized and runs with Docker.

---

## Tech Stack

* Python / Django
* Django Rest Framework
* SQLite
* Docker & Docker Compose

---

## How to Run

```bash
docker compose up --build
```

Then apply migrations:

```bash
docker compose exec web python manage.py migrate
```

The API will be available at:

**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

Admin panel:

**[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## Test Accounts

| Role               | Username | Password          |
| ------------------ | -------- | ----------------- |
| Admin              | `admin`  | `admin`           |
| User 1             | `user1`  | `yGU6bapAvqKvUJZ` |
| User 2             | `user2`  | `DN98nW6eXpmvXjd` |
| Superuser (Docker) | `root`   | `root`            |

Authentication is required for all API endpoints (Basic Auth).

---

## Business Rules Implemented

* Users must be authenticated to access the API
* Users can only see and manage **their own Fleets**
* Users can only manage **Devices in their Fleets**
* Devices can only be moved between Fleets owned by the same user
* Devices must be created in a Fleet owned by the user
* Device list supports filtering by Fleet
