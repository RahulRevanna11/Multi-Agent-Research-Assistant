from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


def text_to_pdf(text: str, output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=20,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=16,
        spaceAfter=10
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontSize=11,
        leading=16,
        spaceAfter=10
    )

    content = []

    lines = text.strip().split("\n")

    for line in lines:
        line = line.strip()

        if not line:
            content.append(Spacer(1, 0.15 * inch))
            continue

        # Main title (first #)
        if line.startswith("# ") and not content:
            content.append(
                Paragraph(f"<b>{line[2:]}</b>", title_style)
            )

        # Section headings (##)
        elif line.startswith("## "):
            content.append(
                Paragraph(f"<b>{line[3:]}</b>", heading_style)
            )

        # Normal paragraph
        else:
            content.append(
                Paragraph(line, body_style)
            )

    doc.build(content)
