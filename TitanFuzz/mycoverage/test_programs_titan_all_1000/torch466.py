import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
input[0] = float('nan')
input[1] = float('inf')
input[2] = float('-inf')
output = torch.nan_to_num(input)