import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5)
conv_transpose2d = torch.nn.ConvTranspose2d(1, 1, 3, stride=2, padding=1, output_padding=1)
output_data = conv_transpose2d(input_data)