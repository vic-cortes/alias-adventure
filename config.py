from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
GRAPHICS_DIR = BASE_DIR / "graphics"


class GraphicsAssets:
    SKY_PATH = GRAPHICS_DIR / "sky.png"
    GROUND_PATH = GRAPHICS_DIR / "ground.png"
