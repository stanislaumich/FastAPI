import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, Base
from routers import user as UserRouter
from routers import auth as AuthRouter
from routers import static as StaticRouter
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]
#app.mount("/static", StaticFiles(directory="static", html=True))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(StaticRouter.router, prefix='')
app.include_router(UserRouter.router, prefix='/api/user')
app.include_router(AuthRouter.router, prefix='/auth')


#app.mount("/", StaticFiles(directory="static", html=True))


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=2)