import os
import typing as T

import yaml
from jinja2 import Environment, FileSystemLoader, Template


class TemplateGenerator:
    def __init__(
        self,
        config_path: str,
        search_path: str,
        template_name: str,
        output_path: str,
    ) -> None:
        self.config_path = config_path
        self.search_path = search_path
        self.template_name = template_name
        self.output_path = output_path

    def _load_params(self) -> T.Dict[str, T.Any]:
        d: T.Dict[str, T.Any]
        with open(self.config_path, "r") as f:
            d = yaml.safe_load(f)
        return d

    def _load_template(self) -> Template:
        env = Environment(loader=FileSystemLoader(self.search_path, encoding="utf8"))
        tmpl = env.get_template(self.template_name)
        return tmpl

    def _render(self, template: Template, params: T.Dict[str, T.Any]) -> str:
        rendered = template.render(params)
        return rendered

    def _save(self, rendered: str) -> None:
        current_dir = os.getcwd()
        current_path = __file__
        this_filepath = current_path.replace(f"{current_dir}/", "")
        with open(self.output_path, "w") as f:
            f.write(rendered)

    def generate(self) -> None:
        params = self._load_params()
        tmpl = self._load_template()
        rendered = self._render(tmpl, params)
        self._save(rendered)


def main() -> None:
    g = TemplateGenerator(
        config_path="./config.yaml",
        search_path="./dist/templates",
        template_name="layout.html",
        output_path="./dist/index.html",
    )
    g.generate()


if __name__ == "__main__":
    main()
