import matplotlib.pyplot as plt
import numpy as np

# General purpose optimal stopping algorithm
def optimal_stopping(len_candidates, num_of_experiments, data):
    optimal_solution_found_count = {}
    for i in range(1, len_candidates):
        optimal_solution_found_count[str(i)] = 0

    for experiment in range(num_of_experiments):
        candidates = data(len_candidates)
        optimal_candidate = max(candidates)

        for i in range(1, len_candidates):
            for candidate in candidates[i:-1]:
                if candidate > max(candidates[0:i]):
                    if candidate == optimal_candidate:
                        optimal_solution_found_count[str(i)] += 1

                    break
    
    # Convert results to a percentage 
    for i in range(1, len_candidates):
        optimal_solution_found_count[str(i)] = round((optimal_solution_found_count[str(i)]/num_of_experiments) * 100, 3)

    return optimal_solution_found_count

def plot_sample(sample):
    x, y = zip(*sample.items())

    plt.plot(x,y)
    plt.xticks(fontsize = 8)
    plt.axvline(np.argmax(y), linestyle='--')
    plt.show()

###############################
# Problem 1
###############################

def uniform_optimal_stopping(len_candidates, num_of_experiments):
    print("Applying optimal stop to uniform distribution data....")
    
    return optimal_stopping(len_candidates, num_of_experiments, uniform_dataset)

def uniform_dataset(len_candidates):
    return np.random.uniform(1, 100, len_candidates)

# Function that attempts to slide back the peak of the graph without losing much success chance
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

# Attempts to optimize the optimal stopping point to be more practical
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


# Results of problem 1
s1 = uniform_optimal_stopping(100, 10000)
plot_sample(s1)


## Personal experiment Results
# s2 = optimization_experiment(10000)
# plot_sample(s2)



###############################
# Problem 2
###############################

def normal_optimal_stopping(len_candidates, num_of_experiments):
    print("Applying optimal stop to normal distribution data....")
    
    return optimal_stopping(len_candidates, num_of_experiments, normal_dataset)

def normal_dataset(len_candidates):
    return np.random.normal(50, 10, len_candidates)

def beta_optimal_stopping(len_candidates, num_of_experiments):
    print("Applying optimal stop to beta distribution data....")
    
    return optimal_stopping(len_candidates, num_of_experiments, beta_dataset)

def beta_dataset(len_candidates):
    return np.random.beta(2, 7, len_candidates)


# Results of problem 2
s3 = normal_optimal_stopping(100, 10000)
s4 = beta_optimal_stopping(100, 10000)

plot_sample(s3)
plot_sample(s4)

###############################
# Problem 3
###############################

def maximize_investments_reward(len_investments, num_of_experiments, data, cap=0):
    reward = {}
    for i in range(1, len_investments):
        reward[str(i)] = 0

    for experiment in range(num_of_experiments):
        investments = data(len_investments)

        for i in range(1, len_investments):
            if cap > 0 and investments[i] > cap:
                investments[i] = cap
            for investment in investments[i:-1]:
                if investment > max(investments[0:i]):
                    reward[str(i)] += (investment - i)

                    break
    
    # Convert results to an average reward amount 
    for i in range(1, len_investments):
        reward[str(i)] = round((reward[str(i)]/num_of_experiments), 3)

    return reward

def uniform_maximize_investments(len_candidates, num_of_experiments):
    print("Applying optimal stop to normal distribution data with evaluation cost....")
    
    return maximize_investments_reward(len_candidates, num_of_experiments, uniform_dataset)

def normal_maximize_investments(len_candidates, num_of_experiments):
    print("Applying optimal stop to normal distribution data with evaluation cost....")
    
    return maximize_investments_reward(len_candidates, num_of_experiments, normal_dataset, 99)

# Results of problem 3
s5 = uniform_maximize_investments(100, 10000)
s6 = normal_maximize_investments(100, 10000)

plot_sample(s5)
plot_sample(s6)

