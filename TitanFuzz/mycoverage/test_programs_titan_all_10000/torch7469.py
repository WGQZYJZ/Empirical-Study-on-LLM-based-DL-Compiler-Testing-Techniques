import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
torch.matrix_power(input, 3)
input1 = torch.randn(2, 3)
input2 = torch.randn(3, 2)
torch.mm(input1, input2)