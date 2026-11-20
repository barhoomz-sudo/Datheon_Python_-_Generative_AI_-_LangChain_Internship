from pydantic import BaseModel, model_validator, Field

class InvoiceItem(BaseModel):
    description: str
    price: float = Field(gt=0)

class Invoice(BaseModel):
    invoice_number: str
    company: str
    customer: str
    items: list[InvoiceItem]
    total: float
    payment_status: str

    @model_validator(mode='after')
    def check_total(self):
        items_total = sum(item.price for item in self.items)

        if self.total != items_total:
            raise ValueError(f"Invoice total ({self.total}) does not match "
    f"the sum of items ({items_total}).")
        return self

    @model_validator(mode="after")
    def check_items(self):
        if not self.items:
            raise ValueError("Invoice must contain at least one item!")
        return self




