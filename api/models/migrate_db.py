# ココ！
from sqlalchemy import create_engine
from api.models.task import Base
DB_URL="mysql+pymysql://root@localhost:3306?charset=utf8"
engine=create_engine(DB_URL,echo=True)
def reset_databese():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.creat_all(bind=engine)

if __name__=="__main__":
    reset_databese()