import torch
from torch import nn
from torch.autograd import Variable
weights = np.array([0.1, 0.2, 0.3, 0.4])
sampler = torch.utils.data.WeightedRandomSampler(weights, 4)
for idx in sampler:
    print(idx)