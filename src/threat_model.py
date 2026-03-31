def generate_response(scene):
    drone_count = scene.count("drone")

    if drone_count >= 3:
        return "Threat level high due to multiple UAVs detected."

    elif drone_count == 2:
        return "Threat level medium. Two UAVs detected."

    elif drone_count == 1:
        return "Threat level low. Single UAV detected."

    else:
        return "No UAV detected."
