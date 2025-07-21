import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 6, 6, 6)
conv = torch.nn.LazyConv3d(out_channels=3, kernel_size=3, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)
output = conv(input)