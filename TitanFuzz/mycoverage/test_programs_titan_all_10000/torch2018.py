import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 5)
torch.nn.LazyConvTranspose1d(out_channels=3, kernel_size=2, stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)