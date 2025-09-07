import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 100)
sampler = torch.utils.data.Sampler(data)