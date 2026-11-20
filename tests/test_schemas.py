
import pytest
from pydantic import ValidationError

from src.schemas import Invoice, InvoiceItem


def test_valid_invoice():
    item1 = InvoiceItem(
        description="Python Course",
        price=150
    )

    item2 = InvoiceItem(
        description="Web Development",
        price=200
    )

    invoice = Invoice(
        invoice_number="INV-001",
        company="Barhoomz Education",
        customer="Ahmed Ali",
        items=[item1, item2],
        total=350,
        payment_status="Paid"
    )

    assert invoice.total == 350
    assert invoice.customer == "Ahmed Ali"


def test_invalid_invoice_total():
    item1 = InvoiceItem(
        description="Python Course",
        price=150
    )

    item2 = InvoiceItem(
        description="Web Development",
        price=200
    )

    with pytest.raises(ValidationError):
        Invoice(
            invoice_number="INV-002",
            company="Barhoomz Education",
            customer="Ahmed Ali",
            items=[item1, item2],
            total=400,
            payment_status="Paid"
        )

def test_empty_invoice_items():
    with pytest.raises(ValidationError):
        invoice = Invoice(
                    invoice_number="INV-001",
                    company="Barhoomz Education",
                    customer="Ahmed Ali",
                    items=[],
                    total=350,
                    payment_status="Paid"
                )

def test_missing_customer():
    with pytest.raises(ValidationError):
        Invoice(
            invoice_number="INV-004",
            company="Barhoomz Education",
            items=[
                InvoiceItem(
                    description="Python Course",
                    price=150
                )
            ],
            total=150,
            payment_status="Paid"
        )

def test_negative_item_price():
    with pytest.raises(ValidationError):
        InvoiceItem(
            description="Python Course",
            price=-150
        )