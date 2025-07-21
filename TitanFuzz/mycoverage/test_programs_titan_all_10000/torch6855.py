import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 2)
output = torch.randint_like(input, low=0, high=10)