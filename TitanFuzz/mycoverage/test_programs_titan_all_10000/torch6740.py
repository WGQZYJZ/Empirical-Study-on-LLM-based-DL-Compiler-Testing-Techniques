import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.randint_like(input, low=0, high=10)