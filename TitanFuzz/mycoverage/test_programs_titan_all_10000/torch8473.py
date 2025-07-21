import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 10)
output = torch.nn.functional.lp_pool1d(input, 2, 3, 2)