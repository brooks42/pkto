# Pokémon TCG for MTG

A repo for the MTG Pokemon TCG cockatrice XML and supporting materials.

## New Mechanics and FAQ

### Pokémon

Pokémon is a replacement for the Creature supertype. Pokémon act like Creatures in all respects.

### Trainer

Trainer is a replacement for the Planeswalker supertype. Trainers act like Planeswalkers in all respects.

### Evolution

```
Evolve to X: flip the card over, just like with transform. Dual-faced Pokémon cards have the same abilities on both sides (minus the evolve ability), only their P/T is different.

Evolve from X: If you control X, put this card on top of it as though it evolved into this card.
```

Evolve works a lot like the Mutate mechanic from Ikoria, except you make a token of the appropriate type instead of mutating from your hand.

## FAQs

**Q: My Bulbasaur evolved into Ivysaur (flipped over) and then [game event] happened, how do I handle it?**

**A**: Pokémon with Evolve to X abilities act just like any other dual-faced cards. [see this link for more info](https://magic.wizards.com/en/articles/archive/feature/double-faced-card-rules-2011-08-29#:~:text=Double-Faced%20Card%20Rules%201%20Double-Faced%20Cards%20in%20General.,...%204%20Double-Faced%20Cards%20and%20Copy%20Effects.%20).

**Q: Why doesn't Spearow have flying?**

**A**: We know it's weird that there are Flying Pokémon, that not all Flying Pokémon have flying and that you can have flying even if you're not a Flying Pokémon. We didn't want to be constrained to all Flying Pokémon having flying, mostly for balance.
