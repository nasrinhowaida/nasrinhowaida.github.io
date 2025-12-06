import os, json

# -------------------------------
#  Folders to scan (exact names)
# -------------------------------
folders = [
    "Tarahi",
    "Modern_Hashour",
    "Khalaghane_Abarang",
    "Model_Figurative"
]

# Allowed image formats
exts = (".jpg", ".jpeg", ".png", ".webp")

print("\n--- Generating manifest.json files ---\n")

for folder in folders:
    if not os.path.isdir(folder):
        print(f"⚠️  Folder not found: {folder}")
        continue

    files = sorted([
        fn for fn in os.listdir(folder)
        if fn.lower().endswith(exts)
    ])

    manifest_path = os.path.join(folder, "manifest.json")

    with open(manifest_path, "w", encoding="utf8") as fh:
        json.dump(files, fh, ensure_ascii=False, indent=2)

    print(f"✔ manifest.json created for {folder} ({len(files)} images)")

print("\nAll done! Now run:")
print("   git add .")
print("   git commit -m \"Add manifest.json files\"")
print("   git push\n")
