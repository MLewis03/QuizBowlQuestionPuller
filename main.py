from question_loader import load_and_select_questions
from round_formatter import build_rounds_output
from grammar_checker import check_grammar
from export_to_word import export_rounds_to_word
from export_to_pdf import export_rounds_to_pdf

# -----------------------------
DIVISION = "Junior"        # "Junior" or "Senior"
YEAR = 2026
SEEDING_ROUNDS = 5
ELIMINATION_ROUNDS = 2     # 1=Finals; 2=Semis+Finals; 3=Quarters+Semis+Finals
QUESTIONS_PER_ROUND = 24
CSV_PATH = "data/Questions_2025_Junior.csv"
# -----------------------------

total_rounds = SEEDING_ROUNDS + ELIMINATION_ROUNDS
total_needed = total_rounds * QUESTIONS_PER_ROUND

df = load_and_select_questions(
    csv_path=CSV_PATH,
    target_year=YEAR,
    total_needed=total_needed
)

issues = check_grammar(df)
if issues:
    print("Grammar/Spelling Issues Found:")
    for issue in issues:
        print(issue)
    print()

output = build_rounds_output(
    df=df,
    division=DIVISION,
    seeding_rounds=SEEDING_ROUNDS,
    elimination_rounds=ELIMINATION_ROUNDS,
    questions_per_round=QUESTIONS_PER_ROUND
)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(output)

export_rounds_to_word(output, division=DIVISION, filename="QuizRounds.docx")
export_rounds_to_pdf(output, division=DIVISION, filename="QuizRounds.pdf")

print("Generated: output.txt, QuizRounds.docx, QuizRounds.pdf")
