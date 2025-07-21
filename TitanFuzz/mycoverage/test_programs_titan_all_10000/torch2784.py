import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 1, 5, 5)
weight = torch.rand(1, 1, 3, 3)
output_data = torch.nn.functional.conv_transpose2d(input_data, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1)