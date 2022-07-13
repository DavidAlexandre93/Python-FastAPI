from fastapi import HTTPException
from datetime import date, timedelta
from aiohttp import ClientSession
from sqlalchemy import delete
from sqlalchemy.future import select
from database.models import User, Favorite
from database.connection import async_session


class UserService:
    async def create_user(self, name: str):
        async with async_session() as session:
            try:
                session.add(User(name=name))
                await session.commit()
            except Exception as error:
                raise HTTPException(404, detail=str(error))

    async def delete_user(self, user_id: int):
        async with async_session() as session:
            try:
                await session.execute(delete(User).where(User.id == user_id))
                await session.commit()
            except Exception as error:
                raise HTTPException(404, detail=str(error))

    async def list_user(self):
        async with async_session() as session:
            try:
                result = await session.execute(select(User))
                return result.scalars().all()
            except Exception as error:
                raise HTTPException(404, detail=str(error))

    async def get_by_id(self, user_id):
        async with async_session() as session:
            try:
                result = await session.execute(select(User).where(User.id == user_id))
                return result.scalar()
            except Exception as error:
                raise HTTPException(404, detail=str(error))


class FavoriteService:
    async def add_favorite(self, user_id: int, symbol: str):
        async with async_session() as session:
            try:
                session.add(Favorite(user_id=user_id, symbol=symbol))
                await session.commit()
            except Exception as error:
                raise HTTPException(404, detail=str(error))

    async def delete_favorite(self, user_id: int, symbol: str):
        async with async_session() as session:
            try:
                await session.execute(delete(Favorite).where(Favorite.user_id == user_id, Favorite.symbol == symbol))
                await session.commit()
            except Exception as error:
                raise HTTPException(404, detail=str(error))


class AssetService:
    async def day_summary(self, symbol: str):
        async with ClientSession() as session:
            try:
                yesterday = date.today() - timedelta(days=1)
                url = f'https://www.mercadobitcoin.net/api/{symbol}/day-summary/{yesterday.year}/{yesterday.month}/{yesterday.day}/'
                response = await session.get(url)
                data = await response.json()
                return {
                    'highest': data['highest'],
                    'lowest': data['lowest'],
                    'symbol': symbol
                }
            except Exception as error:
                raise HTTPException(404, detail=str(error))
