# Pokémon TCG for MTG

A repo for the MTG Pokemon TCG cockatrice XML and supporting materials.

## New Mechanics and FAQ

### Pokémon

Pokémon is a replacement for the creature type. Pokémon act like creatures in all respects.

### Trainer

Trainer is a replacement for the planeswalker type. Trainers act like planeswalkers in all respects.

### Evolution

```
Evolve: Flip the card over, just like with transform. Double-faced Pokémon cards have the same abilities on both sides (minus the evolve ability), only their P/T is different.

Evolve From X: An alternate casting cost very similar to mutate from Ikoria, but it targets a specific Pokémon. They evolve into the Pokémon on top plus all abilities from under it.

Both the activated ability "Evolve" and the alternate casting cost "Evolve from X" count as evolution. Any triggered abilities that care about a Pokémon evolving will trigger from both types of evolution.
```

## FAQs

**Q: My Bulbasaur evolved into Ivysaur (flipped over) and then [game event] happened, how do I handle it?**

**A**: Pokémon with Evolve abilities act just like any other double-faced cards. [see this link for more info](https://magic.wizards.com/en/articles/archive/feature/double-faced-card-rules-2011-08-29#:~:text=Double-Faced%20Card%20Rules%201%20Double-Faced%20Cards%20in%20General.,...%204%20Double-Faced%20Cards%20and%20Copy%20Effects.%20).

**Q: Machop gets a +1/+1 counter when it evolves, and the Machoke on the back gets the same. When I activate its evolve ability, how many counters does it get?**

**A**: Machoke will get one counter. The "when it evolves" ability isn't triggered until it has completed the evolution, at which point there is only one such ability. The ability on the Machop side triggers when casting a Machoke card for its Evolve From cost.

**Q: Many Pokémon have abilities that reference them by name, such as "1G: Bellsprout gets +1/+1 until end of turn." Evolve Pokémon get all abilities from cards underneath them, do abilities like this still work?**

**A**: Yes, a Weepinbell that uses that ability will still get +1/+1. In MTG, stating a creature's name is the same as saying "this creature." We chose to use Pokémon names more frequently for flavor points.

**Q: Eevee says "Evolve abilities of Pokémon you control cost 1 less to activate." Does that reduce Evolve From costs?**

**A**: No, Evolve From is an alternate casting cost, not an ability.

**Q: Why isn't [insert favorite Pokémon here]] the color I think it should be? Your colors are bad and you should feel bad.**

**A**: To make a balanced cube, we need to have roughly equal representation for each color. Gen 1 has a high concentration of poison and water types. Fire, rock, ground, and electric could all be red. Designing the cube requires us to take some poetic license regarding what color a Pokémon ends up being, and the end result may be different than what any Pokémon would have been in a vaccuum. 

**Q: Why doesn't Spearow have flying?**

**A**: We know it's weird that there are Flying Pokémon, that not all Flying Pokémon have flying, and that you can have flying even if you're not a Flying Pokémon. We didn't want to be constrained to all Flying Pokémon having flying, mostly for balance.
