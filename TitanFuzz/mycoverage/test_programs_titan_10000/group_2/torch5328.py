import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3, dtype=torch.float32)
output = torch.rand_like(input, dtype=torch.float32)