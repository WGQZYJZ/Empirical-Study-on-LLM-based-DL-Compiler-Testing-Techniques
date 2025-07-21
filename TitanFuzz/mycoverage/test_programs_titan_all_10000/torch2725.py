import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4)
output = torch.nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=2, stride=2)(input)