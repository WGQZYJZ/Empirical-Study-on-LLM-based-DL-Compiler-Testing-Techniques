import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 3)
sampler = torch.utils.data.RandomSampler(input_data)
sampler = torch.utils.data.RandomSampler(input_data, replacement=True)
sampler = torch.utils.data.RandomSampler(input_data, replacement=True, num_samples=5)
sampler = torch.utils.data.RandomSampler(input_data, replacement=True, num_samples=5, generator=torch.Generator().manual_seed(1))