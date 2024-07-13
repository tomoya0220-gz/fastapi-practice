# Pydanticライブラリからインポートされる基本クラス。Pydanticモデルの基礎となるクラスで、データの検証やシリアライズに使用される。
from pydantic import BaseModel

# ItemBaseクラスはBaseModelを継承している。このクラスは、アイテムの基本的な属性を定義する。
class ItemBase(BaseModel):
  # name属性は文字列型として定義
  name: str
  # description属性も文字型として定義
  description: str

# ItemCreateクラスはItemBaseを継承する。このクラスはアイテムの作成時に使用され、ItemBaseと同じ属性を持つが、追加の属性やメソッドを持たない。
class ItemCreate(ItemBase):
  # passキーワードは、このクラスに追加の属性やメソッドがないことを示します。
  pass

# ItemクラスはItemBaseを継承をしている。このクラスはデータベースから取得したアイテムを表し、ItemBaseの属性に加えてID属性を持つ。
class Item(ItemBase):
  # id属性は整数型として定義。
  id: int

# Configクラスは、Pydanticモデルの設定を行うための内部クラス
class Config:
  # orm_mode属性をTrueに設定することで、PydanticモデルがORMモデルと互換性を持つようになる。これにより、ORMモデルからPydanticモデルへの自動変換が可能になる。
  orm_mode = True