from orm.database import Base
from sqlalchemy import Integer,String,Boolean,text
from sqlalchemy.orm import mapped_column,Mapped

class PostCreate(Base):
    __tablename__ = "orm_posts"

    id :Mapped[int]= mapped_column(Integer,primary_key=True,nullable=False,index=True)
    title :Mapped[str]= mapped_column(String,nullable=False)
    content :Mapped[str]= mapped_column(String,nullable=False)
    published :Mapped[bool]= mapped_column(Boolean,server_default=text("True"))

