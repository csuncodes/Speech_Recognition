#This script systematically sends .wav audio files to AT&T Mashup with a provided
# grammar. The resulting transcription of the audio files is compared to
#the actual transcription in csun_create_hyp.py
#Changing the specificity of the grammar, increases the success rate of the
#speech recognition produced from the AT&T mashup.


import os #necessary for executing shell commands
import glob #to find file with filenames with a matching pattern

path = "/Users/clairesun/desktop/audio" #folder with audio files

directory = glob.glob(path + '/*.wav') #pathnames for the audio files

output_dir= "reco_results/"
os.system("mkdir "+ output_dir) #creates new directory called "output_dir" for the resulting .hyp files

grammar = 'generic'

url = "'http://service.interactions.net/smm/watson?cmd=rawoneshot&appname=pizza&grammar='" + grammar + "'&uuid=FD727325512711E7B18B777444234D2E&resultFormat=emma'"
#url of the AT&T Speech Mashup website which performs speech recognition by referencing the audio with the
#provided grammar

for file in directory:
    filename = os.fsdecode(file) #extracts the filename from the directory
    if filename.endswith(".wav"):
        fileout = filename.replace(".wav",".emma") #converts .wav audio files to .emma files (AT&T Mashup takes .emma as input)
        output_file = fileout[31:]
        wget_call = "wget --post-file=" +  filename + " --header 'Content-Type: audio/wav' --server-response " + url + " -O " + output_file
        #terminal command to send audio files to AT&T Mashup
        os.system(wget_call)
