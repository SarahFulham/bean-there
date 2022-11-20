from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.ext.mutable import MutableDict

import database

class Cafe(database.Base):
    __tablename__ = "cafes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    features = Column(MutableDict.as_mutable(JSONB))
    images = Column(ARRAY(String))
