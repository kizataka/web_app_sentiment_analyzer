from sqlalchemy.orm import Session
from sql_app import models

def create_comment(db: Session, text: str, sentiment: str, sentiment_score: float):
    # 新しいコメントオブジェクトを作成
    db_comment = models.Comment(text=text, sentiment=sentiment, sentiment_score=sentiment_score)
    db.add(db_comment)  # セッションにコメントオブジェクトを追加
    db.commit()  # トランザクションをコミット
    db.refresh(db_comment)  # コメントオブジェクトをリフレッシュして、データベースの任意の新しい状態を反映
    return db_comment  # 新しいコメントオブジェクトを返す

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    # ページネーションを使用してコメントのリストを取得
    # skipパラメータは、結果セットの開始位置を指定
    # limitパラメータは、返される項目の最大数を指定
    return db.query(models.Comment).offset(skip).limit(limit).all()

def get_comment(db: Session, comment_id: int):
    # 指定されたIDを持つコメントを取得
    # もしコメントが存在しない場合はNoneを返す
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()