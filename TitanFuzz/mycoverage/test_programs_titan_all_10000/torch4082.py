import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50, 32)
output = torch.nn.functional.lp_pool2d(input, 2, (2, 2))