from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def create_receipt(transaction_id, date, items, total_amount, customer_name, receipt_filename):
    c = canvas.Canvas(receipt_filename, pagesize=letter)
    width, height = letter

    # Title
    # Change this line
    c.setFont("Helvetica-Oblique", 12)  # instead of "Helvetica-Italic"

    c.drawCentredString(width / 2.0, height - inch, "Payment Receipt")

    # Transaction details
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(1 * inch, height - 1.5 * inch, f"Transaction ID: {transaction_id}")
    c.drawString(1 * inch, height - 1.75 * inch, f"Date: {date}")
    c.drawString(1 * inch, height - 2 * inch, f"Customer Name: {customer_name}")

    # Itemized list
    c.drawString(1 * inch, height - 2.5 * inch, "Items Purchased:")
    y_position = height - 3 * inch
    for item, price in items:
        c.drawString(1.5 * inch, y_position, f"{item}: ${price:.2f}")
        y_position -= 0.25 * inch

    # Total amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, y_position - 0.25 * inch, f"Total Amount: ${total_amount:.2f}")

    # Thank you note
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2.0, y_position - 1 * inch, "Thank you for your purchase!")

    # Save PDF
    c.showPage()
    c.save()


# Example usage
transaction_id = "123456789"
date = "2024-07-12"
items = [("Item A", 10.00), ("Item B", 20.00), ("Item C", 30.00)]
total_amount = sum(price for item, price in items)
customer_name = "John Doe"
receipt_filename = "receipt.pdf"

create_receipt(transaction_id, date, items, total_amount, customer_name, receipt_filename)
