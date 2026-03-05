def elimination_titles(n):
    if n == 1:
        return ["Finals"]
    if n == 2:
        return ["Semifinals", "Finals"]
    if n == 3:
        return ["Quarterfinals", "Semifinals", "Finals"]
    return []


def build_rounds_output(round_df, appendix_df, division, seeding_rounds, elimination_rounds, questions_per_round):
    lines = []
    idx = 0

    # ---------------------------------------------------------
    # SEEDING ROUNDS
    # ---------------------------------------------------------
    for r in range(1, seeding_rounds + 1):

        if r > 1:
            lines.append("===PAGEBREAK===")

        lines.append(f"{division} Round {r}")
        lines.append("=" * 70)

        df_slice = round_df.iloc[idx:idx + questions_per_round]
        idx += questions_per_round

        lines.extend(format_round(df_slice))
        lines.append("")

    # ---------------------------------------------------------
    # ELIMINATION ROUNDS
    # ---------------------------------------------------------
    titles = elimination_titles(elimination_rounds)

    for title in titles:
        lines.append("===PAGEBREAK===")
        lines.append(f"{division} {title}")
        lines.append("=" * 70)

        df_slice = round_df.iloc[idx:idx + questions_per_round]
        idx += questions_per_round

        lines.extend(format_round(df_slice))
        lines.append("")

    # ---------------------------------------------------------
    # APPENDIX
    # ---------------------------------------------------------
    lines.append("===PAGEBREAK===")
    lines.append("Appendix: Extra Question Pairs")
    lines.append("=" * 70)
    lines.append("")

    for i, row in appendix_df.iterrows():
        qnum = i + 1
        lines.append(f"Toss Up {qnum}: {row['Toss_Up_Question']}")
        lines.append(f"Answer: {row['T_Answer']}")
        lines.append(f"Bonus {qnum}: {row['Bonus_Question']}")
        lines.append(f"Answer: {row['B_Answer']}")
        lines.append("*" * 70)

    return "\n".join(lines)


def format_round(df_slice):
    lines = []

    first_half = df_slice.iloc[:12]
    second_half = df_slice.iloc[12:]

    # -------------------------
    # FIRST HALF (1–12)
    # -------------------------
    for i, (_, row) in enumerate(first_half.iterrows(), start=1):
        lines.append(f"Toss Up {i}: {row['Toss_Up_Question']}")
        lines.append(f"Answer: {row['T_Answer']}")
        lines.append(f"Bonus {i}: {row['Bonus_Question']}")
        lines.append(f"Answer: {row['B_Answer']}")
        lines.append("*" * 70)

    lines.append("HALFTIME")
    lines.append("=" * 70)

    # -------------------------
    # SECOND HALF (13–24)
    # -------------------------
    for i, (_, row) in enumerate(second_half.iterrows(), start=13):
        lines.append(f"Toss Up {i}: {row['Toss_Up_Question']}")
        lines.append(f"Answer: {row['T_Answer']}")
        lines.append(f"Bonus {i}: {row['Bonus_Question']}")
        lines.append(f"Answer: {row['B_Answer']}")
        lines.append("*" * 70)

    return lines