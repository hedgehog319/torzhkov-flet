import yaml
import re


class Locale:
    _available_locales: set[str]
    _translate: dict[str, str]
    _template: re.Pattern = re.compile(r"{{\s*(.*?)\s*}}")

    locale: str

    def __init__(self, locale: str = "en") -> None:
        self._available_locales = {"en", "ru"}
        self.set_locale(locale)

    def set_locale(self, locale: str) -> None:
        if locale not in self._available_locales:
            return
        self.locale = locale
        self._translate = yaml.safe_load(open(f"locale/{locale}.yml", "r").read())

    def __call__(self, text: str) -> str:
        pattern = self._template.findall(text)
        if not pattern:
            return text
        return self._translate.get(pattern[0].lower(), text)


localize = Locale()
