#STRIVE
### Structured Textual Reasoning for Interpreting Visual Environments

STRIVE is a hybrid artificial intelligence framework designed to bridge the gap between computer vision perception and contextual reasoning. It enables the interpretation of visual environments by transforming detection outputs into structured textual representations that can be processed by a language model.

---

## 1. Problem Statement

Modern computer vision systems are highly effective at detecting and localizing objects. However, they operate at a perception level and lack the ability to reason about relationships, intent, and contextual meaning.

For example, the presence of multiple drones near critical infrastructure represents a different scenario than a single drone at a distance. Traditional detection pipelines are not designed to interpret such distinctions.

This limitation highlights a fundamental gap between visual perception and contextual understanding.

---

## 2. Approach

STRIVE introduces a multi-stage pipeline that integrates perception with reasoning:

```
Image Input
↓
Object Detection
↓
Scene Representation Generation
↓
Language Model Reasoning
↓
Threat Assessment
```

The core idea is to convert detection outputs into structured or natural language descriptions, enabling a language model to perform higher-level reasoning.

---

## 3. System Architecture

The system consists of the following components:

* Perception Layer: Object detection using a YOLO-based model
* Scene Representation Layer: Converts detections into textual descriptions
* Reasoning Layer: Fine-tuned language model (Qwen2.5)
* Output Layer: Threat classification based on contextual interpretation

---

## 4. Representation Strategies

### 4.1 Version 1: Structured Representation

Scene descriptions are expressed in a rigid format.

Example:

```
Objects detected: drone, drone
Distance: 120 meters
Target: facility
Direction: north
```

This approach enables controlled inputs but limits expressive capacity.

Performance:

* Accuracy: 43 percent
* F1 Score: 0.30

---

### 4.2 Version 2: Natural Language Representation

Scene descriptions are expressed in natural language.

Example:

```
Two drones are approaching a facility from the north at approximately 120 meters.
```

This representation leverages the pretraining of language models and improves contextual reasoning.

Performance:

* Accuracy: 59 percent
* Weighted F1 Score: approximately 0.65

---

## 5. Key Insight

Natural language representations significantly improve reasoning capability compared to rigid structured inputs. This suggests that language models benefit from semantically rich and flexible representations of visual scenes.

---

## 6. Technology Stack

* Computer Vision: YOLO-based object detection
* Language Model: Qwen2.5
* Fine-tuning: LoRA (Low-Rank Adaptation)
* Frameworks: Hugging Face Transformers, PyTorch

---

## 7. Project Structure

```
STRIVE/
│
├── src/              # Core pipeline modules
├── data/             # Sample datasets
├── models/           # Trained models (excluded via .gitignore)
├── notebooks/        # Experimental workflows
├── requirements.txt
└── README.md
```

---

## 8. Usage

### Installation

```
pip install -r requirements.txt
```

### Training

```
python src/train.py
```

### Inference

```
python src/inference.py
```

---

## 9. Evaluation

The system is evaluated using standard classification metrics:

* Accuracy
* Precision
* Recall
* F1 Score

Results demonstrate improvement from structured to natural language representations.

---

## 10. Limitations

* Single-frame analysis without temporal context
* Simplified threat modeling logic
* Limited spatial reasoning capabilities
* Dataset imbalance

---

## 11. Future Work

* Temporal reasoning using multi-frame data
* Spatial reasoning with geometric relationships
* Graph-based scene representation
* Integration with multimodal models
* Deployment in real-time monitoring systems

---

## 12. License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

### Additional Restrictions

This project may not be used for:

* Military or defense applications
* Weaponization
* Harmful surveillance systems

The project is intended for ethical, civilian, and research use only.

---

## 13. Author

Jay Aditya
Founder, Sentrix Labs

---

## 14. Research Direction

STRIVE explores a shift from perception-driven systems toward reasoning-driven systems, where artificial intelligence is capable of interpreting relationships, context, and meaning within complex environments.


<img width="2245" height="1587" alt="Research Poster in Blue   Gold Simple Style" src="https://github.com/user-attachments/assets/8ef3dd0b-0394-4427-bf76-b12de7ad15ea" />


