import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 2)
result = torch.argmin(input, dim=1)