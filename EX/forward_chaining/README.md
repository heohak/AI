# Forward Chaining Algorithm for Horn Clauses and Propositional Logic

This program implements a simple forward chaining algorithm to prove conclusions given a set of premises.
The knowledge base is represented as a list of tuples, where each tuple contains a list of premises and a conclusion.

## Input Format

The knowledge base is represented as a list of tuples, where each tuple contains a list of premises and a conclusion.

```python
clauses = [
    (["Premise1", "Premise2"], "Conclusion"),
    ...
    ([], "Fact"),
]
```

queries a.) to c.):

# Use the Algorithm
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
    print(f"Use the Algorithm Results: {results}")

Use the Algorithm Results: [True, True, False]
