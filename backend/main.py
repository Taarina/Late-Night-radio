from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# DATABASE
# -----------------------------
DATABASE_URL = "sqlite:///./late_night_radio.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# -----------------------------
# MODELS
# -----------------------------
class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)


class Thought(Base):
    __tablename__ = "thoughts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

# Create DB Tables
Base.metadata.create_all(bind=engine)

# -----------------------------
# REQUEST MODELS
# -----------------------------
class VisitorCreate(BaseModel):
    name: str

class ThoughtCreate(BaseModel):
    text: str

# -----------------------------
# ROUTES
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Late Night Radio Backend Running"
    }

@app.post("/visitors")
def create_visitor(visitor: VisitorCreate):
    db = SessionLocal()

    try:
        new_visitor = Visitor(name=visitor.name)

        db.add(new_visitor)
        db.commit()
        db.refresh(new_visitor)

        return {
            "success": True,
            "visitor": {
                "id": new_visitor.id,
                "name": new_visitor.name
            }
        }

    finally:
        db.close()

@app.post("/thoughts")
def create_thought(thought: ThoughtCreate):
    db = SessionLocal()

    try:
        new_thought = Thought(text=thought.text)

        db.add(new_thought)
        db.commit()
        db.refresh(new_thought)

        return {
            "success": True,
            "thought": {
                "id": new_thought.id,
                "text": new_thought.text
            }
        }

    finally:
        db.close()

@app.get("/thoughts")
def get_thoughts():
    db = SessionLocal()

    try:
        thoughts = db.query(Thought).all()

        return [
            {
                "id": thought.id,
                "text": thought.text
            }
            for thought in thoughts
        ]

    finally:
        db.close()
