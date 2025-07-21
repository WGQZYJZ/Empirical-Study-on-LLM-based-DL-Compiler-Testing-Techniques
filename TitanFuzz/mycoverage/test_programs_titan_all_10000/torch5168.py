import torch
from torch import nn
from torch.autograd import Variable
data_source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampler = torch.utils.data.RandomSampler(data_source, replacement=False, num_samples=None, generator=None)