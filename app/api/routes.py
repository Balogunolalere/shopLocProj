from fastapi import APIRouter, HTTPException
from ..models.shop import Shop, ShopCreate, ShopUpdate, ShopList
from ..database import crud
from ..services import maps
from ..services.maps import generate_map_page
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get('/shops', response_model=ShopList)
async def get_shops():
    shops = crud.get_shops()
    return {"shops": shops}

@router.get('/shops/{shop_id}', response_model=Shop)
async def get_shop(shop_id: str):
    shop = crud.get_shop(shop_id)
    if shop:
        return shop
    raise HTTPException(status_code=404, detail="Shop not found")

@router.post('/shops', response_model=Shop)
async def create_shop(shop: ShopCreate):
    return crud.create_shop(shop)

@router.put('/shops/{shop_id}', response_model=Shop)
async def update_shop(shop_id: str, shop: ShopUpdate):
    return crud.update_shop(shop_id, shop)

@router.delete('/shops/{shop_id}')
async def delete_shop(shop_id: str):
    return crud.delete_shop(shop_id)

@router.get('/maps')
async def get_maps():
    shops = crud.get_shops()
    map_html = maps.generate_map(shops)
    page = generate_map_page(map_html)

    return HTMLResponse(content=page, status_code=200) 
