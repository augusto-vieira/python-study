# main.py
from db import SessionLocal
from models import POI

# Função para adicionar um POI
def add_poi(name: str, x: int, y: int):
    session = SessionLocal()
    try:
        poi = POI(name=name, x=x, y=y)
        session.add(poi)
        session.commit()
        print(f"POI '{name}' adicionado com sucesso!")      
    except Exception as e:
        session.rollback()
        print("Erro ao adicionar POI:", e)      
    finally:
        session.close()

# Função para listar todos os POIs
def list_pois():
    session = SessionLocal()
    try:
        pois = session.query(POI).all()
        for poi in pois:
            print(poi)           
    finally:
        session.close()

# Função para buscar POI por nome
def find_poi(name: str):
    session = SessionLocal()
    try:
        pois = session.query(POI).filter(POI.name.ilike(f"%{name}%")).all()
        return pois
    finally:
        session.close()

# Função para atualizar POI
def update_poi(poi_id: int, new_name: str, new_x: int, new_y: int):
    session = SessionLocal()
    try:
        poi = session.query(POI).get(poi_id)
        if poi:
            poi.name = new_name
            poi.x = new_x
            poi.y = new_y
            session.commit()
            print("POI atualizado com sucesso!")
        else:
            print("POI não encontrado!")
    finally:
        session.close()

# Função para deletar POI
def delete_poi(poi_id: int):
    session = SessionLocal()
    try:
        poi = session.query(POI).get(poi_id)
        if poi:
            session.delete(poi)
            session.commit()
            print("POI removido com sucesso!")
        else:
            print("POI não encontrado!")
    finally:
        session.close()

if __name__ == "__main__":
    # Adicionando alguns POIs
    add_poi("Praça Central", 20, 35)
    add_poi("Museu da Cidade", 45, 60)

    print("\nLista de POIs:")
    list_pois()

    print("\nBuscando por 'Museu':")
    for p in find_poi("Museu"):
        print(p)

    print("\nAtualizando POI id=1:")
    update_poi(1, "Praça Nova Central", 25, 40)
    list_pois()

    print("\nRemovendo POI id=2:")
    delete_poi(2)
    list_pois()


    ## Novos POIs
    add_poi("Lanchonete", 27, 12)
    add_poi("Posto", 31, 18)
    add_poi("Joalheria", 15, 12),
    add_poi("Floricultura", 19, 21)
    add_poi("Pub", 12, 8)
    add_poi("Supermercado", 23, 6)
    add_poi("Churrascaria", 28, 2)
    list_pois()