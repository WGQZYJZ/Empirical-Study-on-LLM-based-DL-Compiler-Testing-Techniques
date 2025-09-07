import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(100, 100)
input[0][0] = float('nan')
result = torch.nanmedian(input)