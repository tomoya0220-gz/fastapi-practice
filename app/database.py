# 'create_engine':SQLAlchemyの関数で、データベースへの接続を管理するエンジンを作成する
from sqlalchemy import create_engine
# 'declarative_base':SQLAlchemyの関数で、データベースモデルの基底クラスを作成する。この基底クラスを使用してデータベーステーブルを定義する。
from sqlalchemy.ext.declarative import declarative_base
# 'sessionmaker':SQLAlchemyの関数で、データベースセッションのクラスを作成する。このクラスを使用してデータベースとのセッションを管理する。
from sqlalchemy.orm import sessionmaker

# DATABASE_URL:データベース接続文字列・MySQLデータベースに接続するための情報が含まれている。
DATABASE_URL = "mysql://fastapi_user:password@db/fastapi_test"

# データベースエンジンを作成。このエンジンを使用してデータベースへの接続を管理する。'engine':作成されたデータベースエンジンのインスタンス
engine = create_engine(DATABASE_URL)
# データベースセッションを作成するクラスを定義する。
# 'autocommit=False':トランザクションを自動的にコミットしない設定。
# 'autoflush=False':セッションがフラッシュされる（変更がデータベースに書き込まれる）タイミングを制御する設定。
# 'bind=engine':作成されたエンジンにセッションをバインド（関連付け）する
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 'declarative_base()':データベースモデルの基底クラスを作成。この基底クラスを使用してデータベーステーブルを定義する。
Base = declarative_base()

# SQLAlchemyを使用してデータベースとの接続を管理するための設定を行う。
# このファイルでは、データベースエンジンの作成、セッションの設定、モデルの基底クラスの定義、
# そしてデータベースセッションを取得するための関数を定義する。