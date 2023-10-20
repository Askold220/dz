from translate import Translator

text = """
Моя улюблена гра - це "Fortnite".
"""

translator = Translator(from_lang="uk", to_lang="en")
end_text = translator.translate(text)

with open("translation.txt", "w", encoding="utf-8") as file:
    file.write(end_text)

print(end_text)
