import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 5, 7)
output = torch.nn.AdaptiveMaxPool2d(output_size=(3, 3))(input)