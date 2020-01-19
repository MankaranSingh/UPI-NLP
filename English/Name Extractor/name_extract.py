import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp('pay $500 to mankaran')

print([(X.text, X.label_) for X in doc.ents])

def expand_person_entities(doc):
    new_ents = []
    for ent in doc.ents:
        # Only check for title if it's a person and not the first token
        if ent.label_ == "PERSON":
            if ent.start != 0:
                # if person preceded by title, include title in entity
                prev_token = doc[ent.start - 1]
                if prev_token.text in ("Dr", "Dr.", "Mr", "Mr.", "Ms", "Ms."):
                    new_ent = Span(doc, ent.start - 1, ent.end, label=ent.label)
                    new_ents.append(new_ent)
                else:
                    # if entity can be parsed as a date, it's not a person
                    pass
        else:
            new_ents.append(ent)
    doc.ents = new_ents
    return doc

# Add the component after the named entity recognizer
# nlp.remove_pipe('expand_person_entities')
nlp.add_pipe(expand_person_entities, after='ner')

doc = nlp('send 60 rupees to john')
[(ent.text, ent.label_) for ent in doc.ents if ent.label_=='PERSON']
