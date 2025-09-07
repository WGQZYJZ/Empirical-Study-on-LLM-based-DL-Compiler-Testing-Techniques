import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3, requires_grad=True)
weight = torch.randn(1, 1, 2, 2, requires_grad=True)
output = torch.nn.functional.conv_transpose2d(input, weight)