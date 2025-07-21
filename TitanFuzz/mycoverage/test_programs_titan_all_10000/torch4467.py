import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 3, dtype=torch.float)
other = torch.randn(5, 3, dtype=torch.float)
out = torch.remainder(input, other)