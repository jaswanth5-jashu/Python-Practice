s = "This is a sample sentence to shuffle"
import random
i = s.split()
random.shuffle(i)
print(' '.join(i))