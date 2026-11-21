# Деплой на Cloudflare Pages

1. `python generator.py` — создаёт `output/node-a` … `output/node-p`.
2. Каждый узел — отдельный проект Cloudflare Pages.
   - Репозиторий: один общий (или 16 репо).
   - Build command: пусто.
   - Output directory: `output/node-a` (для проекта узла A), `output/node-b` и т.д.
3. Домены: в каждом проекте добавь кастомный домен или используй `*.pages.dev`.
4. Включи "Always Use HTTPS" в Cloudflare.
5. `map.json` и `generator.py` не деплоить — добавь в `.gitignore`.
6. Проверь: ссылки вида `/node-b/?k=...` должны открываться, без `k` — связи скрыты.
