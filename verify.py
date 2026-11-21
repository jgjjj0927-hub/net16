from pathlib import Path
import re

ROOT = Path(__file__).parent
OUT = ROOT / "output"
NODES = "ABCDEFGHIJKLMNOP"

LINKS = {
    "A": ["B", "C", "E"], "B": ["C", "D", "F"], "C": ["D", "E", "G"],
    "D": ["E", "F", "H"], "E": ["F", "G", "I"], "F": ["G", "H", "J"],
    "G": ["H", "I", "K"], "H": ["I", "J", "L"], "I": ["J", "K", "M"],
    "J": ["K", "L", "N"], "K": ["L", "M", "O"], "L": ["M", "N", "P"],
    "M": ["N", "O", "A"], "N": ["O", "P", "B"], "O": ["P", "A", "C"],
    "P": ["A", "B", "D"],
}

errors = []

for node in NODES:
    d = OUT / f"node-{node.lower()}"
    idx = d / "index.html"
    if not idx.exists():
        errors.append(f"нет файла: {idx}")
        continue

    html = idx.read_text(encoding="utf-8")
    for n in LINKS[node]:
        target = f"/node-{n.lower()}/"
        if target not in html:
            errors.append(f"узел {node}: нет ссылки на {n} ({target})")

    if "noindex" not in html:
        errors.append(f"узел {node}: нет noindex")

    if "duckduckgo.com" not in html:
        errors.append(f"узел {node}: нет ссылки на DuckDuckGo")

if errors:
    print("ОШИБКИ:")
    for e in errors:
        print(f"  - {e}")
else:
    print("всё чисто: 16 узлов, все ссылки на месте")

# проверка что map.json не в output
if (OUT / "map.json").exists():
    print("ВНИМАНИЕ: map.json попал в output — удали")
