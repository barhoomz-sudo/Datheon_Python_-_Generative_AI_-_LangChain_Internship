import pytest
from unittest.mock import MagicMock, patch
from types import SimpleNamespace
from pydantic import ValidationError

from src.extarctor import extract_invoice


def test_successful_invoice_extraction(monkeypatch):

    # Give our application a fake API key
    monkeypatch.setenv("GEMENAI_API", "fake-api-key")

    # Create a fake Gemini response
    fake_response = SimpleNamespace(
        text="""
        {
            "invoice_number": "INV-005",
            "company": "Barhoomz Education",
            "customer": "Ahmed Ali",
            "items": [
                {
                    "description": "Python Course",
                    "price": 150
                }
            ],
            "total": 150,
            "payment_status": "Paid"
        }
        """
    )

    # Create a fake Gemini client
    fake_client = MagicMock()

    fake_client.models.generate_content.return_value = fake_response

    # Replace the real Gemini client with our fake client
    with patch("src.extarctor.genai.Client", return_value=fake_client):

        invoice = extract_invoice("Python Course - $150")

    # Check the extracted invoice
    assert invoice.invoice_number == "INV-005"
    assert invoice.customer == "Ahmed Ali"
    assert invoice.total == 150

    # Check that the client was closed
    fake_client.close.assert_called_once()


def test_empty_invoice_text(monkeypatch):

    monkeypatch.setenv("GEMENAI_API", "fake-api-key")

    with patch("src.extarctor.genai.Client") as mock_client:

        with pytest.raises(
            ValueError,
            match="Invoice text cannot be empty!"
        ):
            extract_invoice("")

        mock_client.assert_not_called()


def test_invalid_gemini_response(monkeypatch):

    monkeypatch.setenv("GEMENAI_API", "fake-api-key")

    fake_response = SimpleNamespace(
        text="""
        {
            "invoice_number": "INV-006",
            "company": "Barhoomz Education",
            "customer": "Ahmed Ali",
            "items": [
                {
                    "description": "Python Course",
                    "price": 150
                }
            ],
            "total": 400,
            "payment_status": "Paid"
        }
        """
    )

    fake_client = MagicMock()
    fake_client.models.generate_content.return_value = fake_response

    with patch("src.extarctor.genai.Client", return_value=fake_client):

        with pytest.raises(ValidationError):
            extract_invoice("Python Course - $150")

        fake_client.close.assert_called_once()
