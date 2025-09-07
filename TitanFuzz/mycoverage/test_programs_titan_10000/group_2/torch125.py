import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(5, 5, dtype=torch.float)
other = torch.randn(5, 5, dtype=torch.float)
output = torch.div(input, other)