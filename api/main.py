from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.summarize import Summarizer
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI(title="AI Text Summarizer API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Model
class SummaryRequest(BaseModel):
    text: str
    ratio: float = 0.2
    algorithm: str = "abstractive"
    language: str = "auto"

# Initialize Summarizer
summarizer = Summarizer()

@app.post("/summarize")
async def summarize_text(request: SummaryRequest):
    try:
        if request.algorithm == "abstractive":
            summary = summarizer.abstractive_summarize(
                request.text, 
                max_length=int(len(request.text) * request.ratio))
        elif request.algorithm == "extractive":
            summary = summarizer.extractive_summarize(
                request.text,
                ratio=request.ratio
            )
        else:
            raise HTTPException(status_code=400, detail="Invalid algorithm")
        
        return {
            "summary": summary,
            "readability_score": summarizer.calculate_readability(summary),
            "processing_time": 0  # Implement timing logic
        }
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))