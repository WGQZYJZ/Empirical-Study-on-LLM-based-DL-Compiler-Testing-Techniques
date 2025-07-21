import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4, 4)
conv_transpose3d = torch.nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=2, stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)