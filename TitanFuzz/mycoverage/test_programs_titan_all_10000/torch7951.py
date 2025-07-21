import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, dtype=torch.float)
other = torch.randn(4, dtype=torch.float)
output = torch.fmod(input, other)