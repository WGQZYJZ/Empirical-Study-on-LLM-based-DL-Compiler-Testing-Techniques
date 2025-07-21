import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.randn(4, 4)
input2 = torch.randn(4, 4)
torch.special.gammaincc(input1, input2, out=None)