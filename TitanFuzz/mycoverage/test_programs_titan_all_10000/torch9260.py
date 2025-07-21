import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3, 3)
output = torch.nn.ConvTranspose3d(1, 1, 3, stride=1, padding=0, output_padding=0, bias=False)(input)