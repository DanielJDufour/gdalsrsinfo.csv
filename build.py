from csv import DictWriter, QUOTE_ALL
from subprocess import check_output, DEVNULL

rows = []

start = 4326
end = 32767

for i in range(start, end + 1):
  try:
    row = {}
    out = check_output(f"OSR_USE_NON_DEPRECATED=NO gdalsrsinfo -o all EPSG:{i}", shell=True, stderr=DEVNULL)

    text = out.decode("utf-8").strip()

    parts = text.split("\n\n")
    for part in parts:
      part = part.strip()

      out_type, data = part.split(":", 1)

      out_type = out_type.strip()
      data = data.strip()
      
      row[out_type] = data

    if row:
      row['EPSG'] = i
      rows.append(row)

  except Exception as e:
    pass

# collect all output types
output_types = set()
for row in rows:
  for key in row:
    output_types.add(key)
print("output_types:", output_types)

fieldnames = sorted(list(output_types))
print("fieldnames:", fieldnames)

with open("gdalsrsinfo.csv", "w") as f:
  writer = DictWriter(f, delimiter="\t", fieldnames=fieldnames, quoting=QUOTE_ALL)
  writer.writeheader()
  writer.writerows(rows)
print("wrote csv")