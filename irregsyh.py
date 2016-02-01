#!/usr/bin/python

import json
from pprint import pprint
from os.path import expanduser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[31m'
    UNDERLINE = '\033[4m'

def printTestVerb(verbRaw):
    print "**************************************"
    print "Entries for << " + bcolors.OKBLUE + verb["baseWord"] + "  ::  " + verb["baseTranslation"] + bcolors.ENDC + " >>"
    getAndValidateEntry(verbRaw["simplePast"], "Simple Past")
    getAndValidateEntry(verbRaw["pastParticiple"], "Past Participle")
    printFullEntry(verbRaw)

def getAndValidateEntry(simplePastRaw, timeVerb):
    counter = 0
    while counter < 2:
        entry = raw_input(timeVerb + " [-h for help]: ")
        while True:
            if entry == '-h':
                print "Example: " + simplePastRaw["example"].replace(simplePastRaw["word"], "_____")
                entry = raw_input(timeVerb + " [-h for help]: ")
            else:
                if validateEntry(entry, simplePastRaw["word"]):
                    counter = 1000
                else:
                    counter += 1
                break

def validateEntry(userEntry, verb):
    result = userEntry == verb
    if result:
        print bcolors.OKGREEN + "Good" + bcolors.ENDC
    else:
        print bcolors.FAIL + "You are wrong!" + bcolors.ENDC
    return result;

def printFullEntry(verb):
    print bcolors.WARNING + "[[[ " + verb["baseWord"] + "  =>  " + verb["simplePast"]["word"] + "  =>  " + verb["pastParticiple"]["word"] + " ]]]" + bcolors.ENDC

verbs_file_path = expanduser('~') + '/.irregsyh/user-verbs.json'

with open(verbs_file_path) as data_file:
    data = json.load(data_file)

for verb in data['verbs']:
    printTestVerb(verb)
