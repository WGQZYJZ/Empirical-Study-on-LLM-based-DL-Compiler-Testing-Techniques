import torch
from torch import nn
from torch.autograd import Variable
inp = torch.randn(1, 10)
mat1 = torch.randn(10, 20)
mat2 = torch.randn(20, 10)
out = torch.addmm(inp, mat1, mat2)