import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
torch.quantile(input, 0.5, dim=1, keepdim=True)
input = torch.randn(3, 4)
torch.quantile(input, 0.5, dim=1, keepdim=True)