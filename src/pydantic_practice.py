# from src.schemas import InvoiceItem, Invoice


# invoice_1_item1 = InvoiceItem(description="Python Course", price=150)
# invoice_1_item2 = InvoiceItem(description="Web Development", price=200)
# invoice_1 = Invoice(
#                     invoice_number="1", 
#                     company="Barhoomz Education",
#                     customer="Barhoomz",
#                     items=[invoice_1_item1, invoice_1_item2],
#                     total=invoice_1_item1.price + invoice_1_item2.price,
#                     payment_status="Done"
# )


# print(invoice_1)

from src.schemas import Invoice, InvoiceItem
from pydantic import ValidationError

try:
    item1 = InvoiceItem(
        description="Python Course",
        price=150
    )

    item2 = InvoiceItem(
        description="Web Development",
        price=200
    )

    invoice = Invoice(
        invoice_number="INV-004",
        company="Barhoomz Education",
        customer="Ahmed Ali",
        items=[item1, item2],
        total=359,
        payment_status="Paid"
    )

    print(invoice)

except ValidationError as error:
    print("Validation failed!")
    print(error)