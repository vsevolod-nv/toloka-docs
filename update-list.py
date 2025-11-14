import os
import json

files = [f"documents/{f}" for f in os.listdir("documents") if f.endswith(".html")]
with open("document-list.json", "w") as f:
    json.dump(files, f)
