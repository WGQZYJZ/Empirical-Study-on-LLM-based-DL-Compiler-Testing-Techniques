import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(5, 3)
other = torch.rand(5, 3)
output = torch.isclose(input, other)