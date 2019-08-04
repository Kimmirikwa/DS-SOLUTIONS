# The solution for PLS0001
For the problem description, kindly refer [here](https://github.com/jumo/de-public/tree/master/play/PLS/PLS0001)

The input data is in ```input.csv```. The requirement here is to aggregate the data on the ```Network```, ```Product``` and ```Month```. 
I decided to use *Python* in this exercise. This is because Python is easy to understand and a very intuitive language. There are very many great python libraries like *Pandas*(use here!), *Numpy*, *Scipy*, *Matplotlib* and others which are very easy to use when tacking data analysis. It also quite easy to have a python script to achieve something. Python is also highly portable.

I only used *Pandas* here. Pandas is very powerful and I was able to achieve a lot by using a few lines of code. It is also very efficient as it has numerious vectorized implementations. I have made many assumptions in this exercise and I have only done close to minimum requirement to do the required aggregation.

The input data in this exercise was very clean. There were no missing data points too. I therefore made so many assumptions and came up with a simple solution to handle this data case. The following are some of the assumptions I had when coming up with my solution.

- I assumed that I was required to do ```sum``` aggregation.
- I assumed that I was to group by ```Network```, then ```Product``` and finally ```Month``` as they were given in that order.
- The input data does not have any missing values. This is a very naive assumption as we it is well known that sometimes we usually have some data missing. I can improve this by handling missing values.
- I assumed that the columns used in aggregation had all their data points in the same case. For example, my solution treats ```Network 2``` and ```network 2``` as 2 different networks. This is definetely an issue.
- As the input file was quite small, I was able to read all the data in memory. This might not always be true as sometimes data can be quite large making it impractical to try fitting all of it memory. It is probably advisable to try reading the data in multiple chunks that can fit in memory.
- I have also done all the processing of data in memory. If the data is too large, this can lead to memory issues. An implementation of ```Map Reduce``` for example ```Dataflow``` can definetely help here.

The result of my aggregation is in ```result/Output.csv```. Unfortunately for this data, all the ```Network```, ```Product``` and ```Month``` combinations were unique and we never had 'true aggregation'.
