import pandas as pd

def load_and_select_questions(csv_path, target_year, total_needed, seed=None):
    df = pd.read_csv(csv_path)

    # Filter by year
    current_year_df = df[df["Origin_Year"] == target_year]
    other_years_df = df[df["Origin_Year"] != target_year]

    total_required = total_needed + 5  # rounds + appendix

    # ---------------------------------------------------------
    # STEP 1: Pull enough questions (prefer current year)
    # ---------------------------------------------------------
    if len(current_year_df) >= total_required:
        selected_df = current_year_df.sample(total_required, random_state=seed)
    else:
        # Use all current-year questions first
        selected_records = list(current_year_df.to_dict("records"))
        remaining_needed = total_required - len(selected_records)

        # Fill the rest from other years
        sampled_other = other_years_df.sample(remaining_needed, random_state=seed)
        selected_records.extend(sampled_other.to_dict("records"))

        selected_df = pd.DataFrame(selected_records)

    # ---------------------------------------------------------
    # STEP 2: Shuffle once, then split
    # ---------------------------------------------------------
    selected_df = selected_df.sample(frac=1, random_state=seed).reset_index(drop=True)

    round_df = selected_df.iloc[:total_needed].reset_index(drop=True)
    appendix_df = selected_df.iloc[total_needed:].reset_index(drop=True)

    return round_df, appendix_df