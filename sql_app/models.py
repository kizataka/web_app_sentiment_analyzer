from sqlalchemy import Column, Integer, String, DateTime, Float, func
from sql_app.database import Base

class Comment(Base):
    __tablename__ = "comments"  # テーブル名を指定
    id = Column(Integer, primary_key=True, index=True)  # 主キーとしてのID
    text = Column(String, index=True)  # コメントテキスト
    sentiment = Column(String, index=True)  # 感情分析の結果（'positive'または'negative'）
    sentiment_score = Column(Float, index=True)  # ポジティブ度合いの数値
    created_at = Column(DateTime(timezone=True), default=func.now())  # コメントの作成日時