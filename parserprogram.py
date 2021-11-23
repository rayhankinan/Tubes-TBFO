from argparse import ArgumentParser
from grammar_processing import read_grammar
from grammar_convert import CFG_to_CNF
from grammar_parser import CYK_parse

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")

    args = argument_parser.parse_args()

    file = open(args.nama_file, "r")
    if CYK_parse(CFG_to_CNF(read_grammar("grammar.txt")), file.read()):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")
    
    file.close()