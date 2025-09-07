import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(4, 4)
output = torch.full_like(input, 2)