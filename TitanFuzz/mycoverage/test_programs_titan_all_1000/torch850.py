import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 3, 4)
mat2 = torch.randn(10, 4, 5)
torch.bmm(input, mat2)