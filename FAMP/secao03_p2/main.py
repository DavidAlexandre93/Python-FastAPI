from fastapi import FastAPI

from routes import curso_router
from routes import usuario_router

app = FastAPI()

app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])

if __name__ == '__main__':
    import uvicorn

    # com o host 0.0.0.0, qualquer pessoa com seu ip e porta 8000 consegue acessar seu endpoints na mesma rede sua
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", debug=True, reload=True)
