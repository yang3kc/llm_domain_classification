from llmdomainrating import create_api_client, get_domain_to_query
import sys
import os
from tqdm import tqdm

domain_list_path = sys.argv[1]
provider = sys.argv[2]
model = sys.argv[3]
output_root = sys.argv[-1]

client = create_api_client(provider)
domains_to_query = get_domain_to_query(domain_list_path, output_root)

for domain in tqdm(domains_to_query):
    resp = client.query_model(domain, model)
    with open(os.path.join(output_root, f"{domain}.txt"), "w") as f:
        f.write(resp)
