import torch
from torch import nn
from torch.autograd import Variable
data_source = list(range(10))
sampler = torch.utils.data.Sampler(data_source)