"""
Iterative solution for 3 Rods(Pegs) :
        (Legal Move means example: A->B if A is larger than move disk from A to B else move B to A)
        disk is Even: then moves are
                            correct move from A -> B
                            correct move from A -> C
                            correct move from B -> c
        disk is Odd: then moves are
                            correct move from A -> C
                            correct move from A -> B
                            correct move from B -> C

        so number of moves is 2^n - 1 where n = number of disk


For more than 3 Rods(Pegs):
    Getting minimum move is so hard (Optimal Solution), couldn't able to solve it
    what I did was, First I put the smallest disk in Rods other than starting, middle and destination,
    then I did the same step as 3 rods for those disks left on starting rods, after I get all those
    left disk on destinationRod, I just move the disk on remaining rods to destinationRod.

    So number of move will be (2^k - 1) + 2m where m = number of  rods - 3
                                                   k = number of disk - m


"""

class TowerOfHanoi:
    def __init__(self, disk, rod):
        self.disk = disk
        self.rod = rod
        self.rods = []
        self.moves = 0

    def numberOfRods(self):
        return self.rod

    def numberOfDisks(self):
        return self.disk

    def numberOfMoves(self):
        return self.moves

    def moveDisk(self, startingRod, destinationRod):
        # take the smallest item which is at first of starting disk
        move = self.rods[startingRod][0]
        del self.rods[startingRod][0]
        self.rods[destinationRod].insert(0, move)
        print("Moving disk {} from {} to {} ".format(move, startingRod, destinationRod))
        self.printRods()
        self.moves += 1

    def legalMoveDisk(self, startingRod, destinationRod):
        #legal move means Pegs with smaller disk will move to the other pegs
        if len(self.rods[startingRod]) == 0:
            self.moveDisk(destinationRod, startingRod)

        elif len(self.rods[destinationRod]) == 0:
            self.moveDisk(startingRod, destinationRod)

        elif self.rods[startingRod][0] < self.rods[destinationRod][0]:
            self.moveDisk(startingRod, destinationRod)

        else:
            self.moveDisk(destinationRod, startingRod)

    def putDiskInStartingRod(self, startingRod):
        for i in range(self.rod):
            if i == startingRod:
                self.rods.append([j for j in range(self.disk)])
            else:
                self.rods.append([])

    def towerOfHanoi_evenDisk(self, startingRod, middleRod, destinationRod):
        while len(self.rods[destinationRod]) != self.disk - (self.rod - 3):
            self.legalMoveDisk(startingRod, middleRod)

            if len(self.rods[destinationRod]) == self.disk - (self.rod - 3):
                break

            self.legalMoveDisk(startingRod, destinationRod)
            if len(self.rods[destinationRod]) == self.disk - (self.rod - 3):
                break

            self.legalMoveDisk(middleRod, destinationRod)

    def towerOfHanoi_oddDisk(self, startingRod, middleRod, destinationRod):
        while len(self.rods[destinationRod]) != self.disk - (self.rod - 3):
            self.legalMoveDisk(startingRod, destinationRod)

            if len(self.rods[destinationRod]) == self.disk - (self.rod - 3):
                break

            self.legalMoveDisk(startingRod, middleRod)
            if len(self.rods[destinationRod]) == self.disk - (self.rod - 3):
                break

            self.legalMoveDisk(middleRod, destinationRod)

    def towerOfHanoi_nthRods(self, startingRod, middleRod, destinationRod):
        self.putDiskInStartingRod(startingRod)
        self.printRods()
        otherMiddleRods = []
        for i in range(self.rod):
            if i != startingRod and i != middleRod and i != destinationRod:
                otherMiddleRods.append(i)
                self.moveDisk(startingRod, i)

        if len(self.rods[startingRod]) % 2 == 0:
            self.towerOfHanoi_evenDisk(startingRod, middleRod, destinationRod)
        else:
            self.towerOfHanoi_oddDisk(startingRod, middleRod, destinationRod)

        for j in reversed(otherMiddleRods):
            self.moveDisk(j, destinationRod)

    def towerOfHanoi(self, startingRod, middleRod, destinationRod):
        if self.rod < 3 or self.disk == 0:
            return None

        # if the the startingRod, MiddleRod, DestinationRod are invalid
        if startingRod > self.rod - 1 or middleRod > self.rod - 1 or destinationRod > self.rod - 1:
            return None

        # tower of Hanoi with rod more than 3, not an optimal solution
        elif self.rod > 3:
            self.towerOfHanoi_nthRods(startingRod, middleRod, destinationRod)
            return

        self.putDiskInStartingRod(startingRod)
        self.printRods()

        if self.disk % 2 == 0:
            self.towerOfHanoi_evenDisk(startingRod, middleRod, destinationRod)
        else:
            self.towerOfHanoi_oddDisk(startingRod, middleRod, destinationRod)

    def printRods(self):
        print(self.rods)

