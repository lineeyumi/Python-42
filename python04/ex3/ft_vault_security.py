#!/usr/bin/env python3
from typing import Optional, Tuple


def secure_archive(
    filename: str, action: str = "read", content: Optional[str] = None
) -> Tuple[bool, str]:
    if action == "write":
        try:
            with open(filename, "w") as f:
                if content is not None:
                    f.write(content)
            return True, "Content successfully written to file"
        except Exception as e:
            return False, str(e)

    try:
        with open(filename, "r") as f:
            data = f.read()
        return True, data
    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    res1 = secure_archive("/not/existing/file")
    print(res1)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    res2 = secure_archive("/etc/shadow")
    print(res2)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    res3 = secure_archive("ancient_fragment.txt")
    print(res3)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    res4 = secure_archive(
        "new_vault_entry.txt", "write", "Secure Data 2087"
    )
    print(res4)
