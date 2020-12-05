# Pokémon TCG for MTG
A repo for the MTG Pokemon TCG cockatrice XML  and supporting materials.

## New Mechanics and FAQ

### Pokémon

Pokémon is a replacement for the Creature supertype. Pokémon act like Creatures in all respects.

### Evolution

```
Evolve to X {cost}: Pay X. Create a token Pokémon, X, and attach this card to it. The creature on top has all abilities of Pokémon below it, except evolve abilities, and has haste.

Evolve with Y to X {cost}: If you control Y, you Evolve as normal except that you also attach Y to the created token Pokémon.
```

Evolve works a lot like the Mutate mechanic from Ikoria, except you make a token of the appropriate type instead of mutating from your hand.

## Status Effect counters

- Paralysis: the next time this Pokémon would untap, instead remove a paralysis counter from it.

- Confusion: this Pokémon attacks and blocks each turn if able. When blocking, it blocks a random Pokémon. When attacking, it attacks a random opponent or Trainer.

- Poison: at the beginning of its controller's end step, this Pokémon deals 1 damage to its controller. Then, remove a poison counter from it.

- Burn: the next time this Pokémon would deal damage, it also deals that much damage to itself.

- Sleep: This Pokémon cannot attack or block. At the start of its controller's upkeep, its controller flips a coin. If heads, remove all sleep counters from this Pokémon. 

- Frozen: This Pokémon cannot attack or block. If this Pokémon takes damage, remove all frozen counters from it. 