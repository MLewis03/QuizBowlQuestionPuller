from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER

def export_grammar_pdf(results, filename="GrammarReport.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph("Grammar & Spelling Report", styles["Title"])
    story.append(title)
    story.append(Spacer(1, 24))

    if not results:
        story.append(Paragraph("No issues found.", styles["BodyText"]))
        doc.build(story)
        return

    for entry in results:
        story.append(Paragraph(
            f"<b>Row {entry['row']} — {entry['column']}</b>",
            styles["Heading3"]
        ))
        story.append(Paragraph(entry["text"], styles["BodyText"]))
        story.append(Spacer(1, 12))

        for issue in entry["issues"]:
            story.append(Paragraph(f"• {issue['message']}", styles["BodyText"]))
            if issue["suggestions"]:
                story.append(Paragraph(
                    f"Suggestions: {', '.join(issue['suggestions'])}",
                    styles["BodyText"]
                ))
            story.append(Spacer(1, 6))

        story.append(Spacer(1, 18))

    doc.build(story)