import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import ValidationError

from src.schemas import Invoice
from src.prompts import build_invoice_prompt


def extract_invoice(invoice_text: str) -> Invoice:
    load_dotenv()

    api_key = os.getenv("GEMENAI_API")

    if not api_key:
        raise ValueError("Gemini API key not found!")

    if not invoice_text.strip():
        raise ValueError("Invoice text cannot be empty!")

    client = genai.Client(api_key=api_key)

    try:
        prompt = build_invoice_prompt(invoice_text)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=Invoice
            )
        )

        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        invoice = Invoice.model_validate_json(response.text)

        return invoice

    finally:
        client.close()
