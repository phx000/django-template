import json
import os

with open(".github/workflows/_app_spec.json") as f:
    data = json.load(f)

for s in data["services"]:
    if s["name"] == "api":
        s["image"]["tag"] = os.getenv("IMAGE_VERSION")
        break

for w in data["workers"]:
    if w["name"] == "worker":
        w["image"]["tag"] = os.getenv("IMAGE_VERSION")
        break

with open(".github/workflows/_app_spec.json", "w") as f:
    json.dump(f, data)
