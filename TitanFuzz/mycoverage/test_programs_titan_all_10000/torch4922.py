import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4, 5)
output = torch.moveaxis(input, 0, 2)
input = torch.randn(3, 4, 5)
output = torch.moveaxis(input, 1, 2)
input = torch.randn(3, 4, 5)
output = torch.moveaxis(input, 2, 1)