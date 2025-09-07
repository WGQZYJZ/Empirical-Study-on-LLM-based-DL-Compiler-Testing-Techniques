import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
input[0][0] = float('inf')
input[1][0] = float('-inf')
input[2][0] = float('nan')
input[3][0] = float('nan')
output = torch.isposinf(input)