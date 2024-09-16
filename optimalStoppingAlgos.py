import random
import matplotlib.pyplot as plt

###############################
# Problem 1
###############################

def uniform_optimal_stopping(len_candidates, num_of_experiments):
    print("Sampling uniform distribution data....")
    optimal_solution_found_count = {}
    for i in range(1, len_candidates):
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(num_of_experiments):
        candidates = random.sample(range(0,1000), len_candidates)
        optimal_candidate = max(candidates)

        for i in range(1, len_candidates):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i)] += 1

                    break

    for i in range(1, len_candidates):
        optimal_solution_found_count[str(i)] = round((optimal_solution_found_count[str(i)]/num_of_experiments) * 100, 3)

    return optimal_solution_found_count

def slide_back(y):
    maxIndex = 0
    for i in range(len(y)):
        if y[i] > y[maxIndex]:
            maxIndex = i
    bestRatio = 0
    bestIndex = maxIndex
    for i in range(maxIndex, 0, -1):
        ratio = 0
        if (y[maxIndex] - y[i]) != 0:
            ratio = (maxIndex - i) / (y[maxIndex] - y[i])
        if ratio >= bestRatio:
            bestRatio = ratio
            bestIndex = i
    return bestIndex + 1

def optimization_experiment(num_of_experiments):
    print("Optimizing data to stop sooner without losing success chance....")
    count = {}

    for i in range(1, 100):
            count[str(i)] = 0

    for experiment in range(num_of_experiments):
            sample = uniform_optimal_stopping(100,1000)
            x, y = zip(*sample.items())
            opSample = slide_back(y)

            count[str(opSample)] += 1
    
    return count

def plot_sample(sample):
    x, y = zip(*sample.items())

    plt.plot(x,y)
    plt.xticks(fontsize = 8)
    plt.show()


s1 = uniform_optimal_stopping(100,10000)
# s2 = optimization_experiment(10000)

plot_sample(s1)

###############################
# Problem 2
###############################

###############################
# Problem 3
###############################

