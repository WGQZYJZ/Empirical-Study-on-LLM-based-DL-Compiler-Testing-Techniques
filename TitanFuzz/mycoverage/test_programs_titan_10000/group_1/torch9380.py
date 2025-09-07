import torch
from torch import nn
from torch.autograd import Variable

data_source = [i for i in range(10)]
sampler = torch.utils.data.RandomSampler(data_source, replacement=False, num_samples=10)