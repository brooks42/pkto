#!/usr/bin/env python

# xml parsing help from https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/?ref=lbp
# to run you need to do
# `pip3 install beautifulsoup4`
# `pip3 install lxml`

import argparse
import datetime
import pickle
import urllib.parse

from bs4 import BeautifulSoup


def main():
    """
    Usage:
        - python3 set_pic_url_script.py
    """

    # open the input file as XML, input is assumed to be a cockatrice card file
    print("Loading file...")
    with open("../ptcg_cockatrice.xml", "r") as f:
        soup_obj = BeautifulSoup(f, "xml")

        # grab the list of cards out of the input cockatrice xml file
        all_cards = soup_obj.findAll("card")

        for index in range(len(all_cards)):

            # grab the info and transform this into the Card instance format above
            cockatrice_card = all_cards[index]

            for tag in cockatrice_card:
                if tag.name == 'name':
                    card_name = tag.string

            cockatrice_card.set[
                'picURL'] = "https://" + urllib.parse.quote(f"raw.githubusercontent.com/brooks42/ptcg/main/images/cards/{card_name}.png")

    print("Writing file with updated URLs...")
    with open('../ptcg_cockatrice.xml', 'w') as f:
        f.write(str(soup_obj))

    print('Done')


if __name__ == "__main__":
    main()
