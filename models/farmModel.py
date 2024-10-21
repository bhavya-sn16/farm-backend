from pydantic import BaseModel, Field, PydanticUserError


class SensorData(BaseModel):
    id : str
    time: str
    humidity: float
    temperature: float
    EC: float
    PH: float
    N: float
    P: float
    K: float
    power: float