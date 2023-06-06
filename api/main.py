from fastapi import FastAPI
from pwgen import pwgen, getWord, spell_number

app = FastAPI()

@app.get("/pwgen/")
async def getPW(count: int=3, format: str = "%jt4%nt0%s%d3%s%d4"):
    this_pw = []
    for i in range(count):
      this_pw.append(str(pwgen(format)))
    return {"pw list": this_pw}

@app.get("/pwgen/alacart/")
async def getPart(number: int=3, type: str = "n"):
  rtnType = "spell_num" if type == "0" else type
  number = 0 if rtnType == "spell_num" and number == 3 else number
  type = type[1] if rtnType[0] == "c" else type
  
  this_type = []
  match rtnType:
    case "n"|"v"|"j"|"b"|"w"|"1"|"2"|"3":
      for i in range(number):
        this_type.append(getWord(type))
    case "spell_num":
        this_type.append(spell_number(str(number)))
  return{"pw list": this_type}