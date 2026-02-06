from question_loader import load_and_select_questions
from round_formatter import build_rounds_output, build_appendix_output
from grammar_checker import check_grammar
from export_grammar_pdf import export_grammar_pdf
from export_to_word import export_rounds_to_word
from export_to_pdf import export_rounds_to_pdf
import random
import numpy as np

# -----------------------------
DIVISION = "Junior"
YEAR = 2026
SEEDING_ROUNDS = 5
ELIMINATION_ROUNDS = 2
QUESTIONS_PER_ROUND = 24
CSV_PATH = "data/Catholic Quizbowl of North Carolina Questions - Junior.csv"
OUTPUT_TYPE = "pdf"
SEED = 20260206

random.seed(SEED)
np.random.seed(SEED)
# -----------------------------

total_rounds = SEEDING_ROUNDS + ELIMINATION_ROUNDS
total_needed = total_rounds * QUESTIONS_PER_ROUND

df, full_df = load_and_select_questions(
    csv_path=CSV_PATH,
    target_year=YEAR,
    total_needed=total_needed,
    seed=SEED
)

issues = check_grammar(df)
if issues:
    print("Grammar/Spelling Issues Found")
    export_grammar_pdf(issues, filename="GrammarReport.pdf")

output = build_rounds_output(
    df=df,
    division=DIVISION,
    seeding_rounds=SEEDING_ROUNDS,
    elimination_rounds=ELIMINATION_ROUNDS,
    questions_per_round=QUESTIONS_PER_ROUND
)

# -----------------------------
# APPENDIX OF 10 EXTRA QUESTIONS
# -----------------------------
remaining_df = full_df.drop(df.index)
appendix_df = remaining_df.sample(10, random_state=SEED)
appendix_text = build_appendix_output(appendix_df)
output = output + "\n\n===PAGEBREAK===\n\n" + appendix_text

# -----------------------------
# OUTPUT FORMATS
# -----------------------------
if OUTPUT_TYPE in ("word", "both"):
    export_rounds_to_word(output, division=DIVISION, filename="QuizRounds.docx")

if OUTPUT_TYPE in ("pdf", "both"):
    export_rounds_to_pdf(output, division=DIVISION, filename="QuizRounds.pdf")

print("Generated Output Files")