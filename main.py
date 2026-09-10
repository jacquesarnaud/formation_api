from fastapi import FastAPI,Query,Path,Body,HTTPException
from heroes import HEROES
from ulils import find_proper_hero_id
from classes import *
from starlette import status
from database import db_dependency,engine
from sqlalchemy import text
from models import Heroes
import models


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
@app.get("/")
async def heatbeat(db: db_dependency):
    try:
        db.execute(text("SELECT 1"))
        return {"message":"DATABASE OK"}
    except Exception as e:
        return {"error" : e}

@app.get("/heroes", status_code=status.HTTP_200_OK)
#recuperer tous les postes 
async def get_all_heroes(db:db_dependency):
    return db.query(Heroes).order_by(Heroes.id.asc()).all()

#recuperer les heroes par rarity
@app.get("/heroes/rarity",status_code=status.HTTP_200_OK)
async def get_all_heroes_by_rarity(db:db_dependency ,nu_rarity:int = Query(ge=0 , le=10)):
    resul = db.query(Heroes).filter(Heroes.rarity >= nu_rarity ).all()
    return resul


#recuperer les heroes par name
@app.get("/heroes/name/{hero_name}",status_code=status.HTTP_200_OK)
async def get_all_heroes_by_name(db:db_dependency,hero_name:str = Path()):
    return  db.query(Heroes).filter(Heroes.name == hero_name).all()


#recuperer les heroes par id
@app.get("/heroes/id/{hero_id}",status_code=status.HTTP_200_OK)
async def get_all_heroes_by_name(db:db_dependency,hero_id:int = Path(gt=0)):
    return  db.query(Heroes).filter(Heroes.id == hero_id).all()

@app.post("/hero/create", status_code=status.HTTP_201_CREATED)
async def creat_hero(db:db_dependency,hero_body: Herovalidation = Body()):
    new_hero = Heroes(**hero_body.model_dump(exclude={"id"}))
    db.add(new_hero)
    db.commit()
    db.refresh(new_hero)

    return new_hero

@app.put("/hero/update" , status_code=status.HTTP_204_NO_CONTENT)
async def update_hero(hero_body : Herovalidation= Body()):
    hero_change = False
    for i in range(len(HEROES)) :
        if  HEROES[i].id == hero_body.id :
            hero_change = True
            HEROES[i] = Herovalid(**hero_body.model_dump())

    if not hero_change:
        raise HTTPException(status_code=404 , detail='hero pas trouvé')
    
@app.delete("/hero/delete/{ hero_id }" , status_code=status.HTTP_204_NO_CONTENT)

async def delete_hero(hero_id:int = Path(gt=0)):
    hero_delete = False
    for i in range(len(HEROES)):
        if HEROES[i].id == hero_id:
            hero_delete = True
            HEROES.pop(i) 
            return {"message": "Hero delete successfully"}
    if not hero_delete:
        raise HTTPException(status_code=404, detail='heor not fund')
