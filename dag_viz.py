import argparse
import yaml

parser = argparse.ArgumentParser(description="visualize argo workflow DAGs")
parser.add_argument("file", type=str, help="the path to the workflow file")
parser.add_argument(
    "template", type=str, help="the template to render", nargs="?", default=""
)
args = parser.parse_args()

path = args.file

wf = {}

try:
    with open(path) as f:
        wf = yaml.load(f, Loader=yaml.FullLoader)
except:
    print(f"file {path} not found")
    exit(1)

templates = wf["spec"]["templates"]

if args.template == "":
    print(f"Please use one of the following templates:")
    for template in templates:
        name = template["name"]
        print(f"\t{name}")
    exit(1)

template_name = args.template

with open("output.gv", "w+") as f:

    for template in templates:
        name = template["name"].replace("-", "_")
        if "dag" not in template or template["name"] != template_name:
            continue

        f.write(f"digraph {name} {{\n")
        tasks = template["dag"]["tasks"]

        for task in tasks:
            name = task["name"].replace("-", "_")
            for dependency in task.get("dependencies", []):
                dep_name = dependency.replace("-", "_")
                f.write(f"\t{dep_name} -> {name}\n")

        f.write("}\n")
