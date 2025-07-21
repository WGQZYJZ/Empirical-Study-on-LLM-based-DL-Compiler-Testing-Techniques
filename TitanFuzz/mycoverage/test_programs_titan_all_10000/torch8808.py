import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
chunks = torch.chunk(input, 2, dim=0)
chunks = torch.chunk(input, 2, dim=1)