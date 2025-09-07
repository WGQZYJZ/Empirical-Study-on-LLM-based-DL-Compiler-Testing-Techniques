import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, dtype=torch.float)
other = torch.randn(2, 3, dtype=torch.float)
result = torch.divide(input, other)