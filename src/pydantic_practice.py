from src.schemas import InvoiceItem, Invoice


invoice_1_item1 = InvoiceItem(description="Python Course", price=150)
invoice_1_item2 = InvoiceItem(description="Web Development", price=200)
invoice_1 = Invoice(
                    invoice_number="1", 
                    company="Barhoomz Education",
                    customer="Barhoomz",
                    items=[invoice_1_item1, invoice_1_item2],
                    total=invoice_1_item1.price + invoice_1_item2.price,
                    payment_status="Done"
)


print(invoice_1)