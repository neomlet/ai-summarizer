from pydantic import BaseModel

class SummaryRequest(BaseModel):
    text: str
    ratio: float = 0.2
    algorithm: str = "abstractive"
    language: str = "auto"
    temperature: float = 0.7

class SummaryResponse(BaseModel):
    summary: str
    readability_score: float
    processing_time: float
    algorithm: str
    original_length: int
    summary_length: int