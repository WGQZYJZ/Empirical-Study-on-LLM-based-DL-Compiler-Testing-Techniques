import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(4, 4)
mean = torch.mean(a, dim=1, keepdim=True)