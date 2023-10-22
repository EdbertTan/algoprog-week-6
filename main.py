character = (' ',',','.','?','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
code = (' ','--..--', '.-.-.-','..--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.−','−...','−.−.','−..','.','..−.','−−.','....','..','.−−−','−.−','.−..','−−','−.','−−−','.−−.','−−.−','.−.','...','−','..−','...−','.−−','−..−','−.−−','−−..')



sentence = "If the answer was 42, then what was the question?"
sentencex = sentence.split()
eachletter = []
varw = [*sentence]
varx = [i.title() for i in varw]
vary = 0
morsecode = []
for letter1 in varx:
     for letter in character:
          if letter1 == letter:
               vary = 1
               break
          else:
               vary = 0
     if vary == 1:
          varz = character.index(letter)
          codex = code[varz]
          morsecode.append(codex)

morsestring = ""
for codepiece in morsecode:
     morsestring += codepiece
print(morsestring)