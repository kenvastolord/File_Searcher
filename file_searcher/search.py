import os
from locale import normalize


def search_by_extension(directory: str, extensions: str) -> list[str]:
    matching_files = []
    normalize_exts = [
        ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in extensions
    ]

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in normalize_exts):
                matching_files.append(os.path.join(root, file))
    return matching_files


def search_by_name(directory: str, name: str) -> list[str]:
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if name.lower() in file.lower():
                matching_files.append((os.path.join(root, file)))

    return matching_files
