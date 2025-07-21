import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
out = torch.randint_like(input, low=0, high=10, dtype=torch.float)