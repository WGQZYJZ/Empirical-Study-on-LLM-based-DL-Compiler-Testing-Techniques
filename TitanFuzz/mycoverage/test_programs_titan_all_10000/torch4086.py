import torch
from torch import nn
from torch.autograd import Variable
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
sampler = torch.utils.data.WeightedRandomSampler(weights, 5)
for idx in sampler:
    print('Index: ', idx)