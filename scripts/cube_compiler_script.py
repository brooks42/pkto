#!/usr/bin/env python

# xml parsing help from https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/?ref=lbp
# to run you need to do
# `pip3 install beautifulsoup4`
# `pip3 install lxml`

import sys

from bs4 import BeautifulSoup


def main():
    """ 
    compiles the set of cards in ../pkto_cockatrice.xml into a cube format

    cube format is just a file with the card names, with repeated card names for commons

    so for example

    Agatha
    Gyarados
    Eevee
    Eevee 
    """

    try:
        # sys.argv[1] is expected to be -f for bash reasons
        filename = sys.argv[2]

        # open the input file as XML, input is assumed to be a cockatrice card file
        print("Loading file...")
        cube_list = list()

        with open(filename, "r") as f:
            soup_obj = BeautifulSoup(f, "xml")

            # grab the list of cards out of the input cockatrice xml file
            all_cards = soup_obj.findAll("card")

            for index in range(len(all_cards)):

                # grab the info and transform this into the Card instance format above
                cockatrice_card = all_cards[index]

                for name_tag in cockatrice_card:
                    if name_tag.name == 'name':
                        card_name = name_tag.string

                        # skip DFCs since they don't need to be in the cube file
                        if '(DFC)' in card_name:
                            continue

                        basic_lands = ["forest", "mountain",
                                       "island", "swamp", "plains"]
                        if card_name.lower() in basic_lands:
                            continue

                        # also catch forest(a) etc
                        basic_lands_a = [sub + " (a)" for sub in basic_lands]
                        if card_name.lower() in basic_lands_a:
                            continue

                        basic_lands_b = [sub + " (b)" for sub in basic_lands]
                        if card_name.lower() in basic_lands_b:
                            continue

                        # append [PKTO] to the card name if it doesn't already end in PKTO
                        if not card_name.endswith('[PKTO]'):
                            card_name = f"{card_name} [PKTO]"

                        # only append non-token rarities, and append twice if rarity is common
                        for rarity_tag in cockatrice_card:
                            if rarity_tag.name == 'set':

                                if rarity_tag['rarity'] == 'token':
                                    continue

                                cube_list.append(card_name)

                                if rarity_tag['rarity'] == 'common':
                                    cube_list.append(card_name)

        cube_list.sort()
        print(f'Writing {len(cube_list)} cards to cube file...')
        with open('pkto_cube.txt', 'w') as f:
            f.write('\n'.join(str(item) for item in cube_list))

        print('Done')

    except Exception as e:
        print(f"Exception: {e}")
        print("Usage: python3 cube_compiler_script -f filename")


if __name__ == "__main__":
    main()
