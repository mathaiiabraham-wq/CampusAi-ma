from fastapi import HTTPException, status


class CampusAIException(Exception):
    """Base exception for CampusAI"""
    pass


class QueryProcessingError(CampusAIException):
    """Raised when query processing fails"""
    pass


class LLMError(CampusAIException):
    """Raised when LLM inference fails"""
    pass


class ChromaDBError(CampusAIException):
    """Raised when ChromaDB operations fail"""
    pass


class KnowledgeBaseError(CampusAIException):
    """Raised when knowledge base operations fail"""
    pass


class ValidationError(CampusAIException):
    """Raised when input validation fails"""
    pass


def raise_http_exception(status_code: int, detail: str):
    """Raise HTTP exception with consistent format"""
    raise HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "error": detail.split(":")[0] if ":" in detail else "Error",
            "message": detail
        }
    )
