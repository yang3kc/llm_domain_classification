import json
import pandas as pd
import os


def load_api_key(api_key_path, provider):
    provider = provider.lower()
    with open(api_key_path) as f:
        key_obj = json.load(f)
        if provider not in key_obj:
            raise ValueError(
                f"Unknown provider: {provider}, must be one of {key_obj.keys()}"
            )

        api_key = key_obj.get(provider)
        return api_key


def get_domain_to_query(url_list_path, output_root):
    """
    Get list of domains that still need to be queried.

    Args:
        url_list_path (str): Path to CSV file containing domain list
        output_root (str): Directory containing processed domain results

    Returns:
        list: List of domain names that have not yet been processed
    """
    domain_df = pd.read_csv(url_list_path, usecols=["domain"])
    processed_domains = set()
    if not os.path.exists(output_root):
        os.makedirs(output_root, exist_ok=True)
    for file_name in os.listdir(output_root):
        if file_name.endswith(".txt"):
            processed_domains.add(file_name[:-4])

    print(f"{len(processed_domains)} domains have been processed")

    domain_to_query = domain_df[
        ~domain_df.domain.isin(processed_domains)
    ].domain.tolist()
    return domain_to_query
