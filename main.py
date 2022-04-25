#%%
import json
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def load_json(fp):
    with open(fp) as f:
        return json.load(f)

va = load_json("eng-wordlist.json")
va2 = set(va['V'] + va['A'])


# rukai = [
#     (x['gloss'], x['free']) for x in load_json("all_lang.json")\
#         if x['file'].startswith('story/Rukai_Vedai') 
# ]
CANDIDATE_VERB_LIST = {}
POS_VERB_LIST = set()
POTENTIAL_POS = set(
    "VB VBD VBG VBN VBP VBZ JJ JJR JJS".split(' ')
)
for x in load_json("all_lang.json"):
    if not x['file'].startswith('story/Rukai_Vedai'): continue

    # PoS tagging
    free = [s for s in x['free'] if s.startswith('#e ')]
    if len(free) == 0: continue
    free = free[0].replace('#e ', '')
    free_pos = nltk.pos_tag(nltk.word_tokenize(free))
    for tk, pos in free_pos:
        if pos in POTENTIAL_POS:
            CANDIDATE_VERB_LIST.setdefault(
                tk, set()
            ).add(pos)

for x in load_json("all_lang.json"):
    if not x['file'].startswith('story/Rukai_Vedai'): continue
    gloss = x['gloss']
    # Gloss tokens
    for o, e, z in gloss:
        e2 = e.replace('<', '-').replace('>', '-').replace('=', '-').strip('.').replace('.', ' ').split('-')
        for tk in e2:
            if tk in CANDIDATE_VERB_LIST:
                POS_VERB_LIST.add(
                    (tk, 
                    ','.join(CANDIDATE_VERB_LIST[tk]),
                    o,
                    e
                    )
                )
            if tk == "STAT":
                POS_VERB_LIST.add(
                    (tk, 
                    "None",
                    o,
                    e
                    )
                )





#%%

# en_tokens = '-'.join(
#     e.replace('<', '-').replace('>', '-').replace('=', '-').strip('.').replace('.', ' ') for x in rukai for o, e, z in x
# ).split('-')

# en_tokens = set(
#     tk.lower() for x in set(en_tokens) for tk in x.split() if not tk.isupper() and tk.isalpha()
# )


# candidates = en_tokens.intersection(va2)
candidates = POS_VERB_LIST
candidates = sorted(POS_VERB_LIST, reverse=False, key=lambda x: (x[0], x[1], x[2])
)
with open("output.txt", "w") as f:
    f.write("{a: <18}\t{b: <18}\t{c: <28}\t{d}\n\n".format(
        a="Verb_from_#e",
        b="PoS_from_#e",
        c="Rukai_gloss",
        d="Eng_gloss"
    ))
    for a, b, c, d in candidates:
        f.write("{a: <18}\t{b: <18}\t{c: <28}\t{d}\n".format(a=a, b=b, c=c, d=d))
# %%
