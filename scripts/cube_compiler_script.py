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

                        if card_name == 'Mewtwo, Redeemed':
                            continue

                        # skip DFCs since they don't need to be in the cube file
                        if '(DFC)' in card_name:
                            continue

                        basicland = False
                        for type_tag in cockatrice_card:
                            if type_tag.name == 'type':
                                if 'Basic Land' in type_tag.string:
                                    basicland = True

                        if basicland:
                            continue

                        # append (PKTO) to the card name to work with dr4ft
                        card_name = f"{card_name} (PKTO)"

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
