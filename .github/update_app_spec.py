import json
import os

with open(".github/_app_spec.json") as f:
    data = json.load(f)

for s in data["services"]:
    if s["name"] == "api":
        s["image"]["tag"] = os.getenv("IMAGE_VERSION")
        break

for w in data["workers"]:
    if w["name"] == "worker":
        w["image"]["tag"] = os.getenv("IMAGE_VERSION")
        break

for j in data["jobs"]:
    if j["name"] == "success-job":
        j["image"]["tag"] = os.getenv("IMAGE_VERSION")
        break

with open(".github/_app_spec.json", "w") as f:
    json.dump(data, f)
