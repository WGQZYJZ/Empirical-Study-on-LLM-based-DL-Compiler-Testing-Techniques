import torch
from torch import nn
from torch.autograd import Variable
data_source = torch.randn(10)
sampler = torch.utils.data.RandomSampler(data_source)
data_source = torch.randn(10)
sampler = torch.utils.data.SequentialSampler(data_source)
data_source = torch.randn(10)