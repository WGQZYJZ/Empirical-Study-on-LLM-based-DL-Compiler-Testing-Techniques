import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
q = torch.quantile(input, 0.4)
q = torch.quantile(input, 0.4, dim=0)
q = torch.quantile(input, 0.4, dim=1)
q = torch.quantile(input, 0.4, dim=1, keepdim=True)