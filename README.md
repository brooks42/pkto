# Pokémon TCG for MTG

A repo for the MTG Pokemon TCG cockatrice XML and supporting materials.

## New Mechanics

### Pokémon

Pokémon is a replacement for the creature type. Pokémon behave like creatures in all respects.

### Trainer

Trainer is a replacement for the planeswalker type. Trainers behave like planeswalkers in all respects.

### Evolution

Evolve - An activated ability that turns the card over, just like transform. Double-faced Pokémon cards have the same abilities on both sides (minus the evolve ability); only their power, toughness, and name are different. Pokémon with Evolve act just like any other double-faced cards. [See this link for more info](https://mtg.fandom.com/wiki/Double-faced_card).

Evolve from - An alternate casting cost very similar to mutate from Ikoria, but it targets a specific Pokémon. They evolve into the Pokémon on top plus all non-evolve abilities from under it. Pokémon with Evolve from act just like any other merged permanents. [See this link for more info](https://mtg.fandom.com/wiki/Merge).

Both "Evolve" and "Evolve from" count as evolution/evolving. Any triggered abilities that care about Pokémon evolving will trigger from both types of evolution. If a card affects what you can pay "to evolve Pokémon" it applies to both types of evolution. 

## FAQs

**Q: If I kill a Pokémon in response to it being targeted by a spell that was cast for its Evolve from cost, what happens?**

**A**: The Evolve from spell will still resolve, but it will enter the battlefield on its own, won't trigger any abilities that care about evolution, and won't be considered evolved.

**Q: Many Pokémon have abilities that reference them by name, such as "1G: Bellsprout gets +1/+1 until end of turn." Pokémon with Evolve from get all abilities from cards underneath them, do abilities like this still work?**

**A**: Yes, a Weepinbell that uses that ability will still get +1/+1. Referencing a permanent's name is the same as saying "this permanent." We chose to use Pokémon names more frequently for flavor points.

**Q: Why isn't [insert favorite Pokémon here] the color I think it should be? Your colors are bad and you should feel bad.**

**A**: We want an equal number of cards in each color in the cube. Gen 1 has a high concentration of poison and water types. Fire, rock, ground, and electric could all be red. Designing the cube requires us to take some poetic license regarding what color a Pokémon ends up being, and the end result may be different than what any Pokémon would have been in a vacuum. 

**Q: Why doesn't Spearow have flying?**

**A**: We know it's weird that there are Flying Pokémon, that not all Flying Pokémon have flying, and that you can have flying even if you're not a Flying Pokémon. We didn't want to be constrained to all Flying Pokémon having flying, for flavor and variety.

**Q: Ditto can become a copy of an evolved Pokémon. Does it get the abilities from the cards under the evolved Pokémon?**

**A**: Yes, abilities of all cards in a merged permanent are copiable characteristics. For example, a copy of Kakuna with a Weedle under it will have deathtouch.

**Q: Are copies of evolved Pokémon considered evolved?**

**A**: No, being a merged permanent (evolved) is not itself a copiable characteristic. Copies are not evolved and have evolved 0 times.

**Q: What if Ditto copies a Pokémon with Evolve? Will it flip to the other side?**

**A**: No, cards that become copies of transforming double-faced cards do not gain the back face. Activating the Evolve ability will not flip the card and will not trigger abilities that care about evolution.

**Q: If I make a token copy of a Pokemon with Evolve with Mewtwo, can that copy activate it and flip to the back face?**

**A**: Yes, unlike cards that become copies, token copies of transforming double-faced cards can transform.

**Q: If I have Raticate evolved onto Rattata and Raticate dies, can it return Rattata to the battlefield?**

**A**: Yes. Dies means "goes to the graveyard" so when the ability triggers both cards are in the graveyard and Rattata is a legal target.

**Q: If Ninetales dies with its attack trigger on the stack, what happens?**

**A**: Ninetales's controller may still pay 2R and discard a card to take control of the targeted Pokémon. The Pokémon will tap, but will not be attacking, as Ninetales is no longer attacking anything.

**Q: What does winning a fight mean on Double Kick?**

**A**: The Pokémon you control will win the fight if it is still on the battlefield after the fight resolves and the other Pokémon is not.

**Q: When do I choose the target for the second fight in Double Kick?**

**A**: You choose the target when the trigger goes on the stack, after your Pokémon wins the first fight.
