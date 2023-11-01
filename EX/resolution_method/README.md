# Simple Resolution Prover

This program implements a simple resolution prover to determine if a given sentence is entailed by a knowledge base.

## Unicorn Knowledge Base

The knowledge base for the unicorn problem is represented in CNF (Conjunctive Normal Form) as follows:

KB = [
    ['-Mythical', 'Immortal'],
    ['Mythical', 'Mortal'],
    ['Mythical', 'Mammal'],
    ['-Immortal', '-Mammal', 'Horned'],
    ['-Horned', 'Magical']
]


## Unicorn Queries

The results for the unicorn queries are as follows:

1. Is the unicorn mythical? `False`
2. Is the unicorn magical? `True`
3. Is the unicorn horned? `True`

## Forward Chaining

The forward chaining solver from the previous assignment does not work for the unicorn problem because forward chaining is a data-driven approach. 
It starts with the known facts in the knowledge base and applies the inference rules to derive new facts until the query is answered or no new facts can be derived. 
In the unicorn problem, there are complex relationships and negations that cannot be easily handled by forward chaining.
