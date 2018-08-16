#!/usr/bin/python

import sys, getopt

USAGE_MESSAGE = """You have to pass three arguments as shown bellow.

usage: main.py --licitacoes <file_path> --participantes <file_path> --propostas <file_path> --dbconf <file_path>

If you don't know what these parameters are, try main.py --help.
"""

HELP_MESSAGE = """usage: main.py --licitacoes <file_path> --participantes <file_path> --propostas <file_path> --dbconf <file_path>

These are the required arguments:
   licitacao           Path to the CSV file with Licitação table downloaded from sagres
   participantes       Path to the CSV file with Participantes de Licitação table downloaded from sagres
   propostas           Path to the CSV file with Propostas de Licitação table downloaded from sagres
   dbconf              Path to the XML file with your MySql configurations
"""

def main(argv):

   licitacao_csv_path = ''
   participantes_csv_path = ''
   propostas_csv_path = ''
   db_conf_path = ''

   try:
      opts, args = getopt.getopt(argv,"h",["help=", "licitacoes=", "participantes=", "propostas=", "dbconf="])
   except getopt.GetoptError:
      print (USAGE_MESSAGE)
      sys.exit(2)

   if not len(opts):
      print (USAGE_MESSAGE)

   for opt, arg in opts:
      if opt in ("-h", "--help"):
         print (HELP_MESSAGE)
         sys.exit()
      elif opt == "--licitacao":
         licitacao_csv_path = arg
      elif opt == "--participantes":
         participantes_csv_path = arg
      elif opt == "--propostas":
         propostas_csv_path = arg
      elif opt == "--dbconf":
         db_conf_path = arg
   

if __name__ == "__main__":
   main(sys.argv[1:])