import sys


def load_reagents() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    missing = False

    try:
        import pandas as pd  # type: ignore[import-untyped]
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except ImportError:
        print("[MISSING] pandas - Reagent missing!")
        missing = True

    try:
        import numpy as np  # type: ignore[import-not-found]
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    except ImportError:
        print("[MISSING] numpy - Reagent missing!")
        missing = True

    print()
    print("pip vs Poetry:")
    print(
        "requirements.txt declares what to install; pip resolves it at "
        "install time."
    )
    print(
        "pyproject.toml declares the same constraints, and Poetry pins the "
        "resolved"
    )
    print("versions in poetry.lock so every install is identical.")
    print()

    if missing:
        print("CRITICAL: Some reagents are missing from your laboratory!")
        print("To install via pip: pip install -r ex0/requirements.txt")
        print("To install via Poetry: poetry install")
        sys.exit(1)
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    load_reagents()
