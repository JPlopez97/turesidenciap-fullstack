from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Título de la factura
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Factura", 0, 1, "C")
        self.ln(10)

    def footer(self):
        # Pie de página
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, "Página %s" % self.page_no(), 0, 0, "C")
        pdf.ln(5)
        pdf.set_font("Arial", "B", 10)
        self.cell(0, 10, "TuResidenciApp", 0, 0, "C")

# Crear el PDF
pdf = PDF()
pdf.add_page()

# Información de la empresa
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Nombre de la Empresa", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.cell(0, 10, "Dirección de la Empresa", 0, 1)
pdf.cell(0, 10, "Teléfono: +57 1234567890", 0, 1)
pdf.cell(0, 10, "Correo: empresa@correo.com", 0, 1)
pdf.ln(10)

# Información del cliente
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Información del Cliente", 0, 1)
pdf.set_font("Arial", "", 10)
pdf.cell(0, 10, "Nombre: Juan Pérez", 0, 1)
pdf.cell(0, 10, "Dirección: Calle Falsa 123", 0, 1)
pdf.cell(0, 10, "Teléfono: +57 987654321", 0, 1)
pdf.ln(10)

# Tabla de productos/servicios
pdf.set_font("Arial", "B", 10)
pdf.cell(60, 10, "Descripción", 1, 0, "C")
pdf.cell(40, 10, "Cantidad", 1, 0, "C")
pdf.cell(40, 10, "Precio Unitario", 1, 0, "C")
pdf.cell(40, 10, "Total", 1, 1, "C")

# Detalles de los productos/servicios
productos = [
    {"descripcion": "Producto 1", "cantidad": 2, "precio_unitario": 5000},
    {"descripcion": "Producto 2", "cantidad": 1, "precio_unitario": 3000},
    {"descripcion": "Producto 3", "cantidad": 5, "precio_unitario": 2000},
]

pdf.set_font("Arial", "", 10)
total_factura = 0

for producto in productos:
    descripcion = producto["descripcion"]
    cantidad = producto["cantidad"]
    precio_unitario = producto["precio_unitario"]
    total = cantidad * precio_unitario
    total_factura += total

    pdf.cell(60, 10, descripcion, 1, 0)
    pdf.cell(40, 10, str(cantidad), 1, 0, "C")
    pdf.cell(40, 10, f"${precio_unitario:,.2f}", 1, 0, "C")
    pdf.cell(40, 10, f"${total:,.2f}", 1, 1, "C")

# Total de la factura
pdf.set_font("Arial", "B", 10)
pdf.cell(140, 10, "Total a Pagar", 1, 0, "R")
pdf.cell(40, 10, f"${total_factura:,.2f}", 1, 1, "C")

# Guardar el archivo PDF
pdf.output("C:/Temp/factura_demo.pdf")