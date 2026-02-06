import language_tool_python

def check_grammar(df):
    tool = language_tool_python.LanguageTool('en-US')
    results = []

    for idx, row in df.iterrows():
        for col in ["Toss_Up_Question", "Bonus_Question"]:
            text = str(row[col])
            matches = tool.check(text)

            if matches:
                entry = {
                    "row": idx,
                    "column": col,
                    "text": text,
                    "issues": []
                }

                for m in matches:
                    entry["issues"].append({
                        "message": m.message,
                        "suggestions": m.replacements,
                        "context": m.context,
                        "offset": m.offset,
                        "error_length": m.error_length,
                        "rule_id": m.rule_id
                    })

                results.append(entry)

    return results