import base64
import json
from pathlib import Path

NODES = "ABCDEFGHIJKLMNOP"

LINKS = {
    "A": ["B", "C", "E"],
    "B": ["C", "D", "F"],
    "C": ["D", "E", "G"],
    "D": ["E", "F", "H"],
    "E": ["F", "G", "I"],
    "F": ["G", "H", "J"],
    "G": ["H", "I", "K"],
    "H": ["I", "J", "L"],
    "I": ["J", "K", "M"],
    "J": ["K", "L", "N"],
    "K": ["L", "M", "O"],
    "L": ["M", "N", "P"],
    "M": ["N", "O", "A"],
    "N": ["O", "P", "B"],
    "O": ["P", "A", "C"],
    "P": ["A", "B", "D"],
}

TOPICS = {
    "A": "Приватность в сети",
    "B": "Шифрование трафика",
    "C": "Анонимность и Tor",
    "D": "Защита данных",
    "E": "Пароли и менеджеры",
    "F": "VPN: как работает",
    "G": "Метаданные и следы",
    "H": "Браузеры и fingerprint",
    "I": "Почта без слежки",
    "J": "Мессенджеры",
    "K": "Хранение файлов",
    "L": "ОС для приватности",
    "M": "Сеть и DNS",
    "N": "Публичные Wi-Fi",
    "O": "Социальная инженерия",
    "P": "Фишинг и защита",
}

def encode_link(target: str) -> str:
    """urlsafe base64 без паддинга"""
    return base64.urlsafe_b64encode(target.encode()).decode().rstrip("=")

def decode_link(code: str) -> str:
    pad = "=" * (-len(code) % 4)
    return base64.urlsafe_b64decode(code + pad).decode()

def build_node(node: str, out_root: Path, template: str):
    neighbors = LINKS[node]
    links_html = ""
    for n in neighbors:
        code = encode_link(n)
        links_html += (
            f'<li><a href="/node-{n.lower()}/?k={code}" '
            f'data-node="{n}">{n}</a></li>\n'
        )

    ddg = "https://duckduckgo.com"
    page = template.format(
        node=node,
        topic=TOPICS[node],
        links=links_html,
        ddg=ddg,
    )
    node_dir = out_root / f"node-{node.lower()}"
    node_dir.mkdir(parents=True, exist_ok=True)
    (node_dir / "index.html").write_text(page, encoding="utf-8")

def main():
    root = Path(__file__).parent
    template = (root / "templates" / "node.html").read_text(encoding="utf-8")
    out = root / "output"
    out.mkdir(exist_ok=True)

    for node in NODES:
        build_node(node, out, template)

    # карта связей — только локально, в .gitignore
    (root / "map.json").write_text(
        json.dumps(LINKS, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print("готово: 16 узлов в output/")

if __name__ == "__main__":
    main()
