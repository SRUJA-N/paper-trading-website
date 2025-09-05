# TODO: Switch to PostgreSQL with Docker

## Approved Plan Steps
- [x] Update `backend/config/database.py` to use PostgreSQL connection URL from settings
- [x] Update `docker-compose.yml` to add PostgreSQL service and remove SQLite volume
- [x] Update `backend/Dockerfile` to wait for database readiness
- [x] Remove existing `app.db` file
- [x] Test with `docker-compose up` to ensure services start correctly
- [x] Verify database tables are created properly
- [x] Fix pydantic-settings import error by adding pydantic-settings to requirements.txt
- [ ] Rebuild with --no-cache to apply pydantic-settings changes
