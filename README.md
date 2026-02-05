# QuizBowlQuestionPuller

A modular Python tool for generating formatted quiz rounds (Junior or Senior division) from a CSV question bank. The system supports:

- Automatic filtering by year (e.g., pull all 2026 questions first)
- Random selection and shuffling of question pairs
- Configurable seeding rounds and elimination rounds
- Automatic round titles (Round One, Semifinals, Finals, etc.)
- Correct question numbering (1–12, HALFTIME, 13–24)
- Grammar and spelling checks using LanguageTool
- Export to Word (.docx) with page breaks and styled headings
- Export to PDF with a title page and clean formatting

This project is designed to produce moderator‑ready documents for academic competitions.

---------------------------------------------------------------------

## Repository Structure

quiz-generator/
│
├── main.py                 # Main entry point; sets parameters and runs the pipeline
├── question_loader.py      # Loads CSV, filters by year, selects random question pairs
├── round_formatter.py      # Builds formatted text output for all rounds
├── grammar_checker.py      # Flags spelling/grammar issues in questions
├── export_to_word.py       # Creates a styled .docx with page breaks
├── export_to_pdf.py        # Creates a PDF with a title page and page breaks
├── requirements.txt        # Python dependencies
│
└── data/
      └── Questions.csv

---------------------------------------------------------------------

## Installation

1. Install Python 3.9+
2. Install dependencies:

pip install -r requirements.txt

Dependencies include:
- pandas — CSV handling
- language-tool-python — grammar checking
- python-docx — Word document generation
- reportlab — PDF generation

---------------------------------------------------------------------

## Usage

Edit the parameters at the top of main.py:

DIVISION = "Junior"        # "Junior" or "Senior"
YEAR = 2026                # Pull all questions from this year first
SEEDING_ROUNDS = 5
ELIMINATION_ROUNDS = 2     # 1=Finals; 2=Semis+Finals; 3=Quarters+Semis+Finals
QUESTIONS_PER_ROUND = 24
CSV_PATH = "data/Questions_2025_Junior.csv"

Then run:

python main.py

This produces:
- output.txt — plain text version
- QuizRounds.docx — formatted Word document
- QuizRounds.pdf — formatted PDF with title page

---------------------------------------------------------------------

## How It Works

### 1. Load & Filter Questions
- All questions from the target year (e.g., 2026) are selected first.
- If more are needed, random questions from other years fill the remaining slots.
- The final set is shuffled.

### 2. Round Generation
Rounds are created in this order:
1. Seeding rounds
2. Elimination rounds:
   - 1 → Finals
   - 2 → Semifinals → Finals
   - 3 → Quarterfinals → Semifinals → Finals

### 3. Question Numbering
Each round contains 24 question pairs:
- Toss‑Up 1–12
- HALFTIME
- Toss‑Up 13–24

Bonus questions share the same number as their Toss‑Up.

### 4. Grammar Checking
The script flags potential issues in:
- TossUpQuestion
- BonusQuestion

This helps catch typos before printing.

### 5. Document Export
Word export includes:
- Title page
- Page breaks between rounds
- Large bold round titles
- Normal‑sized question text

PDF export includes:
- Title page
- Page breaks
- Clean, readable formatting

---------------------------------------------------------------------

## CSV Format

Your CSV must include these columns:
- TossUpQuestion
- TossUpAnswer
- BonusQuestion
- BonusAnswer
- OriginYear

Each row represents one question pair.

---------------------------------------------------------------------

## Example Output (Text)

Junior Round 1
======================================================================

Toss Up 1: What is the capital of France?
Answer: Paris
Bonus 1: Name any two countries that border France.
Answer: Spain, Belgium
***********************************************************************

...

HALFTIME
======================================================================

Toss Up 13: What is the largest planet in our solar system?
Answer: Jupiter
Bonus 13: What is the name of Jupiter’s largest moon?
Answer: Ganymede
***********************************************************************

---------------------------------------------------------------------
