def forward_chaining(clauses, query):
    inferred = set()
    new_symbols = True  # loop while we infer new stuff
    while new_symbols:
        new_symbols = False
        for premises, conclusion in clauses:
            if conclusion not in inferred:
                if all(p in inferred for p in premises):
                    if conclusion == query:
                        return True
                    inferred.add(conclusion)
                    new_symbols = True
    return False  # no new symbols, query symbol was not seen





if __name__ == '__main__':
    clauses = [
        (["P"], "Q"),
        (["L", "M"], "P"),
        (["B", "L"], "M"),
        (["A", "P"], "L"),
        (["A", "B"], "L"),
        ([], "A"),
        ([], "B"),
    ]

    query = "Q"
    print(forward_chaining(clauses, query))

    clauses = [
        ([], "Egg_is_fragile"),
        ([], "Egg_falls_down"),
        ([], "Egg_contains_liquid"),
        (["Egg_is_fragile", "Egg_falls_down"], "Egg_breaks"),
        (["Egg_breaks", "Egg_contains_liquid"], "Egg_makes_a_mess"),
        (["Egg_is_spoiled", "Egg_breaks"], "Egg_smells"),
    ]

    queries = ["Egg_breaks", "Egg_makes_a_mess", "Egg_smells"]
    results = [forward_chaining(clauses, query) for query in queries]

    print(results)

