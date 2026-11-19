INVOICE_EXAMPLE = """
Invoice:
Invoice Number: INV-001
Company: ABC Technologies
Customer: John Smith
Total: $350
Payment Status: Paid

Expected JSON:
{
    "invoice_number": "INV-001",
    "company": "ABC Technologies",
    "customer": "John Smith",
    "total": 350,
    "payment_status": "Paid"
}
"""

INVOICE_PROMPT = """
You are an invoice data extraction assistant.

Your task is to extract structured information
from the invoice provided below.

Extract:
- Invoice number
- Company
- Customer
- Items
- Total
- Payment status

Follow the format demonstrated in this example:

{example}


Invoice:
{invoice_text}

Do not invent missing information.
"""


def build_invoice_prompt(invoice_text):
    return INVOICE_PROMPT.format(
        example=INVOICE_EXAMPLE,
        invoice_text = invoice_text
    )

