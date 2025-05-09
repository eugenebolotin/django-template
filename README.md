# Django-template

**Django-template** is a base starter template for Django projects.

---

## 🧩 Technologies Used

- ⚙️ **[Uvicorn](https://www.uvicorn.org/)** as the application server (ASGI-compatible)
- 🚀 **[uv](https://github.com/astral-sh/uv)** as the package manager (fast `pip` replacement)
- 🐘 **PostgreSQL** as the default database
- 🔐 **[python-decouple](https://github.com/henriquebastos/python-decouple)** for managing environment variables
- 🐳 **Docker** and **Docker Compose** for containerization

---

## 🚀 How to Use This Project

1. Copy the repository contents to your own project folder.
2. Rename and fill in the `.env` file (from `env`).
3. Rename and fill in the `.env.postgres` file (from `env.postgres`).

---

### 💻 Local Development

You can run the project locally using:

```bash
uv run manage.py runserver --verbosity 2 --traceback
```

### env-файл variables

| Variable Name            | Example Value                                                               | Description                                                                 |
| :----------------------- |:----------------------------------------------------------------------------| :-------------------------------------------------------------------------- |
| `DEBUG`                  | `True`                                                                      | Controls whether the application runs in debug mode. Set to `False` in production. |
| `ALLOWED_HOSTS`          | `localhost,127.0.0.1`                                                       | A comma-separated string of hosts/domain names that the application should respond to. Essential for security. |
| `CORS_ALLOWED_ORIGINS`   | `http://localhost,http://127.0.0.1`                                         | A comma-separated string of origins (including scheme and port) that are allowed to make cross-origin requests. |
| `CORS_ALLOW_ALL_ORIGINS` | `False`                                                                     | If `True`, allows requests from any origin. Setting to `False` and using `CORS_ALLOWED_ORIGINS` is more secure. |
| `DATABASE_URL`           | `sqlite:///db.sqlite3` or `postgres://<user>:<password>@<host>:<port>/<db>` | Database connection string, often in URL format, specifying the database type, credentials, host, port, and database name. |
| `DJANGO_SUPERUSER_USERNAME` | `admin`                                                                     | The username for creating or managing the application's superuser (administrator) account. |
| `DJANGO_SUPERUSER_PASSWORD` | `qwerty`                                                                    | The password for the application's superuser account.                           |
| `DJANGO_SUPERUSER_EMAIL` | `email@example.com`                                                         | The email address for the application's superuser account.                    |
| `DJANGO_SECRET_KEY`      | `1234567890`                                                                | A unique, unpredictable secret key used by Django for cryptographic signing. **Must be kept secret.** |

### env.postgres-файл variables

These variables are commonly used to configure an official PostgreSQL Docker container or similar database setups.

| Variable Name   | Example Value | Description                                                       |
| :-------------- |:--------------| :---------------------------------------------------------------- |
| `POSTGRES_DB`   | `projectdb`   | Specifies the name of the default database to be created when the container starts. |
| `POSTGRES_USER` | `user`        | Specifies the name of the default user to be created with access to the database. |
| `POSTGRES_PASSWORD` | `qwerty`      | Specifies the password for the default user. **Must be kept secret.** |