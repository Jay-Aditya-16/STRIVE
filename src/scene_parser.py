import os

def parse_yolo_labels(labels_path, classes):
    scenes = []

    for file in os.listdir(labels_path):
        if not file.endswith(".txt"):
            continue

        objects = []

        with open(os.path.join(labels_path, file)) as f:
            for line in f.readlines():
                class_id = int(line.split()[0])
                objects.append(classes[class_id])

        scene = "Objects detected: " + ", ".join(objects)
        scenes.append(scene)

    return scenes
