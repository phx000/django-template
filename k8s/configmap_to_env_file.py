import json

def create_env_file_from_configmap():
    with open("k8s/_configmap_output.json") as file:
        json_string="\n".join(file.read().splitlines()[2:])
        configmap=json.loads(json_string)

    env_string="\n".join([f"{key}={value}" for key, value in configmap["data"].items()])

    with open("k8s/_configmap.env", "w") as file:
        file.write(env_string)

if __name__ == "__main__":
    create_env_file_from_configmap()