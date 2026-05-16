import json

# =========================
# LOAD RAW CATALOG
# =========================

with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print("Total assessments:", len(catalog))

clean_catalog = []

# =========================
# PROCESS ITEMS
# =========================

for item in catalog:

    name = item.get("name", "")

    url = item.get("url", "") or item.get("link", "")

    description = item.get("description", "")

    duration = item.get("duration", "")

    job_levels = item.get("job_levels", [])

    languages = item.get("languages", [])

    test_types = item.get("test_types", []) or item.get("keys", [])

    remote = item.get("remote", "")

    adaptive = item.get("adaptive", "")

    # =========================
    # STRONG SEARCHABLE TEXT
    # =========================

    search_text = f"""
    Assessment Name: {name}

    Assessment Type:
    {' '.join(test_types)}

    Description:
    {description}

    Technical Skills:
    {description}

    Programming Skills:
    {description}

    Software Engineering:
    {description}

    Communication Skills:
    {description}

    Leadership Skills:
    {description}

    Collaboration Skills:
    {description}

    Job Levels:
    {' '.join(job_levels)}

    Languages:
    {' '.join(languages)}

    Duration:
    {duration}

    Remote Support:
    {remote}

    Adaptive Testing:
    {adaptive}
    """

    cleaned_item = {
        "name": name,
        "url": url,
        "description": description,
        "duration": duration,
        "job_levels": job_levels,
        "languages": languages,
        "test_types": test_types,
        "remote": remote,
        "adaptive": adaptive,
        "search_text": search_text
    }

    clean_catalog.append(cleaned_item)

# =========================
# SAVE CLEAN CATALOG
# =========================

with open(
    "clean_catalog.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        clean_catalog,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Clean catalog saved successfully!")
print(clean_catalog[0])

