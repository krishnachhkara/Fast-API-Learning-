from database import Base
from sqlalchemy import Column,Integer,String,Boolean

class PostCreate(Base):
    __tablename__ = "orm_posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,default=True)

    