import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4)
output = torch.nn.AdaptiveMaxPool2d((3, 3))(input)