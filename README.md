# HW1: Optimal Stopping

Contributors: Dylan Armstrong

## Part 1: Determining the General Optimum (No Look-Back Strategy)

For this problem I had pretty consistent results on my algorithm. The graph below shows the results of over 10,000 samples. As you can see the peak of the line is roughly located where it is stopping at 37 candidates with a 37% success rate. These results were gathered with 10,000 experiments from the uniform_optimal_stopping() function in my code and match closely with what was discussed in class.

![Uniform optimal stop](https://github.com/daffodyl/Optimal-Stopping/blob/main/data/uniform_optimal_stop.png?raw=true)

However one thing I noticed pretty consistently in my results was that the top of my graph ended up pretty flat for a bit before dropping again. So while this next part may not have been required for the homework, I spent too long on this experiment and I have decided to share my results.

I thought the optimal stopping point mathematically may not be the most practical stopping point. So in my code I have included the function optimization_experiment() to test that. You are welcome to run the code on that one, but I don't recommend it unless you have some time. I essentially ran the function from the first graph 1000 * 10,000 times so it took some time to compute. I should figure out how to run in parallel going forward. 

In this experiment I took the highest success result from 10,000 uniform_optimal_stopping() and for each of those results I tried to slide the max back as far as possible on the line, without losing success rate. I measured the change in distance from the max stopping point divided by the change in distance from the correlated max's success rate. The resulting ratio is higher when it gets further from the max without losing success rate.

The results of that experiment are in the graph below. As you can see my graph started to converge with about 8% of my optimizations landing around the stopping point 30. The data is pretty skinny and most of it falls within the range 26-34.

![Optimization experiment](https://github.com/daffodyl/Optimal-Stopping/blob/main/data/optimization_experiment.png?raw=true)

The main point I think this experiment proves is that even though 37% is optimal, stopping a little early (like at 30%) may be more practical if it can save you some time while also not massively losing success rate. Depends on your priorities since time is considered a cost.

## Part 2: Exploring Alternative Distributions

For this problem I got very similar results when using a normal distribution. As you can see below the graph also peaks close to 37% stopping and success chance. These results were gathered with 10,000 experiments from the normal_optimal_stopping() function in my code and match closely with the uniform distribution results.

The graph does look slightly more wobbly near the peak, so it's possible the normal distribution is adding that variance, but it looks very small so it may not be statistically significant. I also attempted a higher standard deviation of 50, but got consistent results with a standard deviation of 10. 

I am a little surprised at how closely the data matched with a uniform distribution, but it is certainly a good thing that the optimal stopping algorithm continues to work for a normal distribution since normal distributions are so common in nature and statistics.

![Normal optimal stop](https://github.com/daffodyl/Optimal-Stopping/blob/main/data/normal_optimal_stop.png?raw=true)
In regards to the beta distribution, from what I understand a distribution of beta(2,7) will have the majority of our data on the left with a longer right tail, or rather it will be right skewed. Basically most of our candidates are not great, while a small number of them are great and located in the right tail.

As you can see this graph also peaks around 37% stopping and success chance. Like the previous distributions, these results were gathered with 10,000 experiments from the beta_optimal_stopping() function in my code and also match closely with the previous results.

![Beta optimal stop](https://github.com/daffodyl/Optimal-Stopping/blob/main/data/beta_optimal_stop.png?raw=true)

One thing I did notice, while my graph tended to peak at 37% when running the function, sometimes the peak was closer to 40, in fact the graph shown specifically peaks at 38, so it makes me wonder if the beta distribution is slightly shifting our best success chance a few points up due to the long right tail. However most of my results continued to center around 37, so I believe the mathematical optimum of this algorithm really is just 37% for all or most distributions.

With how close each result was, I am almost worried I have done something wrong when setting up my data, but the code looks correct to me so I've decided to trust the mathematical truth of 37%, I am not sure in what case you would even know the data distribution type, so assuming you don't know the data distribution type, 37% seems like a safe bet.

## Part 3: Maximizing Benefit in Investment Decisions

The optimal stopping threshold for these scenarios seems to be relatively early. For both distributions the results were gathered with 10,000 experiments from the maximize_investments_reward() function in my code. 
 
In the graph below for the uniform distribution, the average reward peaked just above $80 after 4 evaluations and then steadily declined.

This personally makes sense to me as the cost of evaluations steadily decreases the value we gain from previous information, so the initial evaluations quickly give us a base point without reducing the reward massively like the later evaluations do.

The max reward is S100 so ~$80 isn't too bad considering we stop pretty early, where if we followed the 37% rule the max we could theoretically get is $63, which is why the graph drops so steadily.

![Uniform investment](https://github.com/daffodyl/Optimal-Stopping/blob/main/data/uniform_investment.png?raw=true)

In the graph below for the normal distribution, the data follows a similar pattern to the uniform distribution, but our average reward peaks just below $60 with 3 evaluations.

Considering with a standard deviation of 10, 68% of the data should be between $40 - $60, it makes sense that gathering a small amount of data, then grabbing the next highest would likely be a value within 1 deviation of the median. The first 4 evaluations have a high chance of being near 50 so getting a number just over 50 early seems likely as long as we don't evaluate too much and go below a max of $50. 

![Normal investment](https://github.com/daffodyl/Optimal-Stopping/blob/main/data/normal_investment.png?raw=true)