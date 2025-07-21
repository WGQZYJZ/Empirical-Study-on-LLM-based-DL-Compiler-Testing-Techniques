import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
chunks = torch.chunk(input, 2, dim=1)