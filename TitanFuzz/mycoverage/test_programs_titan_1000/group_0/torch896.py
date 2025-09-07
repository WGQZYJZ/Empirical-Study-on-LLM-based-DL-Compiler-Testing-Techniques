import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, 4)
output = torch.flip(input, [1, 3])