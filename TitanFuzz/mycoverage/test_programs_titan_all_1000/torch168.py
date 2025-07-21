import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10, 3, 4)
mat2 = torch.rand(10, 4, 5)
output = torch.bmm(input, mat2)