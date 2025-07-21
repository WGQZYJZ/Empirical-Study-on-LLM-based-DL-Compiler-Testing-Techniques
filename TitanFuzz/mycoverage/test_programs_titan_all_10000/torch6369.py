import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 5, 5))
upsampling_bilinear2d = torch.nn.UpsamplingBilinear2d(size=None, scale_factor=2)
output_data = upsampling_bilinear2d(input_data)