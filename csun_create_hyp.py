#This script creates a transcript of the recognized audio by AT&T Mashup
#in a similar fashion as csun_pizza_transcript.ref
#This transcript of the recognized audio is then compared to a transcript of the
#actual utterances and a resulting table of success rate of the speech recognition
#included substitions, deletions, and insertions is produced using SClite (in post processing)
#Changing the specificity of the grammar, increases the success rate of the
#speech recognition produced from the AT&T mashup.

import re #to find regexes
import os #necessary for executing shell commands
import glob #to find file with filenames with a matching pattern

path = "/Users/clairesun/desktop/JBS_Generic" # filepath

target = open("JBS_generic.hyp", "w+") #we write to this file
emma_file_path = glob.glob(path + '/*.emma') #pathnames for the emma files
found = False #flag
for file in emma_file_path:
    filename = os.fsdecode(file) #extracts filename from directory
    if filename.endswith(".emma"):
        file_object = open(filename, "r") #reads the file if it is .emma

        for line in file_object:
            if "<emma:literal>" in line: #if the line contains this bracket
                literal =  str(re.findall("<emma:literal>(.*?)</emma:literal>", line))
                # extract all text between emma brackets (this is the transcription resulting from the audiofiles from the AT&T Mashup)
                found = True
                target.write(literal[2:-2] + " (" + filename[37:-5] + ")\n")
                # write this text into the new file

        if found == False:
            target.write("(" + filename[37:-5] + ")\n") #writes filename at end of the transcription
        found = False
target.close()
