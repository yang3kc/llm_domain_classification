import pandas as pd
import sys
import os
from scipy.stats import spearmanr, ttest_ind
import json

data_root = "../../../data"
processed_root = os.path.join(data_root, "processed")
query_list_file = os.path.join(data_root, "source", "dashboard_query_list.csv")


def p_value_to_stars(p_value):
    """
    Convert a p-value to significance stars.

    Parameters:
    p_value (float): The p-value to convert.

    Returns:
    str: The significance stars.
    """
    if p_value < 0.001:
        return "***"
    elif p_value < 0.01:
        return "**"
    elif p_value < 0.05:
        return "*"
    else:
        return "NS"  # Not significant


if __name__ == "__main__":
    resp_file_path = sys.argv[1]
    model_name = sys.argv[2]
    company_name = sys.argv[3]

    resp_df = pd.read_parquet(resp_file_path)
    query_list_df = pd.read_csv(query_list_file)

    print(f"resp_df: {resp_df.shape}")
    print(f"query_list_df: {query_list_df.shape}")
    merged_df = pd.merge(resp_df, query_list_df, on="domain")
    print(f"merged_df: {merged_df.shape}")

    merged_df["rating_diff"] = merged_df.rating - merged_df.credibility_rating

    corr_rho, corr_p = spearmanr(merged_df.rating, merged_df.credibility_rating)
    left_df = merged_df.query("political_leaning == 'left'")
    right_df = merged_df.query("political_leaning == 'right'")
    print(f"left_df: {left_df.shape}")
    print(f"right_df: {right_df.shape}")
    tstats, t_p = ttest_ind(right_df.rating_diff, left_df.rating_diff)

    results = {
        "model_name": model_name,
        "company": company_name,
        "n": merged_df.shape[0],
        "rho": corr_rho,
        "rho_p": corr_p,
        "rho_stars": p_value_to_stars(corr_p),
        "t": tstats,
        "t_p": t_p,
        "t_stars": p_value_to_stars(t_p),
        "left_n": left_df.shape[0],
        "right_n": right_df.shape[0],
    }

    with open(os.path.join(processed_root, f"{model_name}.json"), "a") as f:
        json.dump(results, f)
        f.write("\n")
