from pydantic import BaseModel

class Postcreate(BaseModel):
    title: str
    content : str
    published : str

class PostResponse(Postcreate):
    id : int

    class config:
        from_attributes = True
