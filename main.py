from fastapi import FastAPI,Query,Path,Body
from heroes import HEROES
from ulils import find_proper_hero_id

app = FastAPI()

@app.get("/")
async def heatbeat():
    return 'app fastapi'

@app.get("/heroes")
#recuperer tous les postes 
async def get_all_heroes():
    return HEROES

#recuperer les heroes par rarity
@app.get("/heroes/rarity")
async def get_all_heroes_by_rarity(nu_rarity:int = Query()):
    resul = []
    for hero in HEROES :
        if nu_rarity == hero.rarity:
            resul.append(hero)

    return resul


#recuperer les heroes par name
@app.get("/heroes/name/{hero_name}")
async def get_all_heroes_by_name(hero_name:str = Path()):
    for hero in HEROES :
        if hero_name.casefold() in hero.name.casefold():
            return hero


#recuperer les heroes par id
@app.get("/heroes/id/{hero_id}")
async def get_all_heroes_by_name(hero_id:int = Path()):
    for hero in HEROES :
        if hero_id == hero.id:
            return hero



@app.post("/hero/create")
async def creat_hero(hero_body = Body()):
    HEROES.append(find_proper_hero_id(hero_body))

    return HEROES[-1]



@app.put("/hero/update/{ hero_id }")
async def update_hero(hero_id:int , hero_body = Body()):
    for i in range(len(HEROES)):
        if HEROES[i].get("id") == hero_id:
            hero_body["id"] = hero_id
            HEROES[i] = hero_body 
            return {"message": "Hero updated successfully"}
    
    return {"error": "Hero not found"}


@app.delete("/hero/delete/{ hero_id }")

async def delete_hero(hero_id:int = Path):
    for i in range(len(HEROES)):
        if HEROES[i].id == hero_id:
            HEROES.pop(i) 
            return {"message": "Hero delete successfully"}
            break
    return {"error": "Hero not found"}
