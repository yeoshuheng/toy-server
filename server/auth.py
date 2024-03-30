from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

VALID_API_KEY = "1234"
    
api_key_header = APIKeyHeader(name="X-API-KEY")

def check_key(poss_valid_key : str):
    print(poss_valid_key)
    return VALID_API_KEY == poss_valid_key

def authenticate(api_key_header: str = Security(api_key_header)) :
    print(api_key_header)
    if check_key(api_key_header):
        return True
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Invalid or missing API key"
    )