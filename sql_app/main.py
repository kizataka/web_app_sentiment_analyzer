from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sql_app.sentiment_analysis import analyze_sentiment
from sql_app import models, crud, schemas, database
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# SQLAlchemyセッションを取得する依存関係
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def read_root():
    return {'message': 'Welcome to the sentiment analysis app!'}

@app.post('/analyze_sentiment/', response_model=schemas.SentimentResponse)
async def analyze_sentiment_endpoint(request: schemas.SentimentRequest):
    text = request.text
    analysis_result = analyze_sentiment(text)
    return analysis_result