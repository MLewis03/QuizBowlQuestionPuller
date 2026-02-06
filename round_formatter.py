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
    idx = 0

    # ---------------------------------------------------------
    # SEEDING ROUNDS
    # ---------------------------------------------------------
    for r in range(1, seeding_rounds + 1):

        # Page break before every round except the first
        if r > 1:
            lines.append("===PAGEBREAK===")

        # Round header
        lines.append(f"{division} Round {r}")
        lines.append("=" * 70)

        # Slice the dataframe for this round
        round_df = df.iloc[idx:idx + questions_per_round]
        idx += questions_per_round

        # Add formatted questions
        lines.extend(format_round(round_df, start_number=1))
        lines.append("")  # spacing after round

    # ---------------------------------------------------------
    # ELIMINATION ROUNDS
    # ---------------------------------------------------------
    titles = elimination_titles(elimination_rounds)

    for title in titles:
        lines.append("===PAGEBREAK===")
        lines.append(f"{division} {title}")
        lines.append("=" * 70)

        round_df = df.iloc[idx:idx + questions_per_round]
        idx += questions_per_round

        lines.extend(format_round(round_df, start_number=1))
        lines.append("")

    return "\n".join(lines)


def format_round(round_df, start_number=1):
    lines = []

    # First 12 questions
    first_half = round_df.iloc[:12]
    # Last 12 questions
    second_half = round_df.iloc[12:]

    # -------------------------
    # FIRST HALF (1–12)
    # -------------------------
    for offset, (_, row) in enumerate(first_half.iterrows()):
        qnum = start_number + offset

        lines.append(f"Toss Up {qnum}: {row['Toss_Up_Question']}")
        lines.append(f"Answer: {row['T_Answer']}")
        lines.append(f"Bonus {qnum}: {row['Bonus_Question']}")
        lines.append(f"Answer: {row['B_Answer']}")
        lines.append("*" * 70)

    # Halftime marker
    lines.append("HALFTIME")
    lines.append("=" * 70)

    # -------------------------
    # SECOND HALF (13–24)
    # -------------------------
    for offset, (_, row) in enumerate(second_half.iterrows()):
        qnum = start_number + 12 + offset

        lines.append(f"Toss Up {qnum}: {row['Toss_Up_Question']}")
        lines.append(f"Answer: {row['T_Answer']}")
        lines.append(f"Bonus {qnum}: {row['Bonus_Question']}")
        lines.append(f"Answer: {row['B_Answer']}")
        lines.append("*" * 70)

    return lines


def build_appendix_output(df):
    lines = []
    lines.append("Appendix: Extra Question Pairs")
    lines.append("=" * 70)
    lines.append("")

    for i, row in df.iterrows():
        qnum = i + 1
        lines.append(f"Toss Up {qnum}: {row['Toss_Up_Question']}")
        lines.append(f"Answer: {row['T_Answer']}")
        lines.append(f"Bonus {qnum}: {row['Bonus_Question']}")
        lines.append(f"Answer: {row['B_Answer']}")
        lines.append("*" * 70)

    return "\n".join(lines)