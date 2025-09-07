import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, 3, 3, 3)
conv = torch.nn.Conv3d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)