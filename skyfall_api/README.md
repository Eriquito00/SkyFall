# skyfall_api

A project created with FastAPI CLI.

## Quick Start

### Start the development server

```bash
uv run fastapi dev
```

Visit http://localhost:8000

The root endpoint (`GET /`) returns a welcome message, the current number of
meteorites, and a link to the API documentation.

### List meteorites

`GET /meteorites` returns a page of meteorites. Pagination uses `page` (default
`1`, starting at `1`) and `limit` (default `10`, maximum `1000`). Optional filters are `search`
(case-insensitive partial match on the name), `fall` (`Fell` or `Found`), and
`min_mass` (minimum mass in grams; meteorites without a mass are excluded).
Filters are applied before pagination.

For example, `GET /meteorites?page=2&limit=10&search=aar&fall=Fell&min_mass=100`
returns the matching items and their pagination metadata: filtered `total`,
`total_pages`, `page`, and `limit`.

### Create and delete meteorites

`POST /meteorites` requires `name`, `nametype` (`Valid` or `Relict`),
`recclass`, and `fall` (`Fell` or `Found`). Mass, year, coordinates, and
`GeoLocation` are optional. The API assigns the next available ID.

Example request body:

```json
{
  "name": "New Meteorite",
  "nametype": "Valid",
  "recclass": "L5",
  "mass (g)": 12.5,
  "fall": "Found",
  "year": 2024,
  "reclat": 40.4,
  "reclong": -3.7,
  "GeoLocation": "(40.4, -3.7)"
}
```

`DELETE /meteorites/{id}` removes the matching meteorite and returns it; an
unknown ID returns `404`.

Changes persist in `src/persistence/data/meteorite_landings_editable.csv`.
The original `meteorite_landings.csv` is left unchanged.

### Deploy to FastAPI Cloud

Sign up and log in at https://fastapicloud.com, then deploy with:

```bash
uv run fastapi deploy
```

## Project Structure

- `main.py` - Your FastAPI application
- `pyproject.toml` - Project dependencies
- `service/` - Meteorite use cases and business rules

## Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [FastAPI Cloud](https://fastapicloud.com)
