import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 5)
output = torch.swapaxes(input, 0, 1)