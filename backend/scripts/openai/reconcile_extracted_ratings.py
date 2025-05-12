import sys
import os
import json

if __name__ == "__main__":
    old_resp_dir = sys.argv[1]
    extracted_resp_dir = sys.argv[2]
    output_dir = sys.argv[3]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(old_resp_dir):
        domain = file[:-4]
        extracted_path = os.path.join(extracted_resp_dir, file)
        if not os.path.exists(extracted_path):
            print(f"No extracted response found for {extracted_path}")
            continue
        with open(os.path.join(old_resp_dir, file), "r") as f:
            old_resp = json.load(f)
        with open(extracted_path, "r") as f:
            extracted_resp = json.load(f)
        parsed_extracted_resp = extracted_resp["output"][0]["content"][0]["parsed"]
        parsed_extracted_resp["domain"] = domain
        new_resp = {
            "usage": old_resp["usage"],
            "output": [
                {
                    "type": "message",
                    "role": "assistant",
                    "content": [
                        {
                            "text": json.dumps(parsed_extracted_resp),
                            "type": "text",
                        }
                    ],
                }
            ],
        }
        with open(os.path.join(output_dir, file), "w") as f:
            json.dump(new_resp, f, indent=2)
