from pydantic import BaseModel, Field
class NewsModel(BaseModel):
    title: str = Field(...)
    link: str = Field(...)
    published: str = Field(...)
    description: str = Field(...)
    source: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "City en la mira de la FIFA",
                "link": "https://www.futbolya.com/noticias/2019/02/23/rumor-city-en-la-mira-de-la-fifa/009158",
                "published": "2019-02-23 07:00:00",
                "description": "",
                "language":"es",
            }
        }

class UserModel(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
