"""Synthetic question items with one true and one false source.

Every entity is made up, so a model cannot answer from memory. The true and the false value
come from the same generator and the same sentence templates, and which one is "true" is a
coin flip, so nothing but the reliability signal can tell them apart.

An item depends on (seed, index) only, never on the condition, so every condition sees the
same items and the comparisons are paired.
"""
import random

KINDS = ["Observatory", "Viaduct", "Institute", "Archive", "Reservoir", "Foundry", "Lighthouse",
         "Tramway", "Library", "Mill", "Aqueduct", "Conservatory"]
SYL_A = ["Var", "Hal", "Ost", "Bren", "Kel", "Mor", "Tav", "Lin", "Dru", "Fen", "Gal", "Ysk",
         "Pol", "Rav", "Sel", "Tor", "Ulm", "Wex", "Zan", "Cor"]
SYL_B = ["nholt", "vern", "erby", "dask", "mere", "wick", "stow", "leth", "rane", "gard",
         "bury", "moth", "sund", "field", "croft", "hagen"]
TOWN_A = ["Ash", "Birk", "Cald", "Dorn", "Elm", "Fros", "Grim", "Holl", "Ives", "Jarr", "Kest",
          "Lund", "Marr", "Nor", "Oak", "Pell"]
TOWN_B = ["ford", "by", "ham", "ton", "wold", "mouth", "bridge", "stead", "holme", "thorpe"]
FIRST = ["Edda", "Tomas", "Ilse", "Corin", "Maren", "Anselm", "Petra", "Ludo", "Signe", "Osric",
         "Thea", "Bram", "Nell", "Evander", "Runa", "Casimir"]
LAST = ["Marlow", "Venn", "Achterberg", "Sorrel", "Quist", "Hallam", "Deverel", "Okonjo",
        "Brandt", "Lisle", "Tamsin", "Wren", "Strand", "Follet", "Ibarra", "Keane"]

BACKGROUND = [
    "The {E} has been a local landmark for generations.",
    "Guided visits to the {E} run on most weekends.",
    "The {E} is looked after by a small charitable trust.",
    "Much of the original stonework of the {E} survives.",
    "The {E} appears on the regional tourist trail.",
    "Volunteers keep the grounds of the {E} in order.",
    "The {E} was restored after storm damage.",
    "School groups often visit the {E} during term time.",
    "The {E} is closed to the public in midwinter.",
    "A small exhibition tells the story of the {E}.",
    "The {E} is a short walk from the old market square.",
    "Local historians have written at length about the {E}.",
]


def _year(rng):
    true = rng.randint(1815, 1978)
    false = true
    while abs(false - true) < 7:
        false = rng.randint(1815, 1978)
    return str(true), str(false)


def _height(rng):
    true = rng.randint(23, 97)
    false = true
    while abs(false - true) < 5:
        false = rng.randint(23, 97)
    return str(true), str(false)


def _person(rng):
    firsts = rng.sample(FIRST, 2)
    lasts = rng.sample(LAST, 2)
    return "%s %s" % (firsts[0], lasts[0]), "%s %s" % (firsts[1], lasts[1])


def _town(rng):
    heads = rng.sample(TOWN_A, 2)
    tails = rng.sample(TOWN_B, 2)
    return heads[0] + tails[0], heads[1] + tails[1]


def _code(rng):
    letters = rng.sample(["HR", "KR", "LM", "NT", "PD", "RS", "TV", "WB"], 2)
    numbers = rng.sample(range(1000, 9999), 2)
    return "%s-%d" % (letters[0], numbers[0]), "%s-%d" % (letters[1], numbers[1])


ATTRIBUTES = {
    "year": {
        "question": "In what year was the {E} completed?",
        "values": _year,
        "claims": [
            "The {E} was completed in {v}.",
            "Construction of the {E} finished in {v}.",
            "Work on the {E} ended in {v}, when it was formally opened.",
            "Records give {v} as the year the {E} was completed.",
        ],
    },
    "height": {
        "question": "How tall is the main tower of the {E}, in metres?",
        "values": _height,
        "claims": [
            "The main tower of the {E} is {v} metres tall.",
            "The main tower of the {E} rises to a height of {v} metres.",
            "At {v} metres, the main tower of the {E} is visible for miles.",
            "Surveys put the main tower of the {E} at {v} metres.",
        ],
    },
    "designer": {
        "question": "Who designed the {E}?",
        "values": _person,
        "claims": [
            "The {E} was designed by {v}.",
            "{v} drew up the design for the {E}.",
            "The design of the {E} is the work of {v}.",
            "The designer of the {E} was {v}.",
        ],
    },
    "town": {
        "question": "In which town is the {E} located?",
        "values": _town,
        "claims": [
            "The {E} stands in the town of {v}.",
            "The {E} is located in {v}.",
            "The {E} can be found in the town of {v}.",
            "The town of {v} is home to the {E}.",
        ],
    },
    "register": {
        "question": "What is the heritage register number of the {E}?",
        "values": _code,
        "claims": [
            "The {E} is entry {v} in the heritage register.",
            "The heritage register lists the {E} under number {v}.",
            "The {E} carries the heritage register number {v}.",
            "In the heritage register the {E} is recorded as {v}.",
        ],
    },
}
ATTRIBUTE_ORDER = ["year", "height", "designer", "town", "register"]


def make_item(seed: int, index: int) -> dict:
    rng = random.Random("item-%d-%d" % (seed, index))
    entity = "%s%s %s" % (rng.choice(SYL_A), rng.choice(SYL_B), rng.choice(KINDS))
    attribute = ATTRIBUTE_ORDER[index % len(ATTRIBUTE_ORDER)]
    spec = ATTRIBUTES[attribute]
    true_value, false_value = spec["values"](rng)
    claim_true, claim_false = rng.sample(spec["claims"], 2)
    background = rng.sample(BACKGROUND, 6)

    def doc(claim, value, filler):
        sentences = [filler.format(E=entity), claim.format(E=entity, v=value)]
        if rng.random() < 0.5:
            sentences.reverse()
        return " ".join(sentences)

    docs = [
        {"role": "T", "text": doc(claim_true, true_value, background[0])},
        {"role": "F", "text": doc(claim_false, false_value, background[1])},
        {"role": "D", "text": "%s %s" % (background[2].format(E=entity), background[3].format(E=entity))},
        {"role": "D", "text": "%s %s" % (background[4].format(E=entity), background[5].format(E=entity))},
    ]
    rng.shuffle(docs)
    # Balance which of the two conflicting sources comes first, so position bias cancels.
    true_first = ((index // len(ATTRIBUTE_ORDER)) + seed) % 2 == 0
    order = [d["role"] for d in docs if d["role"] in ("T", "F")]
    if (order[0] == "T") != true_first:
        a = next(i for i, d in enumerate(docs) if d["role"] == "T")
        b = next(i for i, d in enumerate(docs) if d["role"] == "F")
        docs[a], docs[b] = docs[b], docs[a]
    for position, source in enumerate(docs, 1):
        source["id"] = "S%d" % position
    return {
        "item_id": "s%d-i%d" % (seed, index),
        "entity": entity,
        "attribute": attribute,
        "question": spec["question"].format(E=entity),
        "true": true_value,
        "false": false_value,
        "sources": docs,
        "false_position": next(s["id"] for s in docs if s["role"] == "F"),
        "forge_pick": rng.randrange(10 ** 6),
    }


def make_items(seed: int, count: int) -> list:
    return [make_item(seed, index) for index in range(count)]
