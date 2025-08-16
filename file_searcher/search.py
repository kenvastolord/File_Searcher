import os


def search_by_extension(directory: str, extension: str) -> list[str]:
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matching_files.append(os.path.join(root, file))
    return matching_files


def search_by_name(directory: str, name: str) -> list[str]:
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if name.lower() in file.lower():
                matching_files.append((os.path.join(root, file)))

    return matching_files
