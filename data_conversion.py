import json
import os


def json_to_jsonl(json_input, jsonl_output):
    """
    Convert a JSON file to a JSONL (JSON Lines) file.

    Parameters:
    json_input (str): Path to the input JSON file.
    jsonl_output (str): Path to the output JSONL file.
    """
    # Open and read the JSON file
    with open(json_input, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)  # Load the JSON data into a Python object

    # Open the output JSONL file in write mode
    with open(jsonl_output, "w", encoding="utf-8") as jsonl_file:
        for entry in data:
            # Remove the "SOURCE" field if it exists in the current entry
            entry.pop("SOURCE", None)
            # Convert the entry back to a JSON string and write it to the JSONL file, followed by a newline character
            jsonl_file.write(json.dumps(entry) + "\n")


# Example usage
json_input = "data/grade-school-math-instructions-train.json"

# Derive the output file path in the same directory as the input file
input_dir = os.path.dirname(json_input)
jsonl_output = os.path.join(input_dir, "grade-school-math-instructions-train.jsonl")

json_to_jsonl(json_input, jsonl_output)
