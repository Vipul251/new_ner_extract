import spacy
nlp = spacy.load("en_core_web_sm")

def extract_names(text):
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return names