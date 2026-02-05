import language_tool_python

def check_grammar(df):
    tool = language_tool_python.LanguageTool('en-US')
    issues = []

    for idx, row in df.iterrows():
        for col in ["TossUpQuestion", "BonusQuestion"]:
            text = str(row[col])
            matches = tool.check(text)
            if matches:
                issues.append(f"Row {idx} ({col}): {len(matches)} issue(s) found")

    return issues