if __name__ == "__main__":
    play1 = TowerOfHanoi(3, 3)
    print("number of Rods: {} and number of Disks: {}".format(play1.numberOfRods(), play1.numberOfDisks()))
    play1.towerOfHanoi(0, 1, 2)
    print("number of Move for {} Rods and {} disks is {}\n\n".format(play1.numberOfRods(), play1.numberOfDisks(),
                                                                     play1.numberOfMoves()))
    play2 = TowerOfHanoi(7, 5)
    print("number of Rods: {} and number of disk: {}".format(play2.numberOfRods(), play2.numberOfDisks()))
    play2.towerOfHanoi(0,2,4)
    print("number of Move for {} Rods and {} disks is {}\n\n".format(play2.numberOfRods(), play2.numberOfDisks(),
                                                                     play2.numberOfMoves()))
    play3 = TowerOfHanoi(7, 3)
    print("number of Rods: {} and number of Disks: {}".format(play3.numberOfRods(), play3.numberOfDisks()))
    play3.towerOfHanoi(0, 1, 2)
    print("number of Move for {} Rods and {} disks is {}\n\n".format(play3.numberOfRods(), play3.numberOfDisks(),
                                                                     play3.numberOfMoves()))
    play6 = TowerOfHanoi(1,3)
    print("number of Rods: {} and number of disk: {}".format(play6.numberOfRods(), play6.numberOfDisks()))
    play6.towerOfHanoi(0, 1, 2)
    print("number of Move for {} Rods and {} disks is {}\n\n".format(play6.numberOfRods(), play6.numberOfDisks(),
                                                                     play6.numberOfMoves()))
    play4 = TowerOfHanoi(12, 2)
    play4.towerOfHanoi(0,1,2)
    # it will return nothing

    play5 = TowerOfHanoi(0, 3)
    play5.towerOfHanoi(0,1,2)
    # it will return nothing

