#!/usr/bin/python3

import pprint

with open("files.txt", "w") as f:
    f.writelines(['"Master, you are wonderful!" A student, taking his leave, gazed ardently at the patriarchal sage. "You have renounced riches and comforts to seek God and teach us wisdom!" It was well-known that Bhaduri Mahasaya had forsaken great family wealth in his early childhood, when single-mindedly he entered the yogic path.122', '"You are reversing the case!" The saint\'s face held a mild rebuke. "I have left a few paltry rupees, a few petty pleasures, for a cosmic empire of endless bliss. How then have I denied myself anything? I know the joy of sharing the treasure. Is that a sacrifice? The shortsighted worldly folk are verily the real renunciates! They relinquish an unparalleled divine possession for a poor handful of earthly toys!"'])

d = {"v": 0, "w": 0, "u": 0, "d": 0}
with open("files.txt", "r") as f:
    for i in f.readlines():
        for j in i.split():
            print(j[::-1], end=" ")
            
            d["w"] += 1            
            for k in j:
                if k.isdigit():
                    d["d"] += 1
                elif k in "aeiouAEIOU":
                    d["v"] += 1
                if k.isupper():
                    d["u"] += 1

pprint.pprint(d)
