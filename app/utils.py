import time
from typing import Dict, Any

def format_time(seconds: float) -> str:
    """Форматирование времени выполнения"""
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    return f"{seconds:.2f}s"

def validate_input(text: str) -> Dict[str, Any]:
    """Валидация входного текста"""
    errors = {}
    
    if len(text) < 100:
        errors["length"] = "Text must be at least 100 characters"
    
    if len(text) > 10000:
        errors["length"] = "Text exceeds maximum length (10,000 characters)"
    
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }