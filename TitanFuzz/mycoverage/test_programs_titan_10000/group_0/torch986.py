import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(1, dtype=torch.float64)
other = torch.rand(1, dtype=torch.float64)
torch.igammac(input, other)