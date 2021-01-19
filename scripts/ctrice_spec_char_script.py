#!/usr/bin/env python

# script for adding special characters to the passed cockatrice set file. Special characters include accents and line breaks.

# xml parsing help from https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/?ref=lbp
# to run you need to do
# `pip3 install beautifulsoup4`
# `pip3 install lxml`

import argparse
import datetime

from bs4 import BeautifulSoup

def main():
    """
    Usage:
        - python set_editor_script.py [options] -i input_file -o output_file

    Example:
        python set_editor_script.py -i ../ptcg_cockatrice.xml -o cockatrice2.xml
    """
    # TODO: we need a version of this functionality that smashes a cockatrice file w/ 
    # a mtg set file to populate images etc but update the mtg set file with the updated
    # cockatrice info
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i', '--input', type=str, required=True, help='input file')
    parser.add_argument('-o', '--output', type=str, required=True, help='output file, cannot be the same as input file')

    args = parser.parse_args()

    # validate args
    if (args.input == args.output):
        print('Error: input file cannot be the same as output file.')
        return

    # open the input file as XML, input is assumed to be a cockatrice card file
    with open(args.input, 'r') as f: 
        data = f.read()
        xmlObjects = BeautifulSoup(data, "xml")
        
        # grab the list of cards out of the input cockatrice xml file
        allCards = xmlObjects.findAll("card")
        print(f'Retrieved {len(allCards)} cards')

        for index in range(len(allCards)):
            print(f'card {index}:')
            
            # take the card's text and replace it with a special-character prettified version
            cockatrice_card = allCards[index]
            # cockatrice_card.text = cockatrice_card.text.replace('Pokemon', 'Pokémon')
            for tag in cockatrice_card:
                if tag.name == 'text':
                    print("===")
                    print(tag)
                    unicode_string = tag.string
                    if unicode_string != None:
                        unicode_string = tag.string.replace('Pokemon', 'Pokémon') # in case we miss any Pokemon w/ special character
                        unicode_string = tag.string.replace('\n\t\t\t\t', '\n')
                        tag.string.replace_with(unicode_string)
                        print("===")
                        print(tag)
                    print("===")
            print(cockatrice_card.get('text'))

        # then open the output file
        with open(args.output, 'w') as output_file:
            output_file.write(str(xmlObjects))

    print('Done')

if __name__ == "__main__":
    main()
