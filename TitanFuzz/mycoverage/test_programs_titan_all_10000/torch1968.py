import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
mat2 = torch.randn(4, 5)
torch.mm(input, mat2)
out = torch.randn(3, 5)
torch.mm(input, mat2, out=out)
out