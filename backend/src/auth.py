import os
from hmac import compare_digest
from fastapi import Header, HTTPException
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=500, detail="API key is required")

    if not compare_digest(x_api_key, API_KEY):
        raise HTTPException(status_code=403, detail="Invalid API key")
