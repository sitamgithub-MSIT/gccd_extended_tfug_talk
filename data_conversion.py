import json


def json_to_jsonl(json_input, jsonl_output):
    with open(json_input, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    with open(jsonl_output, "w", encoding="utf-8") as jsonl_file:
        for entry in data:
            # Remove the "SOURCE" field if it exists
            entry.pop("SOURCE", None)
            jsonl_file.write(json.dumps(entry) + "\n")


# Example usage
json_input = "data/grade_school_math.json"
jsonl_output = "math_instruct_data.jsonl"
json_to_jsonl(json_input, jsonl_output)
