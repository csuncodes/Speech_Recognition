# Speech_Recognition

This is a small project for evaluating speech recognition performance conducted on .wav audio files for a class on dialog systems. 
This project can be seen as being constructed into three steps:
  
  1. Going through a directory of audio files, each with a different pizza order, and iteratively converting them to .emma files and sending then through the AT&T Mashup - a speech recognizer tool that transcribes utterances according to a provided grammar.

  2. Writing all the resulting transcriptions to a new file. All transcriptions of the audio files are written between <emma:literal> brackets. These transcriptions were extracted using regexes.

  3. The resulting transcriptions are then compared to real transcriptions of the audio files to determine the success rate of the speech recognition. Both files are sent through SClite, which compares similarities between the two transcriptions including percentages for inserted or deleted words. The result is to show the importance of constructing a good grammar for good speech recognition. By changing the grammar, the success rate of the produced transcription and real transcription increases. 
  
Step 1 is done by csun_extraction.py
Step 2 is done by csun_create_hyp.py 

There are many file types in this project due to the various software tools used. All are able to be read in a text editor.

.pra, .dtl, and .sys files are all the results from SClite and show various statistics of the transcriptions.

.hyp files are necessary as input for SClite.

.emma files are necessary as input for AT&T Mashup.

.wbnf file is needed as the grammar of the AT&T Mashup and is uploaded manually.
