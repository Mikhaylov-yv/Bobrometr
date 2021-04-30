import os
import scr.bobr_nlp as nlp



def test_nalp_otv():
    os.chdir('..')
    print(os.path.abspath(os.curdir))
    print(nlp.get_ansver('Привет'))