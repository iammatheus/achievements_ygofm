from PIL import Image
from pathlib import Path

INPUT_DIR = Path("assets/original")
OUTPUT_DIR = Path("assets/optimized")

MAX_SIZE = (312, 312)   # resolução máxima que uma imagem pode atingir
JPEG_QUALITY = 70       # 0–100 (quanto menor, mais leve)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

def optimize_images():
  for img_path in INPUT_DIR.iterdir():
    if img_path.suffix.lower() not in VALID_EXTENSIONS:
      continue

    img = Image.open(img_path)

    # Converte PNG com transparência para RGB
    if img.mode in ("RGBA", "P"):
      img = img.convert("RGB")

    # Mantém proporção
    img.thumbnail(MAX_SIZE)

    output_path = OUTPUT_DIR / f"{img_path.stem}.jpg"

    img.save(
      output_path,
      format="JPEG",
      quality=JPEG_QUALITY,
      optimize=True,
      progressive=True
    )

    print(f"✅ {img_path.name} → {output_path.name}")

optimize_images()