import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50, 32)
conv_transpose2d = torch.nn.ConvTranspose2d(in_channels=16, out_channels=33, kernel_size=3, stride=2)
output = conv_transpose2d(input)