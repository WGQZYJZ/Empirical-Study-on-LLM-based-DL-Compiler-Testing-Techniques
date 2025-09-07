import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 4)
torch.nn.functional.unfold(input, kernel_size=(2, 2), dilation=1, padding=0, stride=1)
input = torch.randn(2, 3, 4, 4)