#!/usr/bin/env python

# xml parsing help from https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/?ref=lbp
# to run you need to do
# `pip3 install beautifulsoup4`
# `pip3 install lxml`

import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup


def main():
    """ 
    compiles the set of cards in ../ptcg_cockatrice.xml into a cube format

    cube format is just a file with the card names, with repeated card names for commons

    so for example

    Agatha
    Gyarados
    Eevee
    Eevee 
    """
    filename = "../ptcg_cockatrice.xml"

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

                    if '(DFC)' in card_name:
                        continue

                    basic_lands = ["forest", "mountain",
                                   "island", "swamp", "plains"]
                    if card_name.lower() in basic_lands:
                        continue

                    cube_list.append(card_name)

                    for rarity_tag in cockatrice_card:
                        if rarity_tag.name == 'set':
                            if rarity_tag['rarity'] == 'common':
                                cube_list.append(card_name)

    print("Writing to cube file...")
    with open('ptcg_cube.txt', 'w') as f:
        f.write('\n'.join(str(item) for item in cube_list))

    print('Done')


if __name__ == "__main__":
    main()
