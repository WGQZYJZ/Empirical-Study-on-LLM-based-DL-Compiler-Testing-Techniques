import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 5, 5)
conv_transpose2d = torch.nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=3, stride=2, padding=1, output_padding=1)
output = conv_transpose2d(input)