import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 4, 4, 4))
conv_transpose3d = torch.nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0)
output = conv_transpose3d(input_data)