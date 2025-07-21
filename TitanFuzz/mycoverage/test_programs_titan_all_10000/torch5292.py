import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
result = torch.unbind(input, dim=0)