import torch
from torch import nn
from torch.autograd import Variable
data_source = torch.arange(10)
sampler = torch.utils.data.RandomSampler(data_source)