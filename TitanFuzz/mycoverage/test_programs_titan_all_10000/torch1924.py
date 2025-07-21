import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 10)
sampler = torch.utils.data.Subset(data, [2, 4, 6, 8])