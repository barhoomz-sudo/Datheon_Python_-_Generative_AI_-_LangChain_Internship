from pathlib import Path
from src.extarctor import extract_invoice
from pydantic import ValidationError
from google.genai.errors import APIError


def main():
    invoice_path = Path("data/invoices/invoice.txt")
    try:
        if not invoice_path.exists():
            raise FileNotFoundError(
                f"Invoice file not found: {invoice_path}"
            )

        invoice_text = invoice_path.read_text(encoding="utf-8")

        invoice = extract_invoice(invoice_text)

        print("\n===== EXTRACTED INVOICE =====")
        print(f"Invoice Number: {invoice.invoice_number}")
        print(f"Company: {invoice.company}")
        print(f"Customer: {invoice.customer}")

        print("\nItems:")
        for item in invoice.items:
            print(f"- {item.description}: ${item.price:.2f}")

        print(f"\nTotal: ${invoice.total:.2f}")
        print(f"Payment Status: {invoice.payment_status}")

    except FileNotFoundError as error:
        print(f"File Error: {error}")

    except ValidationError as error:
        print(f"Validation Error: {error}")

    except APIError as error:
        print(f"Gemini API Error: {error}")

    except ValueError as error:
        print(f"Input Error: {error}")


if __name__ == "__main__":
    main()
