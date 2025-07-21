import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, requires_grad=True)
output = torch.nn.functional.lp_pool1d(input, 1, 3, stride=2)