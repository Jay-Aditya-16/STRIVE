from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "models/strive_model"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)
    return tokenizer, model


def predict(scene):
    tokenizer, model = load_model()

    prompt = f"""
### Instruction
Analyze the aerial scene and determine UAV threat level.

### Scene
{scene}

### Response
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(**inputs, max_new_tokens=50)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    scene = "Objects detected: drone, drone"
    print(predict(scene))
