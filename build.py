"""Assemble les pages à partir de template.html et des données de montures (montures.json).

- index.html      : version pour l'artifact claude.ai (la plateforme ajoute doctype/head/body).
- docs/index.html : version autonome (servie par GitHub Pages), à mettre en ligne sur n'importe quel hébergeur statique.
"""
import json
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root / "montures.json").read_text(encoding="utf-8"))
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
page = (root / "template.html").read_text(encoding="utf-8").replace("/*__DATA__*/", payload)
(root / "index.html").write_text(page, encoding="utf-8")

# Sépare l'en-tête (title, meta, link, style) du contenu pour l'envelopper dans un document complet.
split = page.index("</style>") + len("</style>")
standalone = (
    "<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    + page[:split] + "\n</head>\n<body>\n" + page[split:] + "\n</body>\n</html>\n"
)
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(standalone, encoding="utf-8")
print(f"index.html et docs/index.html générés ({len(standalone) // 1024} Ko)")
