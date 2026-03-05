from question_loader import load_and_select_questions
from round_formatter import build_rounds_output
from grammar_checker import check_grammar
from export_grammar_pdf import export_grammar_pdf
from export_to_word import export_rounds_to_word
from export_to_pdf import export_rounds_to_pdf
import random
import numpy as np

# -----------------------------
DIVISION = "Senior"
YEAR = 2026
SEEDING_ROUNDS = 2
ELIMINATION_ROUNDS = 3
QUESTIONS_PER_ROUND = 24
CSV_PATH = f"data/Championship Questions 2026 - {DIVISION}.csv"
OUTPUT_TYPE = "pdf"
SEED = 20260228

random.seed(SEED)
np.random.seed(SEED)
# -----------------------------

total_rounds = SEEDING_ROUNDS + ELIMINATION_ROUNDS
total_needed = total_rounds * QUESTIONS_PER_ROUND

round_df, appendix_df = load_and_select_questions(
    csv_path=CSV_PATH,
    target_year=YEAR,
    total_needed=total_needed,
    seed=SEED
)

output = build_rounds_output(
    round_df,
    appendix_df,
    division=DIVISION,
    seeding_rounds=SEEDING_ROUNDS,
    elimination_rounds=ELIMINATION_ROUNDS,
    questions_per_round=QUESTIONS_PER_ROUND
)

issues = check_grammar(round_df)
if issues:
    print("Grammar/Spelling Issues Found")
    export_grammar_pdf(issues, filename=f"{DIVISION}GrammarReport.pdf")

# -----------------------------
# OUTPUT FORMATS
# -----------------------------
if OUTPUT_TYPE in ("word", "both"):
    export_rounds_to_word(output, division=DIVISION, filename=f"{DIVISION}QuizRounds.docx")

if OUTPUT_TYPE in ("pdf", "both"):
    export_rounds_to_pdf(output, division=DIVISION, filename=f"{DIVISION}QuizRounds.pdf")

print("Generated Output Files")