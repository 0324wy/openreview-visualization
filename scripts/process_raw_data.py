from openreview_visualization.utils import open_json

papers = open_json("data/raw/iclr2025/raw_paperlist.json")

print(len(papers))

print(type(papers))

print(papers["notes"].keys())
    