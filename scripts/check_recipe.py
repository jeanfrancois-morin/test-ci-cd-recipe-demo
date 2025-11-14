import sys
from pathlib import Path

EXPECTED_INGREDIENTS = ["œufs", "sucre", "beurre", "chocolat", "farine"]

def main():
    readme = Path("README.md").read_text(encoding="utf-8").lower()

    missing = [i for i in EXPECTED_INGREDIENTS if i not in readme]

    if missing:
        print("❌ Recette incomplète ! Ingrédients manquants :", ", ".join(missing))
        sys.exit(1)
    else:
        print("✅ Tous les ingrédients sont présents !")

if __name__ == "__main__":
    main()
