# 2. batchify.py
import pandas as pd
import math
import os

# 🔢 Justera batchstorlek här
BATCH_SIZE = 100

# 📥 Läs in din rensade Excelfil
input_file = 'gymnasieskolor_unika_email.xlsx'
df = pd.read_excel(input_file)

# 🧮 Räkna ut antal batchar
num_batches = math.ceil(len(df) / BATCH_SIZE)
print(f"Total emails: {len(df)}")
print(f"Create {num_batches} files with {BATCH_SIZE} per file.")

# 📂 Skapa undermapp för batch-filer (om du vill)
output_dir = "batches"
os.makedirs(output_dir, exist_ok=True)

# 🪄 Dela upp och spara varje batch
for i in range(num_batches):
    start = i * BATCH_SIZE
    end = start + BATCH_SIZE
    batch_df = df.iloc[start:end]

    batch_filename = os.path.join(output_dir, f"batch_{i + 1:02}.xlsx")
    batch_df.to_excel(batch_filename, index=False)

    print(f"✅ Created {batch_filename} with {len(batch_df)} rows")

print("\n🚀 All batch files have been created!")
