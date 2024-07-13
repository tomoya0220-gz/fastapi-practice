# SQLAlchemyのデータベースセッションを管理するクラス。データベースへのクエリ実行やトランザクション管理を行う。
from sqlalchemy.orm import Session
from . import models, schemas

# 'get_item'関数を定義。この関数はデータベースから特定のアイテムを取得するためのもの
def get_item(db: Session, item_id: int):
  # 'db.query(models.Item)':'models.Item'テーブルに対するクエリを作成する。
  # '.filter(models.Item.id == item_id)':'item_id'に一致するレコードをフィルタリングする。
  # '.first()':フィルタリングされたレコードの最初の１件を返す。
  return db.query(models.Item).filter(models.Item.id == item_id).first()

# 'get_items'関数を定義。データベースから複数のアイテムを取得するためのもの
def get_items(db: Session, skip: int = 0, limit: int = 10):
  # 'db.query(models.Item)': 'models.Item'テーブルに対するクエリを作成。
  # '.offset(skip)': クエリ結果をskipだけスキップする。
  # '.all()':クエリ結果のすべてのレコードをリストとして返す。
  return db.query(models.Item).offset(skip).limit(limit).all()

# 'create_item'関数を定義。この関数はデータベースに新しいアイテムを作成するためのもの
def create_item(db: Session, item: schemas.ItemCreate):
  # 'models.Item'クラスを使用して新しいアイテムインスタンス'db_item'を作成
  db_item = models.Item(name=item.name, description=item.description)
  # 'db_item'をセッションに追加する
  db.add(db_item)
  # トランザクションをコミットして、データベースに変更を永続化する。
  db.commit()
  # データベースから最新のデータを取得して'db_item'インスタンスを更新する
  db.refresh(db_item)
  # 作成したアイテムを返す。
  return db_item

# データベースに対するCRUD操作を実装する関数を定義する。特定のアイテムを取得する'get_item'関数、
# 複数のアイテムを取得する'get_items'関数、新しいアイテムを作成する'create_item'関数を定義する。
# これらの関数は'models'モジュールのデータベースモデルと'schemas'モジュールのPydanticスキーマを
# 使用して、データベース操作を行う。