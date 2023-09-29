from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    sentiment: str
    sentiment_score: float
    created_at: datetime  

    class Config:
        orm_mode = True

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    sentiment_score: float