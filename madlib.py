import random
from sample_madlibs import code, hp, hungergames, zombie
if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()