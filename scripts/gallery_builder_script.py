#!/usr/bin/env python

# xml parsing help from https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/?ref=lbp
# to run you need to do
# `pip3 install beautifulsoup4`
# `pip3 install lxml`

import sys

from bs4 import BeautifulSoup


def main():
    """ 
    compiles the set of cards in ../pkto_cockatrice.xml into a format the gallery can display them in, 
    which is more-or-less their order in the cockatrice file itself

    format is just a file with `"{card_name}.png",`

    so for example

    "Eevee.png",
    "Gyarados.png",
    "Agatha.png",
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

                        # point to the file
                        card_name = f"\"{card_name}.png\","

                        cube_list.append(card_name)

        print(f'Writing {len(cube_list)} cards to gallery file...')
        with open('pkto_cube.txt', 'w') as f:
            f.write('\n'.join(str(item) for item in cube_list))

        print('Done')

    except Exception as e:
        print(f"Exception: {e}")
        print("Usage: python3 gallery_builder_script.py -f filename")


if __name__ == "__main__":
    main()
