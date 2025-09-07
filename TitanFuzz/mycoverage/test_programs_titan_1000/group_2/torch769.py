import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([1.0, 2.0, 3.0])
output = torch.special.i0(input)