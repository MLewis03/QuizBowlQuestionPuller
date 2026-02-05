def elimination_titles(n):
    if n == 1:
        return ["Finals"]
    if n == 2:
        return ["Semifinals", "Finals"]
    if n == 3:
        return ["Quarterfinals", "Semifinals", "Finals"]
    return []

def build_rounds_output(df, division, seeding_rounds, elimination_rounds, questions_per_round):
    lines = []
    lines.append(f"{division} Division Questions")
    lines.append("=" * 70)
    lines.append("")

    idx = 0

    # Seeding rounds
    for r in range(1, seeding_rounds + 1):
        lines.append(f"{division} Round {r}")
        lines.append("=" * 70)
        round_df = df.iloc[idx:idx + questions_per_round]
        lines.extend(format_round(round_df, start_number=1))
        lines.append("")  # blank line between rounds
        idx += questions_per_round

    # Elimination rounds
    titles = elimination_titles(elimination_rounds)
    for title in titles:
        lines.append(f"{division} {title}")
        lines.append("=" * 70)
        round_df = df.iloc[idx:idx + questions_per_round]
        lines.extend(format_round(round_df, start_number=1))
        lines.append("")
        idx += questions_per_round

    return "\n".join(lines)

def format_round(round_df, start_number=1):
    lines = []
    first_half = round_df.iloc[:12]
    second_half = round_df.iloc[12:]

    # First half: questions 1–12 (or start_number..start_number+11)
    for offset, (_, row) in enumerate(first_half.iterrows()):
        qnum = start_number + offset
        lines.append(f"Toss Up {qnum}: {row['TossUpQuestion']}")
        lines.append(f"Answer: {row['TossUpAnswer']}")
        lines.append(f"Bonus {qnum}: {row['BonusQuestion']}")
        lines.append(f"Answer: {row['BonusAnswer']}")
        lines.append("*" * 70)

    lines.append("HALFTIME")
    lines.append("=" * 70)

    # Second half: questions 13–24 (or start_number+12..start_number+23)
    for offset, (_, row) in enumerate(second_half.iterrows()):
        qnum = start_number + 12 + offset
        lines.append(f"Toss Up {qnum}: {row['TossUpQuestion']}")
        lines.append(f"Answer: {row['TossUpAnswer']}")
        lines.append(f"Bonus {qnum}: {row['BonusQuestion']}")
        lines.append(f"Answer: {row['BonusAnswer']}")
        lines.append("*" * 70)

    return lines
