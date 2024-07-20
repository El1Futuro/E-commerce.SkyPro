from typing import Any


class MixinLog:
    def __repr__(self: Any) -> Any:
        attrs = []
        for attr in self.__dict__:
            attrs.append(f"{getattr(self, attr)}")
        attrs_str = ", ".join(attrs)
        print(f"Создан объект класса: {self.__class__.__name__}({attrs_str})")
