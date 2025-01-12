
from supabase_py_async import AsyncClient
from app.crud.base import CRUDBase
from app.schemas.auth import UserIn
from app.schemas.item import Item, ItemCreate, ItemInDB, ItemUpdate



class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    async def create(self, db: AsyncClient, *, obj_in: ItemCreate) -> Item:
        return await super().create(db, obj_in=obj_in)
    async def get(self, db: AsyncClient, *, id: str) -> Item | None:
        return await super().get(db, id=id)

    async def get_all(self, db: AsyncClient) -> list[Item]:
        return await super().get_all(db)

    async def get_multi_by_owner(self, db: AsyncClient, *, user: UserIn) -> list[Item]:
        return await super().get_multi_by_owner(db, user=user)
    
    async def get_multi_by_category(self, db: AsyncClient, *, category_id: str) -> list[Item]:
        return await super().get_multi_by_category(db, category_id=category_id)
    
    async def get_multi_by_team(self, db: AsyncClient, *, team_id: str) -> list[Item]:
        return await super().get_multi_by_team(db, team_id=team_id)

    async def update(self, db: AsyncClient, *, obj_in: ItemUpdate) -> Item:
        return await super().update(db, obj_in=obj_in)

    async def delete(self, db: AsyncClient, *, id: str) -> Item:
        return await super().delete(db, id=id)


item = CRUDItem(Item)