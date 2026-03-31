import json
from threat_model import generate_response

def build_dataset(scenes):
    dataset = []

    for scene in scenes:
        dataset.append({
            "instruction": "Analyze the aerial scene and determine UAV threat level.",
            "input": scene,
            "output": generate_response(scene)
        })

    return dataset


def format_dataset(dataset):
    formatted = []

    for item in dataset:
        text = f"""
### Instruction
{item['instruction']}

### Scene
{item['input']}

### Response
{item['output']}
"""
        formatted.append({"text": text})

    return formatted


def save_dataset(data, path="data/training.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
