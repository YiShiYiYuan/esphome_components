from pathlib import Path
from jinja2 import Environment, FileSystemLoader

self_path = Path(__file__).resolve()
env = Environment(loader=FileSystemLoader(self_path.parent))

template = env.get_template("bl0906.jinja2")

rendered_output = template.render()

print(rendered_output)
