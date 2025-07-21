import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
output = torch.rot90(input, 1, [0, 1])