import json
from pathlib import Path

# This points to the folder where your script is located
folder_path = Path(r"c:\Users\paupau\Desktop\Comprog\Lab5_FIleHandling_Malabrigo")

# This looks for ANY .ipynb file in that folder
notebook_files = list(folder_path.glob("*.ipynb"))

if not notebook_files:
    print(f"❌ ERROR: No .ipynb files found in {folder_path}")
else:
    # We will check the first notebook we found
    target_file = notebook_files[0]
    print(f"🔍 Analyzing: {target_file.name}")

    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("✅ SUCCESS: This notebook is valid JSON. GitHub's error is likely a timeout.")
        print("👉 ACTION: Open the notebook, 'Clear All Outputs', save, and push again.")
        
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Found a broken character at Line {e.lineno}, Column {e.colno}")
        print(f"Message: {e.msg}")
        
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")