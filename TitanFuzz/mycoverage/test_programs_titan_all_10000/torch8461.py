import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
result = torch.argmin(input, dim=1)