import pandas as pd

def load_and_select_questions(csv_path, target_year, total_needed, seed=None):
    # Load full dataset
    df = pd.read_csv(csv_path)

    # Filter by year
    current_year_df = df[df["Origin_Year"] == target_year]
    other_years_df = df[df["Origin_Year"] != target_year]

    # Select questions
    if len(current_year_df) >= total_needed:
        selected_df = current_year_df.sample(total_needed, random_state=seed)
    else:
        selected_records = []

        # Use all current-year questions first
        selected_records.extend(current_year_df.to_dict("records"))

        remaining_needed = total_needed - len(selected_records)

        # Sample remaining from other years
        sampled_other = other_years_df.sample(remaining_needed, random_state=seed)
        selected_records.extend(sampled_other.to_dict("records"))

        selected_df = pd.DataFrame(selected_records)

    # Shuffle final selection deterministically
    selected_df = selected_df.sample(frac=1, random_state=seed).reset_index(drop=True)

    # Return BOTH the selected questions and the full dataset
    return selected_df, df