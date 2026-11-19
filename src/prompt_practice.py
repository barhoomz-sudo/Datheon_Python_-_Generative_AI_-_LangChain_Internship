from src.prompts import build_invoice_prompt

invoice = """
Invoice Number: INV-001
Company: ABC Technologies
Customer: John Smith
Total: $350
"""

prompt = build_invoice_prompt(invoice)

print(prompt)