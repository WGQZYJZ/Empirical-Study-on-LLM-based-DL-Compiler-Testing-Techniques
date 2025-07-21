import torch
from torch import nn
from torch.autograd import Variable
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
weights = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sampler = torch.utils.data.WeightedRandomSampler(weights, 5)
for i in range(5):
    print(next(iter(sampler)))