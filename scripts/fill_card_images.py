import json
from pathlib import Path

CARDS_PATH = Path("memory/data/all_cards.json").resolve()
IMAGES_PATH = Path("memory/data/cards_images_paths.json").resolve()

def fill_images():
  with open(CARDS_PATH, "r", encoding="utf-8") as f:
    cards = json.load(f)

  with open(IMAGES_PATH, "r", encoding="utf-8") as f:
    images_map = json.load(f)

  updated = 0

  for card in cards:
    card_id = str(card.get("id"))

    if card_id in images_map:
      card["image"] = images_map[card_id]
      updated += 1


  with open(CARDS_PATH, "w", encoding="utf-8") as f:
    json.dump(cards, f, indent=2, ensure_ascii=False)

  print(f"✅ {updated} cartas atualizadas com imagem.")


fill_images()
# if __name__ == "__main__":
#   fill_images()
