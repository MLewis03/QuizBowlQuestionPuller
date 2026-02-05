from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER

def export_rounds_to_pdf(text_output, division, filename="QuizRounds.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    halftime_style = styles["Heading3"]
    normal_style = styles["BodyText"]

    story = []

    # Title page
    story.append(Paragraph(f"{division} Questions", title_style))
    story.append(Spacer(1, 48))
    story.append(PageBreak())

    lines = text_output.split("\n")
    first_round_seen = False

    for line in lines:
        stripped = line.strip()
        if stripped == "":
            story.append(Spacer(1, 6))
            continue

        is_round_title = stripped.startswith(f"{division} Round")
        is_elim_title = stripped.startswith(f"{division} ") and any(
            t in stripped for t in ["Finals", "Semifinals", "Quarterfinals"]
        )
        is_title_page = stripped == f"{division} Division Questions"

        if is_title_page:
            # already handled as title page
            continue

        if is_round_title or is_elim_title:
            if first_round_seen:
                story.append(PageBreak())
            first_round_seen = True
            story.append(Paragraph(stripped, heading_style))
            story.append(Spacer(1, 12))
            continue

        if stripped == "HALFTIME":
            story.append(Spacer(1, 12))
            story.append(Paragraph(stripped, halftime_style))
            story.append(Spacer(1, 12))
            continue

        story.append(Paragraph(stripped, normal_style))

    doc.build(story)
