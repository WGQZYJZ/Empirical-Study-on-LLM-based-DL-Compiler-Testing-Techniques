import torch
from torch import nn
from torch.autograd import Variable
in_channels = 2
out_channels = 3
kernel_size = 4
batch_size = 3
input_data = torch.randn(batch_size, in_channels, kernel_size)
conv_transpose_1d = torch.nn.ConvTranspose1d(in_channels, out_channels, kernel_size)
output_data = conv_transpose_1d(input_data)