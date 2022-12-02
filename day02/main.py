#/usr/bin/env python3

class Play:
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, type(self))

    def __lt__(self, __o: object) -> bool:
        if type(self) == type(__o):
            return False
        if type(self) == Rock:
            return True if type(__o) == Paper else False
        if type(self) == Paper:
            return True if type(__o) == Scissors else False
        if type(self) == Scissors:
            return True if type(__o) == Rock else False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

class Rock(Play):
    value = 1

class Paper(Play):
    value = 2

class Scissors(Play):
    value = 3

# Part 1
A = X = Rock()
B = Y = Paper()
C = Z = Scissors()

def score(other, me):
    score = 0
    if other == me:  # draw
        score += 3
    elif other < me: # I win
        score += 6

    score += me.value # points for my type of play
    return score

with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        other, me = globals()[line[0]], globals()[line[2]]  # eugh, pretty gross globals use :'(

        total += score(other, me)

        print(other, me, score, total)
part1_total = total

# Part 2

#X = lose
#Y = draw
#Z = win

with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        other, command = globals()[line[0]], line[2]

        # lol, this is an inefficient way to do things (using filter), but hey, it works!
        # Nice way to reuse the classes, I guess
        if command == 'X':  # lose
            play = list(filter( lambda x : x < other, [A, B, C] ))[0]
            print(f"They played {other}, to lose play {play}")
        if command == 'Y':  # draw
            play = other
            print(f"They played {other}, to draw play {play}")
        if command == 'Z':  # win
            play = list(filter( lambda x : other < x, [A, B, C] ))[0]
            print(f"They played {other}, to win play {play}")

        total += score(other, play)
part2_total = total

print(f"Scores: {part1_total=}")
print(f"Scores: {part2_total=}")