import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 3, 4)
mat2 = torch.randn(10, 4, 5)
torch.bmm(input, mat2)
a = torch.randn(3, 4)
b = torch.randn(3, 4)
torch.cat((a, b))