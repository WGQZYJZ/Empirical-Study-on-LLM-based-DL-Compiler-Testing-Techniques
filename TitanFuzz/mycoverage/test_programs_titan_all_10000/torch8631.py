import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, requires_grad=True)
output = torch.rad2deg(input)