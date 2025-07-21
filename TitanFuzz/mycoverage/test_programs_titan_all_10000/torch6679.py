import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 5, 5)
unfold = torch.nn.Unfold(kernel_size=(3, 3), dilation=1, padding=0, stride=1)
output = unfold(input)