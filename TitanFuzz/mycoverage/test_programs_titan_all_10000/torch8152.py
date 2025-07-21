import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 4, 6, 6, 6)
output = torch.nn.AdaptiveAvgPool3d((2, 2, 2))(input)