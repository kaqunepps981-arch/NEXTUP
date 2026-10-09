"""Minimal local NEXTUP API prototype. This does not connect to NBA 2K20 servers."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='NEXTUP local prototype', version='0.1.0')

class Health(BaseModel):
    status: str
    note: str

@app.get('/health', response_model=Health)
def health():
    return Health(status='ok', note='Local prototype only; no game integration is configured.')

@app.get('/roles')
def roles():
    return {'planned_roles': ['Mods', 'Content Creator', 'Beta Tester'], 'connected': False}
