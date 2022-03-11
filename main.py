#%%
import json

def load_json(fp):
    with open(fp) as f:
        return json.load(f)

va = load_json("eng-wordlist.json")
va2 = set(va['V'] + va['A'])


rukai = [
    x['gloss'] for x in load_json("all_lang.json")\
        if x['file'].startswith('story/Rukai_Vedai') 
]


en_tokens = '-'.join(
    e.replace('<', '-').replace('>', '-').replace('=', '-').strip('.').replace('.', ' ') for x in rukai for o, e, z in x
).split('-')

en_tokens = set(
    tk.lower() for x in set(en_tokens) for tk in x.split() if not tk.isupper() and tk.isalpha()
)


candidates = en_tokens.intersection(va2)
candidates = sorted((
    (a, 'Verb' if a in va['V'] else 'Adj') for a in candidates), reverse=True, key=lambda x: (x[1], x[0])
)
with open("output.txt", "w") as f:
    for a, b in candidates:
        f.write("{a: <15}\t{b}\n".format(a=a, b=b))
# %%
