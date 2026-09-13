from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_API_KEY_HERE"
)

def get_ai_categories(files):
    prompt = f"""You will categorize a list of filenames into a MAIN category and a SUBCATEGORY.

Filenames (one per line):
{chr(10).join(files)}

For EACH filename, output exactly one line in this format:
filename: MainCategory/Subcategory

Main categories: Images, Videos, Documents, Music, Code, Others
Subcategories should describe the specific purpose (e.g. Screenshots, Personal, Work, Study, Memes)

Example:
resume.pdf: Documents/Work
funny_meme.png: Images/Memes
lecture_notes.pdf: Documents/Study
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