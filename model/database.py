from sqlalchemy import (create_engine, Column, Integer,
                        Text, DateTime, Boolean, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
from os import path
db_folder = path.dirname(path.abspath(__file__))
db_path = path.join(db_folder, 'rakusyoku.sqlite3')

# 接続先DBの設定
DATABASE = 'sqlite:///{}'.format(db_path)

# Engineの作成
Engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=False,
    connect_args={"check_same_thread": False}
)

Base = declarative_base()


class Product(Base):

    __tablename__ = 'product'

    _id = Column(Integer, primary_key=True, autoincrement=True)
    genre_id = Column(Integer)
    name = Column(Text)
    image = Column(Text)
    explanation = Column(Text)
    updated_at = Column(DateTime, onupdate=func.now())
    publish = Column(Boolean)
    recommend = Column(Boolean)
    sales = Column(Boolean)

    def to_dict(self):
        product = {
            "_id": self._id,
            "genre_id": self.genre_id,
            "name": self.name,
            "image": self.image,
            "publish": self.publish,
            "recommend": self.recommend,
            "sales": self.sales
        }
        if self.updated_at:
            product["updated_at"] = time.mktime(self.updated_at.timetuple)

        if self.explanation:
            product["explanation"] = self.explanation

        return product


def create_database():
    Base.metadata.create_all(bind=Engine)


def create_session():
    return sessionmaker(bind=Engine)()


if __name__ == "__main__":
    create_database()
