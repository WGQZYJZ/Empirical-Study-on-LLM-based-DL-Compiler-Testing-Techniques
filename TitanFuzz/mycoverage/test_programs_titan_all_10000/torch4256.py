import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(0, 100, (10,))
weights = torch.randint(0, 100, (10,))
weights = (weights / weights.sum())
sampler = torch.utils.data.WeightedRandomSampler(weights, 10, replacement=True)
for i in range(5):
    idx = sampler.__iter__().__next__()
    print(idx)
    print(input_data[idx])