# NEXTUP local API prototype

This is a development-only FastAPI starter. It does **not** restore retired NBA 2K20 online services, modify player ratings, or integrate with the game.

## Run locally

1. Install Python 3.10+.
2. From this folder, run `python -m pip install -r requirements.txt`.
3. Run `uvicorn main:app --host 127.0.0.1 --port 8000`.
4. Visit `http://127.0.0.1:8000/health`.

Only bind to localhost while testing. Do not put Steam passwords or Discord bot tokens into source code.
