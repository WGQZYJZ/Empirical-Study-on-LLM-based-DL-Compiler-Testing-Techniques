import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0], [1, 1, 0]])
output = torch.masked_select(input, mask)