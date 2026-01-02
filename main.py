from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import router as userRoutes
from routes.projects import router as projectRoutes
from routes.files import router as filesRoutes
from routes.files import router as chatsRoutes

# Create FastAPI app
app = FastAPI(
    title="Six-Figure AI Engineering API",
    description="Backend API for Six-Figure AI Engineering application",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userRoutes, prefix="/api")
app.include_router(projectRoutes, prefix="")
app.include_router(filesRoutes, prefix="")
app.include_router(chatsRoutes, prefix="")