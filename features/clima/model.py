from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather_querys'  # Debe coincidir con el nombre real de la tabla

    id = Column(String, nullable=False, primary_key=True)
    source_query = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    region = Column(String, nullable=False)
    dateQuery = Column(Date, default=func.now())
    temp_c = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    humidity = Column(String, nullable=False)
    wind_kph = Column(String, nullable=False) 

