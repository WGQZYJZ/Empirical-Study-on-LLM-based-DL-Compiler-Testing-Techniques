import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(4, 4)
other = torch.rand(4, 4)
result = torch.fmod(input, other)
input = torch.rand(4, 4)
result = torch.frac(input)