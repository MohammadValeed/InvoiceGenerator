from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# Sample invoice data
customer_name = "Valeed"
invoice_number = "INV001"
invoice_date = datetime.now().strftime('%Y-%m-%d')
items = [
    {"description": "Product 1", "quantity": 2, "price": 50.0},
    {"description": "Product 2", "quantity": 1, "price": 30.0},
    {"description": "Service 1", "quantity": 3, "price": 100.0}
]

# Calculate total amount
total_amount = sum(item["quantity"] * item["price"] for item in items)

# Create a PDF invoice
def create_invoice(pdf_filename):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Define the content for the PDF
    content = []

    # Add a title
    title_style = getSampleStyleSheet()["Title"]
    title = Paragraph("Invoice", style=title_style)
    content.append(title)

    # Add customer information
    customer_info_style = getSampleStyleSheet()["Normal"]
    customer_info = Paragraph(f"Customer: {customer_name}<br/>Invoice Number: {invoice_number}<br/>Invoice Date: {invoice_date}", style=customer_info_style)
    content.append(customer_info)

    # Create a table for the invoice items
    item_data = [["Description", "Quantity", "Price", "Total"]]
    for item in items:
        description = item["description"]
        quantity = item["quantity"]
        price = item["price"]
        total = quantity * price
        item_data.append([description, quantity, f"${price:.2f}", f"${total:.2f}"])

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Create the table
    invoice_table = Table(item_data)
    invoice_table.setStyle(table_style)
    content.append(invoice_table)

    # Add the total amount
    total_style = getSampleStyleSheet()["Heading2"]
    total_text = Paragraph(f"<br/><b>Total Amount: ${total_amount:.2f}</b>", style=total_style)
    content.append(total_text)

    # Build the PDF
    doc.build(content)

if __name__ == "__main__":
    pdf_filename = "invoice.pdf"
    create_invoice(pdf_filename)
    print(f"Invoice saved as {pdf_filename}")
