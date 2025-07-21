import torch
from torch import nn
from torch.autograd import Variable
weights = [0.1, 0.2, 0.3, 0.4]
samples = [1, 2, 3, 4]
sampler = torch.utils.data.WeightedRandomSampler(weights, 4)
for i in sampler:
    print(samples[i])