from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_API_KEY_HERE"
)

def get_ai_categories(files):
    prompt = f"""You will categorize a list of filenames into a folder path with up to 3 levels: MainCategory/Subcategory/Detail

Filenames (one per line):
{chr(10).join(files)}

Use these Main Categories: Documents, Pictures, Videos, Audio, Archives, Others

For each Main Category, choose a Subcategory based on the file's purpose or theme (examples):
- Documents: Finance, Legal, Personal_ID, Work
- Pictures: Travel, Family_Events, Screenshots, Profiles
- Videos: Travel, Family_Events, Work
- Audio: Meetings, Music
- Archives: (no subcategory needed, just use Archives)

Within Documents/Finance, further classify into: Bills, Receipts, Budgets (as a third level) when relevant.

For EACH filename, output exactly one line in this format:
filename: MainCategory/Subcategory/Detail

If a third level doesn't apply, just use MainCategory/Subcategory

Example:
Electricity_Bill_January_2025.pdf: Documents/Finance/Bills
Dentist_Receipt_March_2025.pdf: Documents/Finance/Receipts
Passport_Scan_Main_Page.jpg: Documents/Personal_ID
IMG_20240812_Beach_Sunset_HDR.jpg: Pictures/Travel
Backup_Old_Phone_2019.zip: Archives
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[{"role": "user", "content": prompt}]
    )

    ai_text = response.choices[0].message.content
    file_categories = {}
    for line in ai_text.split("\n"):
        if ":" in line:
            filename, category = line.split(":", 1)
            file_categories[filename.strip()] = category.strip()

    return file_categories