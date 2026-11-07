import os
import sys
import site


def check_laboratory() -> None:
    has_venv = (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
        or "VIRTUAL_ENV" in os.environ
    )

    if not has_venv:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print()
        print("Then run this program again.")
    else:
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        venv_name = os.path.basename(venv_path)

        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")
        site_packages = site.getsitepackages()
        if site_packages:
            print(site_packages[0])
        else:
            print(
                f"{sys.prefix}/lib/python"
                f"{sys.version_info.major}.{sys.version_info.minor}"
                "/site-packages"
            )


if __name__ == "__main__":
    check_laboratory()
