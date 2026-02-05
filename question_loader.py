import pandas as pd

def load_and_select_questions(csv_path, target_year, total_needed):
    df = pd.read_csv(csv_path)

    current_year_df = df[df["OriginYear"] == target_year]
    other_years_df = df[df["OriginYear"] != target_year]

    if len(current_year_df) >= total_needed:
        selected_df = current_year_df.sample(total_needed)
    else:
        selected = []
        selected.extend(current_year_df.to_dict("records"))
        remaining_needed = total_needed - len(selected)
        selected.extend(other_years_df.sample(remaining_needed).to_dict("records"))
        selected_df = pd.DataFrame(selected)

    selected_df = selected_df.sample(frac=1).reset_index(drop=True)
    return selected_df
