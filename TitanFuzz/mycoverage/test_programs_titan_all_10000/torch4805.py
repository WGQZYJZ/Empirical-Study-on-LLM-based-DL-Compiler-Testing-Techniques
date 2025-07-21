import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
conv_transpose_2d = torch.nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0, output_padding=0)
output = conv_transpose_2d(input_data)