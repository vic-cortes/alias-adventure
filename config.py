from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
GRAPHICS_DIR = BASE_DIR / "graphics"
FONT_DIR = BASE_DIR / "font"


class GraphicsAssets:
    SKY_PATH = GRAPHICS_DIR / "sky.png"
    GROUND_PATH = GRAPHICS_DIR / "ground.png"
    SNAIL_PATH = GRAPHICS_DIR / "snail" / "snail1.png"
    PLAYER_PATH = GRAPHICS_DIR / "Player" / "player_walk_1.png"


class FontsAssets:
    MAIN_FONT = FONT_DIR / "Pixeltype.ttf"
