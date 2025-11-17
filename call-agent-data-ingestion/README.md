# Data Ingestion Service

Lightweight FastAPI service to accept ingestion records and persist them to PostgreSQL. Designed for deployment to Azure App Service as a Docker container and development with local Docker or a dev Postgres.

## Features
- POST /api/v1/data_ingestion endpoint
- Input validation with Pydantic
- Async database access using `asyncpg`
- API Key authentication via `X-API-Key` header (placeholder implementation)
- Dockerfile for containerized deployment
- Terraform scaffold for Azure resources and ACR
- GitHub Actions workflow for CI (tests  build  push  deploy)

## API

- Endpoint: `POST /api/v1/data_ingestion`
- Authentication: header `X-API-Key: <your-key>` (service reads `API_KEY` env var)
- Request JSON schema:

  {
    "user_id": "string",
    "timestamp": "ISO 8601 datetime string",
    "data_payload": { ... }  // arbitrary JSON object
  }

- Response: `201 Created` with body `{ "id": <record-id> }`

## Project layout

- `main.py` - FastAPI application and endpoint
- `app/db.py` - `PostgreSQLConnector` using `asyncpg`
- `requirements.txt` - Python dependencies
- `Dockerfile` - production image
- `tests/` - unit tests (pytest)
- `sql/init.sql` - SQL to create `ingestion_log` table
- `terraform/` - Terraform scaffold for Azure resources
- `.github/workflows/ci.yml` - CI workflow

## Environment variables

Required for runtime (set in App Service or your environment):

- `API_KEY` - expected API key for requests
- `DB_HOST` - Postgres host
- `DB_PORT` - Postgres port (default `5432`)
- `DB_NAME` - database name (e.g., `ingestiondb`)
- `DB_USER` - database user
- `DB_PASSWORD` - database password
- `PORT` - application port (default `8000`)

## Local development

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

2. Set env vars and run the app:

```bash
export API_KEY="dev-key"
export DB_HOST="localhost"
export DB_PORT="5432"
export DB_NAME="ingestiondb"
export DB_USER="postgres"
export DB_PASSWORD="postgres"
uvicorn main:app --reload
```

3. Run tests:

```bash
pytest -q
```

## Docker

Build and run locally:

```bash
docker build -t data-ingestion:local .
docker run -e API_KEY="dev-key" -e DB_HOST=localhost -p 8000:8000 data-ingestion:local
```

## Database schema

`sql/init.sql` creates the `ingestion_log` table:

```sql
CREATE TABLE IF NOT EXISTS ingestion_log (
    id BIGSERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    data_payload JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
```

## Terraform (Azure)

The `terraform/` folder provisions Azure resources. See `terraform/main.tf` for details.

## CI/CD (GitHub Actions)

The workflow at `.github/workflows/ci.yml` runs tests, builds Docker image, pushes to ACR, and updates Azure App Service.

Required GitHub secrets:
- `AZURE_CREDENTIALS`
- `ACR_NAME`
- `AZURE_RESOURCE_GROUP`
- `AZURE_WEBAPP_NAME`

## Security & production notes

- Replace simple API key check with a proper authentication method (Azure AD, rotating keys, etc.)
- Use Azure Key Vault for database credentials
- Use managed identity for ACR access
