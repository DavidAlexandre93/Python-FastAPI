from fastapi import APIRouter
from asyncio import gather
from typing import List
from service.services import UserService, FavoriteService, AssetService
from model.schemas import (
    UserCreateInput, StandardOutput, AlternativeOutput, UserFavoriteAddInput, UserListOutput, DaySummaryOutput
)

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create', description='EndPoint Create Users', response_model=StandardOutput,
                  responses={404: {'model': AlternativeOutput}})
async def user_create(user_input: UserCreateInput):
    await UserService.create_user(name=user_input.name)
    return StandardOutput(message='Ok')


@user_router.delete('/delete/{user_id}', description='EndPoint Delete User', response_model=StandardOutput,
                    responses={404: {'model': AlternativeOutput}})
async def user_delete(user_id: int):
    await UserService.delete_user(user_id)
    return StandardOutput(message='Ok')


@user_router.post('/favorite/add', description='EndPoint Add Favorite', response_model=StandardOutput,
                  responses={404: {'model': AlternativeOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
    return StandardOutput(message='Ok')


@user_router.delete('/favorite/delete/{user_id}', description='EndPoint Delete Favorite', response_model=StandardOutput,
                    responses={404: {'model': AlternativeOutput}})
async def user_delete_favorite(user_id: int, symbol: str):
    await FavoriteService.delete_favorite(user_id=user_id, symbol=symbol)
    return StandardOutput(message='Ok')


@user_router.get('/list', description='EndPoint List Users and yours favorites', response_model=List[UserListOutput],
                 responses={404: {'model': AlternativeOutput}})
async def user_list():
    return await UserService.list_user()


@assets_router.get('/day_summary/{user_id}', description='EndPoint List Symbol and value yesterday',
                   response_model=List[DaySummaryOutput],
                   responses={404: {'model': AlternativeOutput}})
async def day_summary(user_id: int):
    user = await UserService.get_by_id(user_id)
    favorites_symbols = [favorite.symbol for favorite in user.favorites]
    tasks = [AssetService.day_summary(symbol=symbol) for symbol in favorites_symbols]
    return await gather(*tasks)
