import os
common_uses = [
    "Content Creation",
    "Customer Support",
    "Data Analysis",
    "Educational Tools",
    "Language Translation",
    "Legal Assistance",
    "Medical Information",
    "Programming Help",
    "Social Media Management",
    "Virtual Assistant"
]

# Sort the list alphabetically
common_uses.sort()

# Create the folders
for folder_name in common_uses:
    os.makedirs(folder_name, exist_ok=True)

print("Folders created:")
for folder_name in common_uses:
    print(f"- {folder_name}")