""" ---------------------------- OUTPUT -------------------------------------------
number of Rods: 3 and number of Disks: 3
[[0, 1, 2], [], []]
Moving disk 0 from 0 to 2 
[[1, 2], [], [0]]
Moving disk 1 from 0 to 1 
[[2], [1], [0]]
Moving disk 0 from 2 to 1 
[[2], [0, 1], []]
Moving disk 2 from 0 to 2 
[[], [0, 1], [2]]
Moving disk 0 from 1 to 0 
[[0], [1], [2]]
Moving disk 1 from 1 to 2 
[[0], [], [1, 2]]
Moving disk 0 from 0 to 2 
[[], [], [0, 1, 2]]
number of Move for 3 Rods and 3 disks is 7


number of Rods: 3 and number of Disks: 7
[[0, 1, 2, 3, 4, 5, 6], [], []]
Moving disk 0 from 0 to 2 
[[1, 2, 3, 4, 5, 6], [], [0]]
Moving disk 1 from 0 to 1 
[[2, 3, 4, 5, 6], [1], [0]]
Moving disk 0 from 2 to 1 
[[2, 3, 4, 5, 6], [0, 1], []]
Moving disk 2 from 0 to 2 
[[3, 4, 5, 6], [0, 1], [2]]
Moving disk 0 from 1 to 0 
[[0, 3, 4, 5, 6], [1], [2]]
Moving disk 1 from 1 to 2 
[[0, 3, 4, 5, 6], [], [1, 2]]
Moving disk 0 from 0 to 2 
[[3, 4, 5, 6], [], [0, 1, 2]]
Moving disk 3 from 0 to 1 
[[4, 5, 6], [3], [0, 1, 2]]
Moving disk 0 from 2 to 1 
[[4, 5, 6], [0, 3], [1, 2]]
Moving disk 1 from 2 to 0 
[[1, 4, 5, 6], [0, 3], [2]]
Moving disk 0 from 1 to 0 
[[0, 1, 4, 5, 6], [3], [2]]
Moving disk 2 from 2 to 1 
[[0, 1, 4, 5, 6], [2, 3], []]
Moving disk 0 from 0 to 2 
[[1, 4, 5, 6], [2, 3], [0]]
Moving disk 1 from 0 to 1 
[[4, 5, 6], [1, 2, 3], [0]]
Moving disk 0 from 2 to 1 
[[4, 5, 6], [0, 1, 2, 3], []]
Moving disk 4 from 0 to 2 
[[5, 6], [0, 1, 2, 3], [4]]
Moving disk 0 from 1 to 0 
[[0, 5, 6], [1, 2, 3], [4]]
Moving disk 1 from 1 to 2 
[[0, 5, 6], [2, 3], [1, 4]]
Moving disk 0 from 0 to 2 
[[5, 6], [2, 3], [0, 1, 4]]
Moving disk 2 from 1 to 0 
[[2, 5, 6], [3], [0, 1, 4]]
Moving disk 0 from 2 to 1 
[[2, 5, 6], [0, 3], [1, 4]]
Moving disk 1 from 2 to 0 
[[1, 2, 5, 6], [0, 3], [4]]
Moving disk 0 from 1 to 0 
[[0, 1, 2, 5, 6], [3], [4]]
Moving disk 3 from 1 to 2 
[[0, 1, 2, 5, 6], [], [3, 4]]
Moving disk 0 from 0 to 2 
[[1, 2, 5, 6], [], [0, 3, 4]]
Moving disk 1 from 0 to 1 
[[2, 5, 6], [1], [0, 3, 4]]
Moving disk 0 from 2 to 1 
[[2, 5, 6], [0, 1], [3, 4]]
Moving disk 2 from 0 to 2 
[[5, 6], [0, 1], [2, 3, 4]]
Moving disk 0 from 1 to 0 
[[0, 5, 6], [1], [2, 3, 4]]
Moving disk 1 from 1 to 2 
[[0, 5, 6], [], [1, 2, 3, 4]]
Moving disk 0 from 0 to 2 
[[5, 6], [], [0, 1, 2, 3, 4]]
Moving disk 5 from 0 to 1 
[[6], [5], [0, 1, 2, 3, 4]]
Moving disk 0 from 2 to 1 
[[6], [0, 5], [1, 2, 3, 4]]
Moving disk 1 from 2 to 0 
[[1, 6], [0, 5], [2, 3, 4]]
Moving disk 0 from 1 to 0 
[[0, 1, 6], [5], [2, 3, 4]]
Moving disk 2 from 2 to 1 
[[0, 1, 6], [2, 5], [3, 4]]
Moving disk 0 from 0 to 2 
[[1, 6], [2, 5], [0, 3, 4]]
Moving disk 1 from 0 to 1 
[[6], [1, 2, 5], [0, 3, 4]]
Moving disk 0 from 2 to 1 
[[6], [0, 1, 2, 5], [3, 4]]
Moving disk 3 from 2 to 0 
[[3, 6], [0, 1, 2, 5], [4]]
Moving disk 0 from 1 to 0 
[[0, 3, 6], [1, 2, 5], [4]]
Moving disk 1 from 1 to 2 
[[0, 3, 6], [2, 5], [1, 4]]
Moving disk 0 from 0 to 2 
[[3, 6], [2, 5], [0, 1, 4]]
Moving disk 2 from 1 to 0 
[[2, 3, 6], [5], [0, 1, 4]]
Moving disk 0 from 2 to 1 
[[2, 3, 6], [0, 5], [1, 4]]
Moving disk 1 from 2 to 0 
[[1, 2, 3, 6], [0, 5], [4]]
Moving disk 0 from 1 to 0 
[[0, 1, 2, 3, 6], [5], [4]]
Moving disk 4 from 2 to 1 
[[0, 1, 2, 3, 6], [4, 5], []]
Moving disk 0 from 0 to 2 
[[1, 2, 3, 6], [4, 5], [0]]
Moving disk 1 from 0 to 1 
[[2, 3, 6], [1, 4, 5], [0]]
Moving disk 0 from 2 to 1 
[[2, 3, 6], [0, 1, 4, 5], []]
Moving disk 2 from 0 to 2 
[[3, 6], [0, 1, 4, 5], [2]]
Moving disk 0 from 1 to 0 
[[0, 3, 6], [1, 4, 5], [2]]
Moving disk 1 from 1 to 2 
[[0, 3, 6], [4, 5], [1, 2]]
Moving disk 0 from 0 to 2 
[[3, 6], [4, 5], [0, 1, 2]]
Moving disk 3 from 0 to 1 
[[6], [3, 4, 5], [0, 1, 2]]
Moving disk 0 from 2 to 1 
[[6], [0, 3, 4, 5], [1, 2]]
Moving disk 1 from 2 to 0 
[[1, 6], [0, 3, 4, 5], [2]]
Moving disk 0 from 1 to 0 
[[0, 1, 6], [3, 4, 5], [2]]
Moving disk 2 from 2 to 1 
[[0, 1, 6], [2, 3, 4, 5], []]
Moving disk 0 from 0 to 2 
[[1, 6], [2, 3, 4, 5], [0]]
Moving disk 1 from 0 to 1 
[[6], [1, 2, 3, 4, 5], [0]]
Moving disk 0 from 2 to 1 
[[6], [0, 1, 2, 3, 4, 5], []]
Moving disk 6 from 0 to 2 
[[], [0, 1, 2, 3, 4, 5], [6]]
Moving disk 0 from 1 to 0 
[[0], [1, 2, 3, 4, 5], [6]]
Moving disk 1 from 1 to 2 
[[0], [2, 3, 4, 5], [1, 6]]
Moving disk 0 from 0 to 2 
[[], [2, 3, 4, 5], [0, 1, 6]]
Moving disk 2 from 1 to 0 
[[2], [3, 4, 5], [0, 1, 6]]
Moving disk 0 from 2 to 1 
[[2], [0, 3, 4, 5], [1, 6]]
Moving disk 1 from 2 to 0 
[[1, 2], [0, 3, 4, 5], [6]]
Moving disk 0 from 1 to 0 
[[0, 1, 2], [3, 4, 5], [6]]
Moving disk 3 from 1 to 2 
[[0, 1, 2], [4, 5], [3, 6]]
Moving disk 0 from 0 to 2 
[[1, 2], [4, 5], [0, 3, 6]]
Moving disk 1 from 0 to 1 
[[2], [1, 4, 5], [0, 3, 6]]
Moving disk 0 from 2 to 1 
[[2], [0, 1, 4, 5], [3, 6]]
Moving disk 2 from 0 to 2 
[[], [0, 1, 4, 5], [2, 3, 6]]
Moving disk 0 from 1 to 0 
[[0], [1, 4, 5], [2, 3, 6]]
Moving disk 1 from 1 to 2 
[[0], [4, 5], [1, 2, 3, 6]]
Moving disk 0 from 0 to 2 
[[], [4, 5], [0, 1, 2, 3, 6]]
Moving disk 4 from 1 to 0 
[[4], [5], [0, 1, 2, 3, 6]]
Moving disk 0 from 2 to 1 
[[4], [0, 5], [1, 2, 3, 6]]
Moving disk 1 from 2 to 0 
[[1, 4], [0, 5], [2, 3, 6]]
Moving disk 0 from 1 to 0 
[[0, 1, 4], [5], [2, 3, 6]]
Moving disk 2 from 2 to 1 
[[0, 1, 4], [2, 5], [3, 6]]
Moving disk 0 from 0 to 2 
[[1, 4], [2, 5], [0, 3, 6]]
Moving disk 1 from 0 to 1 
[[4], [1, 2, 5], [0, 3, 6]]
Moving disk 0 from 2 to 1 
[[4], [0, 1, 2, 5], [3, 6]]
Moving disk 3 from 2 to 0 
[[3, 4], [0, 1, 2, 5], [6]]
Moving disk 0 from 1 to 0 
[[0, 3, 4], [1, 2, 5], [6]]
Moving disk 1 from 1 to 2 
[[0, 3, 4], [2, 5], [1, 6]]
Moving disk 0 from 0 to 2 
[[3, 4], [2, 5], [0, 1, 6]]
Moving disk 2 from 1 to 0 
[[2, 3, 4], [5], [0, 1, 6]]
Moving disk 0 from 2 to 1 
[[2, 3, 4], [0, 5], [1, 6]]
Moving disk 1 from 2 to 0 
[[1, 2, 3, 4], [0, 5], [6]]
Moving disk 0 from 1 to 0 
[[0, 1, 2, 3, 4], [5], [6]]
Moving disk 5 from 1 to 2 
[[0, 1, 2, 3, 4], [], [5, 6]]
Moving disk 0 from 0 to 2 
[[1, 2, 3, 4], [], [0, 5, 6]]
Moving disk 1 from 0 to 1 
[[2, 3, 4], [1], [0, 5, 6]]
Moving disk 0 from 2 to 1 
[[2, 3, 4], [0, 1], [5, 6]]
Moving disk 2 from 0 to 2 
[[3, 4], [0, 1], [2, 5, 6]]
Moving disk 0 from 1 to 0 
[[0, 3, 4], [1], [2, 5, 6]]
Moving disk 1 from 1 to 2 
[[0, 3, 4], [], [1, 2, 5, 6]]
Moving disk 0 from 0 to 2 
[[3, 4], [], [0, 1, 2, 5, 6]]
Moving disk 3 from 0 to 1 
[[4], [3], [0, 1, 2, 5, 6]]
Moving disk 0 from 2 to 1 
[[4], [0, 3], [1, 2, 5, 6]]
Moving disk 1 from 2 to 0 
[[1, 4], [0, 3], [2, 5, 6]]
Moving disk 0 from 1 to 0 
[[0, 1, 4], [3], [2, 5, 6]]
Moving disk 2 from 2 to 1 
[[0, 1, 4], [2, 3], [5, 6]]
Moving disk 0 from 0 to 2 
[[1, 4], [2, 3], [0, 5, 6]]
Moving disk 1 from 0 to 1 
[[4], [1, 2, 3], [0, 5, 6]]
Moving disk 0 from 2 to 1 
[[4], [0, 1, 2, 3], [5, 6]]
Moving disk 4 from 0 to 2 
[[], [0, 1, 2, 3], [4, 5, 6]]
Moving disk 0 from 1 to 0 
[[0], [1, 2, 3], [4, 5, 6]]
Moving disk 1 from 1 to 2 
[[0], [2, 3], [1, 4, 5, 6]]
Moving disk 0 from 0 to 2 
[[], [2, 3], [0, 1, 4, 5, 6]]
Moving disk 2 from 1 to 0 
[[2], [3], [0, 1, 4, 5, 6]]
Moving disk 0 from 2 to 1 
[[2], [0, 3], [1, 4, 5, 6]]
Moving disk 1 from 2 to 0 
[[1, 2], [0, 3], [4, 5, 6]]
Moving disk 0 from 1 to 0 
[[0, 1, 2], [3], [4, 5, 6]]
Moving disk 3 from 1 to 2 
[[0, 1, 2], [], [3, 4, 5, 6]]
Moving disk 0 from 0 to 2 
[[1, 2], [], [0, 3, 4, 5, 6]]
Moving disk 1 from 0 to 1 
[[2], [1], [0, 3, 4, 5, 6]]
Moving disk 0 from 2 to 1 
[[2], [0, 1], [3, 4, 5, 6]]
Moving disk 2 from 0 to 2 
[[], [0, 1], [2, 3, 4, 5, 6]]
Moving disk 0 from 1 to 0 
[[0], [1], [2, 3, 4, 5, 6]]
Moving disk 1 from 1 to 2 
[[0], [], [1, 2, 3, 4, 5, 6]]
Moving disk 0 from 0 to 2 
[[], [], [0, 1, 2, 3, 4, 5, 6]]
number of Move for 3 Rods and 7 disks is 127


number of Rods: 5 and number of disk: 7
[[0, 1, 2, 3, 4, 5, 6], [], [], [], []]
Moving disk 0 from 0 to 1 
[[1, 2, 3, 4, 5, 6], [0], [], [], []]
Moving disk 1 from 0 to 3 
[[2, 3, 4, 5, 6], [0], [], [1], []]
Moving disk 2 from 0 to 4 
[[3, 4, 5, 6], [0], [], [1], [2]]
Moving disk 3 from 0 to 2 
[[4, 5, 6], [0], [3], [1], [2]]
Moving disk 2 from 4 to 2 
[[4, 5, 6], [0], [2, 3], [1], []]
Moving disk 4 from 0 to 4 
[[5, 6], [0], [2, 3], [1], [4]]
Moving disk 2 from 2 to 0 
[[2, 5, 6], [0], [3], [1], [4]]
Moving disk 3 from 2 to 4 
[[2, 5, 6], [0], [], [1], [3, 4]]
Moving disk 2 from 0 to 4 
[[5, 6], [0], [], [1], [2, 3, 4]]
Moving disk 5 from 0 to 2 
[[6], [0], [5], [1], [2, 3, 4]]
Moving disk 2 from 4 to 2 
[[6], [0], [2, 5], [1], [3, 4]]
Moving disk 3 from 4 to 0 
[[3, 6], [0], [2, 5], [1], [4]]
Moving disk 2 from 2 to 0 
[[2, 3, 6], [0], [5], [1], [4]]
Moving disk 4 from 4 to 2 
[[2, 3, 6], [0], [4, 5], [1], []]
Moving disk 2 from 0 to 4 
[[3, 6], [0], [4, 5], [1], [2]]
Moving disk 3 from 0 to 2 
[[6], [0], [3, 4, 5], [1], [2]]
Moving disk 2 from 4 to 2 
[[6], [0], [2, 3, 4, 5], [1], []]
Moving disk 6 from 0 to 4 
[[], [0], [2, 3, 4, 5], [1], [6]]
Moving disk 2 from 2 to 0 
[[2], [0], [3, 4, 5], [1], [6]]
Moving disk 3 from 2 to 4 
[[2], [0], [4, 5], [1], [3, 6]]
Moving disk 2 from 0 to 4 
[[], [0], [4, 5], [1], [2, 3, 6]]
Moving disk 4 from 2 to 0 
[[4], [0], [5], [1], [2, 3, 6]]
Moving disk 2 from 4 to 2 
[[4], [0], [2, 5], [1], [3, 6]]
Moving disk 3 from 4 to 0 
[[3, 4], [0], [2, 5], [1], [6]]
Moving disk 2 from 2 to 0 
[[2, 3, 4], [0], [5], [1], [6]]
Moving disk 5 from 2 to 4 
[[2, 3, 4], [0], [], [1], [5, 6]]
Moving disk 2 from 0 to 4 
[[3, 4], [0], [], [1], [2, 5, 6]]
Moving disk 3 from 0 to 2 
[[4], [0], [3], [1], [2, 5, 6]]
Moving disk 2 from 4 to 2 
[[4], [0], [2, 3], [1], [5, 6]]
Moving disk 4 from 0 to 4 
[[], [0], [2, 3], [1], [4, 5, 6]]
Moving disk 2 from 2 to 0 
[[2], [0], [3], [1], [4, 5, 6]]
Moving disk 3 from 2 to 4 
[[2], [0], [], [1], [3, 4, 5, 6]]
Moving disk 2 from 0 to 4 
[[], [0], [], [1], [2, 3, 4, 5, 6]]
Moving disk 1 from 3 to 4 
[[], [0], [], [], [1, 2, 3, 4, 5, 6]]
Moving disk 0 from 1 to 4 
[[], [], [], [], [0, 1, 2, 3, 4, 5, 6]]
number of Move for 5 Rods and 7 disks is 35


number of Rods: 3 and number of disk: 1
[[0], [], []]
Moving disk 0 from 0 to 2 
[[], [], [0]]
number of Move for 3 Rods and 1 disks is 1



Process finished with exit code 0

"""











