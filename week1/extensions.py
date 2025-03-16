import os


def main():
    file = input("File name: ").lower().strip()
    parts = os.path.splitext(file)[1]
    parts = parts[1:] if parts else ""

    types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "gif": "image/gif",
        "png": "image/png",
        "pdf": "application/pdf",
        "zip": "application/zip",
        "txt": "text/plain"
    }

    if parts in types:
        print(types[parts])
    else:
        print(types.get(parts, "application/octet-stream"))


main()
