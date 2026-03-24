from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://root:0000@localhost:3306/flask_db")
Base = declarative_base()
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# 테이블 생성
Base.metadata.create_all(engine)

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

# Create
user = User(name="짱구", age=20)
session.add(user)
session.commit()

# Read
users = session.query(User).all()

for u in users:
    print(u.name)

# 조건 조회
user = session.query(User).filter(User.name == "짱구").first()

# Update
if user:
    user.name="수정된 이름"
    session.commit()

# Delete
if user:
    session.delete(user)
    session.commit()

# 세션 종료
session.close()