import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5)
conv = torch.nn.Conv2d(1, 1, 3, stride=1, padding=1, bias=False)
output = conv(input_data)