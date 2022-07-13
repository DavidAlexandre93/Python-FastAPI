from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def raiz():
    return {"msg": "FastAPI Curso"}


if __name__ == '__main__':
    import uvicorn

    # com o host 0.0.0.0, qualquer pessoa com seu ip e porta 8000 consegue acessar seu endpoints na mesma rede sua
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
