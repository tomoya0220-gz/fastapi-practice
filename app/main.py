from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from . database import SessionLocal, engine

# データベースのテーブルを作成する。`engine`を使用して、`models.Base`で定義されたすべてのテーブルをデータベースに作成。
models.Base.metadata.create_all(bind=engine)

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# データベースセッションを取得する依存関係を定義する関数。
def get_db():
  # 新しいデータベースセッションを作成
  db = SessionLocal()
  try:
    # セッションを返す
    yield db
  # セッションの使用が終わった後にセッションを閉じる
  finally:
    db.close()

# エンドポイントに対するPOSTリクエストを処理するエンドポイントを定義
@app.post("/items/", response_model=schemas.Item)
  # リクエストボディとして’ItemCreate’スキーマを使用、データベースセッションを依存関係として注入
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    # 'crud'モジュールの'create_item'関数を呼び出してアイテムを作成し、その結果を返す。
    return crud.create_item(db=db, item=item)

# '/items/{item_id}'エンドポイントに対するGETリクエストを処理するエンドポイントを定義。レスポンスのスキーマとしてschemas.Itemを使用
@app.get("/items/{item_id}", response_model=schemas.Item)
# URLパスパラメータとしてアイテムIDを受け取る。データベースセッションを依存関係として注入。
def read_item(item_id: int, db: Session = Depends(get_db)):
  # crudモジュールの'get_item'関数を呼び出してアイテムを取得
  db_item = crud.get_item(db, item_id=item_id)
  # db_itemが依存しなし場合、HTTP 404エラーを発生させる
  if db_item is None:
    raise HTTPException(status_code=404, detail="Item not found")
  # 取得したアイテムを返す。
  return db_item

# '/items/'エンドポイントに対するGETリクエストを処理するエンドポイントを定義。レスポンスのスキーマとして'schemas.Item'のリストを使用
@app.get("/items/", response_model=List[schemas.Item])
# クエリパラメータとしてスキップ・取得するアイテム数を受け取る。データベースセッションを依存関係として注入。
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  # 'crud'モジュールの'get_item'関数を呼び出してアイテムのリストを取得。
  items = crud.get_items(db, skip=skip, limit=limit)
  # 取得したアイテムのリストを返す。
  return items
