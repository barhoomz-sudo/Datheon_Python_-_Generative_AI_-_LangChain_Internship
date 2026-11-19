import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.schemas import Invoice
from src.prompts import build_invoice_prompt

load_dotenv()

api_key = os.getenv("GEMENAI_API")

if not api_key:
    raise ValueError("something went wrong.")
else:
    print("everything is great!")

client = genai.Client(api_key=api_key)

invoice_text = """
INVOICE

Invoice Number: INV-003
Company: Barhoomz Education
Customer: Ahmed Ali

Items:
Python Course - $150
Web Development - $200

Total: $350
Payment Status: Paid
"""

prompt = build_invoice_prompt(invoice_text)


response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Invoice
    )
)

invoice = Invoice.model_validate_json(response.text)

print(invoice)
client.close()