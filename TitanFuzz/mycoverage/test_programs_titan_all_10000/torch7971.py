import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4, 4, 4)
conv_transpose3d = torch.nn.ConvTranspose3d(in_channels=3, out_channels=2, kernel_size=3, stride=2, padding=1)
output_data = conv_transpose3d(input_data)