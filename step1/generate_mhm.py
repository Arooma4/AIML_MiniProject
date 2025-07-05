import json

def generate_mhm(json_file, mhm_output):
    with open(json_file) as f:
        data = json.load(f)

    with open(mhm_output, "w") as f:
        f.write(f'''
human height {data["height"]}
macrodetails-universal-shoulderWidth {data["shoulderWidth"]}
macrodetails-universal-hipCircum {data["hipWidth"]}
''')

    print(f"✅ MHM file saved as {mhm_output}")

# Run it
generate_mhm("output_measurements.json", "user_model.mhm")
