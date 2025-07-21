import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
mat2 = torch.randn(2, 4, 5)
output = torch.bmm(input, mat2)