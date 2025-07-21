import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3, 3)
output = torch.flip(input, dims=[1])