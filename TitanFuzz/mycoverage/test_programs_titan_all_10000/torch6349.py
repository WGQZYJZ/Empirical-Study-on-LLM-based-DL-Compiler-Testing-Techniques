import torch
from torch import nn
from torch.autograd import Variable
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
num_samples = 5
replacement = True
generator = None
sampler = torch.utils.data.WeightedRandomSampler(weights, num_samples, replacement, generator)