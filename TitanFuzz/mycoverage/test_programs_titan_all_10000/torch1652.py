import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 2)
sum = torch.sum(input, dim=1)
sum = torch.sum(input, dim=1, keepdim=True)
sum = torch.sum(input, dim=1, keepdim=True, dtype=torch.float)