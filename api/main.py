from fastapi import FastAPI
from pwgen import pwgen

app = FastAPI()

@app.get("/pwgen/")
async def getPW(count: int=5, format: str = "%jt4%nt0%s%d3%s%d4"):
    this_pw = []
    for i in range(count):
      this_pw.append(str(pwgen(format)))
    return {"message": this_pw}