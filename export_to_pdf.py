from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch

def export_rounds_to_pdf(text_output, division, filename="QuizRounds.pdf"):
    styles = getSampleStyleSheet()

    # Basic styles
    h1 = ParagraphStyle("Heading1", parent=styles["Heading1"], spaceAfter=12)
    h2 = ParagraphStyle("Heading2", parent=styles["Heading2"], spaceAfter=6)
    normal = styles["BodyText"]

    # Create PDF
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    story = []

    # ---------------------------------------------------------
    # TITLE PAGE (simple, clean)
    # ---------------------------------------------------------
    story.append(Paragraph("Catholic Quiz Bowl of North Carolina", styles["Title"]))
    story.append(Spacer(1, 36))
    story.append(Paragraph(f"{division} Questions", styles["Title"]))
    story.append(Spacer(1, 36))
    story.append(PageBreak())
    
    # ---------------------------------------------------------
    # MAIN CONTENT
    # ---------------------------------------------------------
    lines = text_output.split("\n")

    for line in lines:
        stripped = line.strip()

        if stripped == "":
            story.append(Spacer(1, 6))
            continue

        # Skip division title lines so they don't appear before Round One 
        if stripped.lower() in [ 
            f"{division.lower()} questions", 
            f"{division.lower()} division questions" 
        ]: 
            continue

        # Page break marker for appendix
        if stripped == "===PAGEBREAK===":
            story.append(PageBreak())
            continue

        # Round titles
        is_round_title = stripped.startswith(f"{division} Round")
        is_elim_title = stripped.startswith(f"{division} ") and any(
            t in stripped for t in ["Finals", "Semifinals", "Quarterfinals"]
        )
        is_appendix = stripped.startswith("Appendix")

        if is_round_title or is_elim_title or is_appendix:
            story.append(Paragraph(stripped, h1))
            continue

        # Halftime
        if stripped == "HALFTIME":
            story.append(Paragraph(stripped, h2))
            continue

        # Normal text
        story.append(Paragraph(stripped, normal))

    # ---------------------------------------------------------
    # Build PDF (no page numbers, no headers)
    # ---------------------------------------------------------
    doc.build(story)