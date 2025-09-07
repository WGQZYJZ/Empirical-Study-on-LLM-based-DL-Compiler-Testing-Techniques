import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
mat2 = torch.randn(3, 3)
torch.mm(input, mat2, out=None)