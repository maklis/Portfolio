import random
from pprint import pprint



def BoardSize():
    n = input("How many queens: ")
    return int(n)


def print_board(board, n):
    print('Board:')
    for i in range(len(board)):
        print(str(board[i]) + ' ', end='')
        if (i + 1) % n == 0:
            print()
    print('H value: ', determine_h_cost(board, n))
    print('---------------------\n\n')


def generate_board(n):
    genboard = []
    for i in range(n):
        j = random.randint(0, n - 1)
        row = [0] * n
        row[j] = 1
        genboard.extend(row)
    return genboard


def determine_h_cost(board, n, vb=False):
    hits, haps = find_hits(board, n)
    if vb:
        pprint(haps)
    return int(hits / 2)

def find_hits(board, n):
    hits = 0
    haps = []
    max_index = len(board)
    for i in range(max_index):
        if board[i] == 1:
            for x in range(1, n):
                if (i - n * x >= 0):
                    north = i - n * x
                    if (board[north] == 1):
                        hits += 1
                        haps.append('north: ' + str(i) + ' and ' + str(north))
                    if (int((north - x) / n) == int(north / n)) and (north - x) >= 0:
                        northwest = north - x
                        if (board[northwest] == 1):
                            hits += 1
                            haps.append('northwest: ' + str(i) + ' and ' + str(northwest))
                    if (int((north + x) / n) == int(north / n)):
                        northeast = north + x
                        if (board[northeast] == 1):
                            hits += 1
                            haps.append('northeast: ' + str(i) + ' and ' + str(northeast))
                if (i + n * x < max_index):
                    south = i + n * x
                    if (board[south] == 1):
                        hits += 1
                        haps.append('south: ' + str(i) + ' and ' + str(south))
                    if (int((south - x) / n) == int(south / n)):
                        southwest = south - x
                        if (board[southwest] == 1):
                            hits += 1
                            haps.append('southwest: ' + str(i) + ' and ' + str(southwest))
                    if (int((south + x) / n) == int(south / n)) and ((south + x) < max_index):
                        southeast = south + x
                        if (board[southeast] == 1):
                            hits += 1
                            haps.append('southeast: ' + str(i) + ' and ' + str(southeast))
                if (int((i - x) / n) == int(i / n)) and (i - x >= 0):
                    west = i - x
                    if (board[west] == 1):
                        hits += 1
                        haps.append('west: ' + str(i) + ' and ' + str(west))
                if (int((i + x) / n) == int(i / n)) and (i + x < max_index):
                    east = i + x
                    if (board[east] == 1):
                        hits += 1
                        haps.append('east: ' + str(i) + ' and ' + str(east))
    return [hits, haps]





def find_child(board, n, sideways_move=False):
    child = []
    current_h_cost = determine_h_cost(board, n)
    scc = []

    for row in range(n):
        for col in range(n):
            TBoard = []
            TBoard.extend(board[:row * n])
            new_row = [0] * n
            new_row[col] = 1
            TBoard.extend(new_row)
            TBoard.extend(board[(row + 1) * n:])
            temp_h_cost = determine_h_cost(TBoard, n)
            if (sideways_move):
                if (TBoard != board):
                    if (temp_h_cost < current_h_cost):
                        child = TBoard.copy()
                        current_h_cost = temp_h_cost
                    elif (temp_h_cost == current_h_cost):
                        scc.append(TBoard)
                        x = random.randint(0, len(scc) - 1)
                        child = scc[x]
            else:
                if (TBoard != board) and (temp_h_cost < current_h_cost):
                    child = TBoard.copy()
                    current_h_cost = temp_h_cost
    return child


def steepest_hill_climbing(board, n, max_iterations=1000, vb=False):
    steps = 0
    success = False
    current_board = board.copy()

    if (vb):
        print_board(current_board, n)

    for i in range(max_iterations):
        next_node = find_child(current_board, n).copy()

        if (vb and len(next_node) != 0):
            print_board(next_node, n)

        steps += 1
        if (len(next_node) != 0) and (determine_h_cost(next_node, n) == 0):
            success = True
            break
        if (len(next_node) == 0):
            break
        current_board = next_node.copy()
    return steps, success


n = BoardSize()
iterations = 1000

print('Steepest Hill Climbing:')
success_rate_steepest_hill_climbing = False
step_count_rate_steepest_hill_climbing_success = 0
step_count_rate_steepest_hill_climbing_failure = 0
for i in range(iterations):
    print('Number of iteration ' + str(i + 1) + ':')
    step_count, success = steepest_hill_climbing(generate_board(n), n, vb=True)
    if (success):
        print('Success.')
        print('The number of steps are :' + str(step_count))
        step_count_rate_steepest_hill_climbing_success += step_count
    step_count_rate_steepest_hill_climbing_failure += step_count
    success_rate_steepest_hill_climbing += success
print('Success rate: ' + str(success_rate_steepest_hill_climbing / iterations))
print('Failure rate: ' + str(1 - (success_rate_steepest_hill_climbing / iterations)))
print('Average steps when success: ' + str(
    step_count_rate_steepest_hill_climbing_success / success_rate_steepest_hill_climbing))
print('Average steps when failure: ' + str(
    step_count_rate_steepest_hill_climbing_failure / (iterations - success_rate_steepest_hill_climbing)))


#For Genetic
def random_chromosome(size):  
    return [ random.randint(1, nq) for _ in range(nq) ]

def FitnessScore(chromosome):
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
    
    return int(maxFitnessScore - (horizontal_collisions + diagonal_collisions)) 

def probability(chromosome, FitnessScore):
    return FitnessScore(chromosome) / maxFitnessScore

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
        
def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):  
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def genetic_queen(population, FitnessScore):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, FitnessScore) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities) 
        child = reproduce(x, y) 
        if random.random() < mutation_probability:
            child = mutate(child)
        print_chromosome(child)
        new_population.append(child)
        if FitnessScore(child) == maxFitnessScore: break
    return new_population

def print_chromosome(chrom):
    print("chromosome = {},  FitnessScore = {}"
        .format(str(chrom), FitnessScore(chrom)))

if __name__ == "__main__":
    nq = int(input("Enter Number of Queens: ")) 
    maxFitnessScore = (nq*(nq-1))/2 
    population = [random_chromosome(nq) for _ in range(100)]
    
    generation = 1

    while not maxFitnessScore in [FitnessScore(chrom) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, FitnessScore)
        print("")
        print("Maximum FitnessScore = {}".format(max([FitnessScore(n) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}!".format(generation-1))
    for chrom in population:
        if FitnessScore(chrom) == maxFitnessScore:
            print("");
            print("One of the solutions: ")
            chrom_out = chrom
            print_chromosome(chrom)
            
    board = []


    def print_board(board):
        for row in board:
            print (" ".join(row))
            
    print()
    print_board(board)

