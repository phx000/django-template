import json

def get_variables_from_configmap():
    with open("k8s/_configmap_output.json") as file:
        json_string="\n".join(file.read().splitlines()[2:])
        configmap=json.loads(json_string)

    for key,value in configmap["data"].items():
        print(f'{key}={value}')

if __name__ == "__main__":
    get_variables_from_configmap()