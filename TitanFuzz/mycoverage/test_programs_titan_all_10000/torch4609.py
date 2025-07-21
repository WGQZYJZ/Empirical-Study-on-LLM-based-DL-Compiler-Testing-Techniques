import torch
from torch import nn
from torch.autograd import Variable
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_samples = 10
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement=True, generator=None)