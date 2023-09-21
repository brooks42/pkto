# Pokémon TCG for MTG

A repo for the MTG Pokemon TCG cockatrice XML and supporting materials.

## New Mechanics

### Pokémon

Pokémon is a replacement for the creature type. Pokémon behave like creatures in all respects.

### Trainer

Trainer is a replacement for the planeswalker type. Trainers behave like planeswalkers in all respects.

### Fossil

Fossil is a replacement for the escape mechanic. Fossil behaves like escape in all respects.

### Evolution

Evolve - An activated ability that turns the card over, just like transform. Double-faced Pokémon cards have the same abilities on both sides (minus the evolve ability), only their power, toughness, and name are different.

Evolve From - An alternate casting cost very similar to mutate from Ikoria, but it targets a specific Pokémon. They evolve into the Pokémon on top plus all non-evolve abilities from under it.

Both "Evolve" and "Evolve From" count as evolution/evolving. Any triggered abilities that care about Pokémon evolving will trigger from both types of evolution. If a card affects what you can pay "to evolve Pokémon" it applies to both types of evolution. 

A Pokémon is considered evolved if it is the back side of a card with an evolve ability or it was cast using its Evolve From cost. A Pokémon is considered unevolved if it is the front side of a card with an evolve ability, it is a card with an Evolve From cost that was cast using its standard mana cost, or it is a card without Evolve or Evolve From.

## FAQs

**Q: My Bulbasaur evolved into Ivysaur (flipped over) and then [game event] happened, how do I handle it?**

**A**: Pokémon with Evolve abilities act just like any other double-faced cards. [See this link for more info](https://magic.wizards.com/en/articles/archive/feature/double-faced-card-rules-2011-08-29#:~:text=Double-Faced%20Card%20Rules%201%20Double-Faced%20Cards%20in%20General.,...%204%20Double-Faced%20Cards%20and%20Copy%20Effects.%20).

**Q: If I kill a Pokémon in response to it being targeted by a spell that was cast for its Evolve From cost, what happens?**

**A**: The Evolve From spell will still resolve, but it will enter battlefield on its own, won't trigger any abilities that care about evolution, and won't be considered evolved.

**Q: Many Pokémon have abilities that reference them by name, such as "1G: Bellsprout gets +1/+1 until end of turn." Evolve Pokémon get all abilities from cards underneath them, do abilities like this still work?**

**A**: Yes, a Weepinbell that uses that ability will still get +1/+1. In MTG, stating a creature's name is the same as saying "this creature." We chose to use Pokémon names more frequently for flavor points.

**Q: Why isn't [insert favorite Pokémon here] the color I think it should be? Your colors are bad and you should feel bad.**

**A**: To make a balanced cube, we need to have roughly equal representation for each color. Gen 1 has a high concentration of poison and water types. Fire, rock, ground, and electric could all be red. Designing the cube requires us to take some poetic license regarding what color a Pokémon ends up being, and the end result may be different than what any Pokémon would have been in a vaccuum. 

**Q: Why doesn't Spearow have flying?**

**A**: We know it's weird that there are Flying Pokémon, that not all Flying Pokémon have flying, and that you can have flying even if you're not a Flying Pokémon. We didn't want to be constrained to all Flying Pokémon having flying, mostly for balance.

**Q: Hyper Beam says "Enchant target Pokémon without an Evolve ability." Does that mean I can't use it on Dragonite, which has Evolve From?**

**A**: Evolve is an activated ability, while Evolve From is an alternate casting cost. Any Pokémon with Evolve From can be enchanted by Hyper Beam.

**Q: Beedrill and Ditto can make copies of evolved Pokémon. Do those copies get the abilities from the cards under the evolved Pokémon?**

**A**: Yes, abilities of all cards in a merged permanent are copiable characteristics. For example, a copy of Beedrill with a weedle under it will have deathtouch.

**Q: Are copies of evolved Pokémon considered evolved?**

**A**: No, being a merged permanent (evolved) is not itself a copiable characteristic. Copies are not evolved and have evolved 0 times.

**Q: What if Ditto copies a Pokémon with an Evolve ability? Will it flip to the other side?**

**A**: No, the reverse face of a DFC is not a copiable characteristic. This will not trigger abilities that care about evolution either.

**Q: Solar Beam says "Destroy target artifact, target enchantment, target trainer, or target token." If I overload it, do I destroy each artifact, enchantment, trainer, and token?**

**A**: No, overload replaces all instances of "target" with "each." This means you choose between destroying each artifact, each enchantment, each trainer, or each token.

**Q: If I have Raticate evolved onto Rattata and Raticate dies, can it return Rattata to the battlefield?**

**A**: Yes. Dies means "goes to the graveyard" so when the ability triggers both cards are in the graveyard and Rattata is a legal target.

**Q: If Ninetales dies with its attack trigger on the stack, what happens?**

**A**: Ninetales's controller may still pay 1RR and discard a card to take control of the targeted Pokémon. The Pokémon will tap, but will not be attacking, as Ninetales is no longer attacking anything.

**Q: If I make a token copy of a Pokemon with an Evolve ability with Mewtwo, can that copy activate it and flip to the back face?**

**A**: Yes, token copies of transforming double-faced cards can transform.

**Q: Do Pokémon die between the fights for Double Kick?**
**A**: Double kick creates a delayed trigger that goes on the stack after the first fight resolves. State based actions are checked while that trigger is on the stack, so Pokémon can die before the second fight occurs.

**Q: When do I choose the target for the second fight in Double Kick?**
**A**: You choose the target when the trigger goes on the stack, after the first fight resolves but before state based actions are checked.
