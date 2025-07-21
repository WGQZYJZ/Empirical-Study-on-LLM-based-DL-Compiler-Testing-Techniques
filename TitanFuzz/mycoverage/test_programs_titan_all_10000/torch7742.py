import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 5)
output = torch.swapdims(input, 0, 2)