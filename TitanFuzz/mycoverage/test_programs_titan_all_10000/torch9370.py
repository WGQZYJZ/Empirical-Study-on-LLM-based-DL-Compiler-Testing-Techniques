import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 5)
torch.nn.LazyConv1d(out_channels=3, kernel_size=3, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)
torch.nn.LazyConv1d(out_channels=3, kernel_size=3, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)(input_data)
torch.nn.LazyConv1d(out_channels=3, kernel_size=3, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)(input_data).shape
torch.nn